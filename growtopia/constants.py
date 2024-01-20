__all__ = (
    "IGNORED_ATTRS",
    "ITEM_ATTR_SIZES",
    "ANSI_ESCAPE",
    "LOG_LOOP_SLEEP_TIME",
)

LOG_LOOP_SLEEP_TIME: float = 0.2  # time to sleep between each flush, (currently 200ms)

IGNORED_ATTRS: dict[int, list[str]] = {
    11: ["flags3", "bodypart", "flags4", "flags5", "unknown", "sit_file", "renderer_file"],
    12: ["flags4", "flags5", "unknown", "sit_file", "renderer_file"],
    13: ["flags5", "unknown", "sit_file", "renderer_file"],
    14: ["unknown", "sit_file", "renderer_file"],
    15: ["renderer_file"],
    16: [],
}

ITEM_ATTR_SIZES: dict[str, int] = {
    "id": 4,
    "editable_type": 1,
    "category": 1,
    "action_type": 1,
    "hit_sound_type": 1,
    "texture_hash": 4,
    "kind": 1,
    "flags1": 4,
    "texture_x": 1,
    "texture_y": 1,
    "spread_type": 1,
    "is_stripey_wallpaper": 1,
    "collision_type": 1,
    "break_hits": 1,
    "reset_time": 4,
    "clothing_type": 1,
    "rarity": 2,
    "max_amount": 1,
    "extra_file_hash": 4,
    "audio_volume": 4,
    "seed_base": 1,
    "seed_overlay": 1,
    "tree_base": 1,
    "tree_leaves": 1,
    "seed_colour": 4,
    "seed_overlay_colour": 4,
    "ingredient": 4,
    "grow_time": 4,
    "flags2": 2,
    "rayman": 2,
    "reserved": 80,
    "flags3": 4,
    "bodypart": 9,
    "flags4": 4,
    "flags5": 4,
    "unknown": 25,
}

ANSI_ESCAPE: dict[str, str] = {
    "bold": "1",
    "underline": "4",
    "reverse": "7",
    "invisible": "8",
    "red": "31",
    "green": "32",
    "yellow": "33",
    "blue": "34",
    "reset": "0",
    "clear": "c",
}  # we can add more later (if we need them)
