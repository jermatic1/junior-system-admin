"""Starship Traveller — a deep-space choose-your-own-adventure."""

from engine import play

# ---------------------------------------------------------
# STORY DATA (edit this section to change the adventure!)
# ---------------------------------------------------------
STORY = {
    "wormhole_arrival": {
        "title": "ENTRY LOG: SECTOR 44-X",
        "text": (
            "Your ship emerges from a violent gravity rip in space. The navigation terminal shows "
            "unknown stars. You are trapped in an unmapped galaxy. Hull shielding is stable, but "
            "fuel cells are burning down. Ahead lie two distinct anomalies to explore for resources."
        ),
        "choices": {
            "1": {
                "text": "Set course toward a dense, foggy Nebular Grid",
                "next": "nebula_grid",
            },
            "2": {
                "text": "Approach a barren rogue moon reflecting strange metallic signals",
                "next": "metallic_moon",
            },
        },
    },
    "nebula_grid": {
        "title": "THE RADION FOG GRID",
        "text": (
            "The starship cuts through thick ion clouds. Static crackles over the comms. Suddenly, "
            "an automated derelict freighter drifts into view. It displays no life signs but its "
            "emergency storage hangar doors are hanging wide open."
        ),
        "choices": {
            "1": {
                "text": "Send a recon team inside the freighter's hangar bay",
                "next": "freighter_salvage",
            },
            "2": {
                "text": "Ignore the debris and continue searching the cloud barrier",
                "next": "nebula_empty",
            },
        },
    },
    "freighter_salvage": {
        "title": "DERELICT CARGO RACK",
        "text": (
            "Your team boards the freezing freighter. Among broken crates, they discover a locked "
            "safe with binary code and an auxiliary fuel drum! You haul the drum back to the ship."
        ),
        "choices": {
            "1": {
                "text": "Extract fuel from the drum to restock energy cells (+1 Fuel)",
                "next": "wormhole_arrival",
                "add": {"fuel": 1},
            },
            "2": {
                "text": "Attempt to crack the encrypted military safe block",
                "next": "safe_crack",
            },
        },
    },
    "safe_crack": {
        "title": "ENCRYPTED VAULT DATA",
        "text": (
            "Using the ship's computer, you run an override. Success! Inside is an Ancient Language "
            "Translation Matrix Module. This might help talk to local civilizations."
        ),
        "choices": {
            "1": {
                "text": "Install the Matrix decoder onto the main terminal",
                "next": "wormhole_arrival",
                "set": {"has_decoder": True},
            },
        },
    },
    "nebula_empty": {
        "title": "GRAVITY WELL TRAP",
        "text": (
            "The nebula hides a localized micro-black hole. The gravitational shear strains your "
            "ship's frame before the sub-light engines can tear you free."
        ),
        "choices": {
            "1": {
                "text": "Divert full power to forward thrusters (-15 Hull, -1 Fuel)",
                "next": "wormhole_arrival",
                "add": {"hull": -15, "fuel": -1},
            },
        },
    },
    "metallic_moon": {
        "title": "OUTPOST SIGMA-9",
        "text": (
            "You orbit the desolate rocky moon. An underground city covered by a geodesic dome "
            "lights up your scan. As you approach, an alien combat cruiser interceptor demands "
            "identification on an unknown frequency."
        ),
        "choices": {
            "1": {
                "text": "Hail the cruiser and attempt to broadcast communications",
                "next": "alien_hail",
            },
            "2": {
                "text": "Raise defensive tactical shields and attempt to outfly them",
                "next": "space_dogfight",
            },
        },
    },
    "alien_hail": {
        "title": "FIRST CONTACT FREQUENCY",
        "text": (
            "You beam out a broad-spectrum greeting signal. The alien captain answers, but their "
            "language is completely unrecognizable clicks and hums. They raise their target "
            "acquisition lasers."
        ),
        "choices": {
            "1": {
                "text": "Check if your collected ship components can translate the message",
                "next": "check_translation_matrix",
            },
            "2": {
                "text": "Break off transmission and engage evasive maneuvers",
                "next": "space_dogfight",
            },
        },
    },
    "check_translation_matrix": {
        "title": "MATRIX RESOLUTION RUNNING",
        "text": "Checking inventory databases...",
        "branches": [
            {"require": {"has_decoder": True}, "next": "victory_home"},
            {"next": "no_translation_fail"},
        ],
    },
    "space_dogfight": {
        "title": "ORBITAL ESCAPE RUN",
        "text": (
            "The cruiser fires a burst of pulse-slugs! You barrel-roll through the canyon line of "
            "the moon, escaping back into deep space but taking direct damage to your engine "
            "shielding rings."
        ),
        "choices": {
            "1": {
                "text": "Re-route auxiliary engine coolant pumps (-20 Hull, -1 Fuel)",
                "next": "wormhole_arrival",
                "add": {"hull": -20, "fuel": -1},
            },
        },
    },
    "victory_home": {
        "title": "TRANSLATION SUCCESS: THE WAY HOME",
        "text": (
            "The Translation Matrix pairs flawlessly! The alien captain smiles, realizing you are "
            "a lost explorer. They transmit the specific stellar pulsar jump path back to Earth's "
            "sector. You fire up the hyperdrive and break orbit. Mission success, Captain!"
        ),
        "choices": {},
    },
    "no_translation_fail": {
        "title": "COMMUNICATION BREACH",
        "text": (
            "Without a decryption module, you cannot understand them. Interpreting your silence as "
            "hostile, the alien cruiser launches a target-seeking missile that shatters your fuel "
            "alignment array."
        ),
        "choices": {
            "1": {
                "text": "Attempt a blind emergency jump away (-30 Hull, -2 Fuel)",
                "next": "wormhole_arrival",
                "add": {"hull": -30, "fuel": -2},
            },
        },
    },
    "death_destroyed": {
        "title": "SYSTEM FAILURE: HULL COMPROMISED",
        "text": (
            "Hull integrity hits zero percent. The bulkheads buckle under deep space atmospheric "
            "pressures. The Starship Traveller breaks apart into cosmic remnants."
        ),
        "choices": {},
    },
    "death_stranded": {
        "title": "CRITICAL EMERGENCY: FUEL CELLS DEPLETED",
        "text": (
            "Your fuel readouts drop to empty. The reactors go silent, the life support switches to "
            "reserve emergency tanks, and your starship drifts indefinitely among the cold stars."
        ),
        "choices": {},
    },
}

