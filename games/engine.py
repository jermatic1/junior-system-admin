"""Shared choose-your-own-adventure engine for simple terminal games."""

import textwrap
import time
from copy import deepcopy

from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt

DEFAULT_THEME = {
    "primary": "cyan",
    "text": "bold white",
    "dim": "grey50",
    "banner": "bold reverse violet",
    "prompt": "What do you do?",
    "typewriter_delay": 0.015,
    "width": 90,
    "exit_hint": "Press [bold]Ctrl+C[/bold] anytime to exit.",
}

console = Console(width=DEFAULT_THEME["width"])


def _theme(overrides: dict | None) -> dict:
    merged = dict(DEFAULT_THEME)
    if overrides:
        merged.update(overrides)
    return merged


def typewriter(text: str, style: str, delay: float, width: int) -> None:
    wrapped = textwrap.fill(text, width=width)
    for char in wrapped:
        console.print(char, end="", style=style)
        time.sleep(delay)
    console.print()


def _matches(stats: dict, require: dict) -> bool:
    for key, value in require.items():
        if stats.get(key) != value:
            return False
    return True


def _apply_effects(stats: dict, choice: dict) -> None:
    for key, amount in choice.get("add", {}).items():
        stats[key] = stats.get(key, 0) + amount
    for key, value in choice.get("set", {}).items():
        stats[key] = value

    if "hull" in stats and stats["hull"] > 100:
        stats["hull"] = 100


def _check_stat_endings(stats: dict, stat_endings: dict | None) -> str | None:
    """If a tracked stat is at or below its limit, return that ending scene key."""
    if not stat_endings:
        return None
    for stat_name, (limit, scene_key) in stat_endings.items():
        if stats.get(stat_name, 0) <= limit:
            return scene_key
    return None


def _resolve_branches(scene: dict, stats: dict) -> str | None:
    """Return next scene from a branches list, or None if this is not a branch scene."""
    branches = scene.get("branches")
    if not branches:
        return None
    default_next = None
    for branch in branches:
        require = branch.get("require")
        if require is None:
            default_next = branch["next"]
            continue
        if _matches(stats, require):
            return branch["next"]
    return default_next


def _render_hud(stats: dict, theme: dict, hud_labels: dict | None) -> None:
    if not stats:
        return
    labels = hud_labels or {}
    parts = []
    for key, value in stats.items():
        label = labels.get(key, key.replace("_", " ").title())
        if isinstance(value, bool):
            display = "FOUND" if value else "MISSING"
        elif key == "hull":
            display = f"{value}%"
        else:
            display = str(value)
        parts.append(f"{label}: [bold white]{display}[/bold white]")
    console.print(
        Panel(
            "  |  ".join(parts),
            title="[bold]STATUS[/bold]",
            title_align="left",
            style=theme["dim"],
            expand=False,
        )
    )


def play_scene(
    story: dict,
    scene_key: str,
    stats: dict,
    theme: dict,
    *,
    show_hud: bool = False,
    hud_labels: dict | None = None,
    stat_endings: dict | None = None,
) -> str | None:
    """Render one scene and return the next scene key, or None at an ending."""
    scene = story.get(scene_key)
    if not scene:
        console.print(f"[bold red]Error: Scene '{scene_key}' not found![/bold red]")
        return None

    branch_next = _resolve_branches(scene, stats)
    if branch_next is not None and "text" not in scene:
        return branch_next

    color = scene.get("color", theme["primary"])
    divider = theme.get("divider", "=" * 60)

    console.print(f"\n{divider}\n")
    if show_hud:
        _render_hud(stats, theme, hud_labels)
        console.print()

    console.print(Panel(f"[bold]{scene['title']}[/bold]", style=color, expand=False))
    console.print()

    if "text" in scene:
        typewriter(scene["text"], theme["text"], theme["typewriter_delay"], theme["width"])
        console.print()

    if branch_next is not None:
        return branch_next

    choices = scene.get("choices") or {}
    if not choices:
        return None

    valid_options = []
    for option, details in choices.items():
        console.print(f" [bold {color}][{option}][/bold {color}] {details['text']}")
        valid_options.append(option)
    console.print()

    user_choice = ""
    while user_choice not in valid_options:
        user_choice = Prompt.ask(
            f"[bold {color}]{theme['prompt']}[/bold {color}]",
            choices=valid_options,
        ).strip()

    choice = choices[user_choice]
    _apply_effects(stats, choice)

    ending = _check_stat_endings(stats, stat_endings)
    if ending:
        return ending

    return choice["next"]


def play(
    story: dict,
    start: str,
    *,
    stats: dict | None = None,
    title: str = "Adventure",
    subtitle: str = "A Python Adventure",
    banner_body: str | None = None,
    theme: dict | None = None,
    show_hud: bool = False,
    hud_labels: dict | None = None,
    stat_endings: dict | None = None,
    replay_prompt: str = "Would you like to play again?",
    goodbye: str = "Thank you for playing!",
) -> None:
    """Run a full game loop with optional replay."""
    global console
    theme = _theme(theme)
    console = Console(width=theme["width"])
    initial_stats = deepcopy(stats) if stats is not None else {}

    try:
        while True:
            current_stats = deepcopy(initial_stats)
            console.clear()

            if banner_body:
                console.print(
                    Panel.fit(
                        banner_body,
                        style=theme["banner"],
                        subtitle=subtitle,
                    )
                )
            else:
                console.print(
                    Panel.fit(
                        f"   {title}   ",
                        style=theme["banner"],
                        subtitle=subtitle,
                    )
                )
            console.print(f"\n[{theme['dim']}]{theme['exit_hint']}[/{theme['dim']}]\n")

            current_scene = start
            while current_scene:
                current_scene = play_scene(
                    story,
                    current_scene,
                    current_stats,
                    theme,
                    show_hud=show_hud,
                    hud_labels=hud_labels,
                    stat_endings=stat_endings,
                )

            console.print(f"\n{theme.get('divider', '=' * 60)}\n")
            replay = Prompt.ask(replay_prompt, choices=["y", "n"], default="y")
            if replay.lower().strip() != "y":
                console.print(f"[bold green]{goodbye}[/bold green]")
                break
    except KeyboardInterrupt:
        console.print(f"\n\n[bold green]{goodbye}[/bold green]")
