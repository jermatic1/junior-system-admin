"""The Iron Gates — a short choose-your-own-adventure."""

from engine import play

# ---------------------------------------------------------
# STORY DATA (edit this section to change the adventure!)
# ---------------------------------------------------------
STORY = {
    "start": {
        "title": "The Iron Gates",
        "color": "cyan",
        "text": (
            "You stand before a pair of towering iron gates at the edge of a whispering forest. "
            "A cold breeze cuts through your jacket. To the left, a broken wall offers a way inside. "
            "To the right, a dark path winds deep into the trees."
        ),
        "choices": {
            "1": {"text": "Climb through the broken wall", "next": "courtyard"},
            "2": {"text": "Follow the dark forest path", "next": "forest_path"},
        },
    },
    "courtyard": {
        "title": "The Ruined Courtyard",
        "color": "green",
        "text": (
            "You scramble over the rubble into a crumbling courtyard. In the center sits an old "
            "stone fountain brimming with shimmering, clear water. A heavy wooden door ahead "
            "stands slightly ajar."
        ),
        "choices": {
            "1": {"text": "Drink from the shimmering fountain", "next": "fountain_death"},
            "2": {"text": "Push open the heavy wooden door", "next": "castle_win"},
        },
    },
    "forest_path": {
        "title": "The Whispering Woods",
        "color": "yellow",
        "text": (
            "The canopy blocks out the light as you walk. Red eyes flash in the dark foliage ahead. "
            "You hear a low growl rolling through the shadows."
        ),
        "choices": {
            "1": {
                "text": "Draw your pocket knife and stand your ground",
                "next": "wolf_death",
            },
            "2": {
                "text": "Turn around and run back to the iron gates",
                "next": "start",
            },
        },
    },
    "fountain_death": {
        "title": "Game Over: A Fool's Thirst",
        "color": "red",
        "text": (
            "The water is sweet, but instantly paralyzing. The magic of the courtyard consumes you. "
            "You are now part of the fountain's history."
        ),
        "choices": {},
    },
    "wolf_death": {
        "title": "Game Over: Consumed by Shadows",
        "color": "red",
        "text": (
            "A massive shadow-wolf leaps from the brush. Your small knife is no match for its "
            "supernatural strength. The forest claims another soul."
        ),
        "choices": {},
    },
    "castle_win": {
        "title": "Victory: Safe Haven",
        "color": "bright_magenta",
        "text": (
            "You slip inside the castle just as heavy rain begins to pour outside. Inside is warm, "
            "dry, and completely safe. You have survived the adventure!"
        ),
        "choices": {},
    },
}


def main() -> None:
    play(
        STORY,
        start="start",
        title="THE IRON GATES",
        subtitle="A Python Adventure",
        theme={
            "banner": "bold reverse violet",
            "prompt": "What do you do?",
        },
    )


if __name__ == "__main__":
    main()