THEME = {
    "primary": "grey37",
    "text": "grey70",
    "dim": "grey54",
    "banner": "bold white on grey54",
    "prompt": "Select Navigation Vector",
    "typewriter_delay": 0.01,
    "divider": "═" * 65,
}

STARTING_STATS = {
    "hull": 100,
    "fuel": 3,
    "has_decoder": False,
}

HUD_LABELS = {
    "hull": "Hull Matrix",
    "fuel": "Fuel Stocks",
    "has_decoder": "Decoder Module",
}

# If a stat drops to this value or below, jump to that ending scene
STAT_ENDINGS = {
    "hull": (0, "death_destroyed"),
    "fuel": (0, "death_stranded"),
}


def main() -> None:
    play(
        STORY,
        start="wormhole_arrival",
        stats=STARTING_STATS,
        title="STARSHIP TRAVELLER",
        subtitle="[Core OS 2.6.4]",
        banner_body=(
            " \n  STARSHIP TRAVELLER OPERATING SYSTEM \n"
            "  COMMENCING DEEP SPACE SECTOR SCAN  \n "
        ),
        theme=THEME,
        show_hud=True,
        hud_labels=HUD_LABELS,
        stat_endings=STAT_ENDINGS,
        replay_prompt="Reinitialize jump drive simulator to run a new iteration?",
        goodbye="Console Feed Closed. Terminal offline.",
    )


if __name__ == "__main__":
    main()
