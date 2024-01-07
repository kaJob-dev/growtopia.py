__all__ = (
    "PacketType",
    "VariantType",
    "GameUpdatePacketFlags",
    "GameUpdatePacketType",
    "PlayerEffectFlag",
)

from enum import IntEnum


class PacketType(IntEnum):
    """
    An integer enumeration of all packet types.
    """

    UNKNOWN = 0
    HELLO = 1
    TEXT = 2
    GAME_MESSAGE = 3
    GAME_UPDATE = 4

    # Custom variant type aliases.
    CONTAINS_TEXT = 2  # TEXT but applies to GAME_MESSAGE too.

    @classmethod
    def _missing_(cls, _: int) -> "PacketType":
        return cls.UNKNOWN


class VariantType(IntEnum):
    """
    An integer enumeration of all variant types.
    """

    NONETYPE = 0
    FLOAT = 1
    STR = 2
    VECTOR2 = 3
    VECTOR3 = 4
    UINT = 8
    INT = 9

    # Custom variant type aliases.
    DIALOG = 2  # str
    BOOL = 9

    @classmethod
    def _missing_(cls, _):
        return cls.NONETYPE


class GameUpdatePacketFlags(IntEnum):
    """
    An integer enumeration of all game update packet flags.
    """

    NONE = 0
    EXTRA_DATA = 8
    FACING_LEFT = 16

    @classmethod
    def _missing_(cls, _):
        return cls.NONE


class GameUpdatePacketType(IntEnum):
    """
    An integer enumeration of all game update packet types.
    """

    UNKNOWN = 99

    STATE_UPDATE = 0
    CALL_FUNCTION = 1
    UPDATE_STATUS = 2
    TILE_CHANGE_REQUEST = 3
    SEND_MAP_DATA = 4
    SEND_TILE_UPDATE_DATA = 5
    SEND_TILE_UPDATE_DATA_MULTIPLE = 6
    TILE_ACTIVATE_REQUEST = 7
    TILE_APPLY_DAMAGE = 8
    SEND_INVENTORY_STATE = 9
    ITEM_ACTIVATE_REQUEST = 10
    ITEM_ACTIVATE_OBJECT_REQUEST = 11
    SEND_TILE_TREE_STATE = 12
    MODIFY_ITEM_INVENTORY = 13
    ITEM_CHANGE_OBJECT = 14
    SEND_LOCK = 15
    SEND_ITEMS_DATA = 16
    SEND_PARTICLE_EFFECT = 17
    SET_ICON_STATE = 18
    ITEM_EFFECT = 19
    SET_CHARACTER_STATE = 20
    PING_REPLY = 21
    PING_REQUEST = 22
    GOT_PUNCHED = 23
    APP_CHECK_RESPONSE = 24
    APP_INTEGRITY_FAIL = 25
    DISCONNECT = 26
    BATTLE_JOIN = 27
    BATTLE_EVENT = 28
    USE_DOOR = 29
    SEND_PARENTAL = 30
    GONE_FISHIN = 31
    STEAM = 32
    PET_BATTLE = 33
    NPC = 34
    SPECIAL = 35
    SEND_PARTICLE_EFFECT_V2 = 36
    ACTIVE_ARROW_TO_ITEM = 37
    SELECT_TILE_INDEX = 38
    SEND_PLAYER_TRIBUTE_DATA = 39

    @classmethod
    def _missing_(cls, _):
        return cls.UNKNOWN


class PlayerEffectFlag(IntEnum):
    """
    An integer enumeration of all player effect flags.
    """

    NOCLIP = 0
    DOUBLE_JUMP = 1
    INVISIBLE = 2
    NO_HAND = 3
    NO_EYE = 4
    NO_BODY = 5
    DEVIL_HORNS = 6
    GOLDEN_HALO = 7
    # ???????? = 8
    FIRE_PROOF = 9
    SPIKE_PROOF = 10
    FROZEN = 11
    CURSED = 12
    DUCT_TAPE = 13
    CIGAR = 14
    SHINING = 15
    ZOMBIE = 16
    RED_BODY = 17
    HAUNTED_SHADOWS = 18
    GEIGER_RADIATION = 19
    SPOTLIGHT = 20
    YELLOW_BODY = 21
    PINEAPPLE = 22
    FLYING_PINEAPPLE = 23
    SUPPORTER_NAME = 24
    SUPPER_PINEAPPLE = 25
    CIRCLE_BUBBLE = 26
    FLOODED = 27
    NEON_GUM_FACE_PINK = 28
    NEON_GUM_FACE = 29
    NEON_GUM_FACE_YELLOW = 30
    NEON_GUM_FACE_GREEN = 31

    @classmethod
    def _missing_(cls, _):
        return cls.UNKNOWN
