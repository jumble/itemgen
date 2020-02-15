from enum import Enum

from random_utils import get_random_bool, get_random_list_value, get_random_enum_value
from random_utils import bag_pull

################
# Weapon Types #
################
class WeaponTypes(Enum):
    SWORD  = 0
    SPEAR  = 1
    SHIELD = 2
    HORN   = 3
    CLOAK  = 4

WEAPON_TYPE_GENERATOR = bag_pull(WeaponTypes)

WEAPON_TYPE_NAME_GENERATORS = [
    bag_pull(["KHOPESH", "SCIMITAR", "SHOTEL", "DAO", "FALCHION"]),
    bag_pull(["JAVELIN", "HARPOON", "BOARSPEAR", "PIKE", "FAUCHARD"]),
    bag_pull(["BUCKLER", "TARGE", "WALL"]),
    bag_pull(["HORN", "GJALLARHORN"]),
    bag_pull(["CLOAK", "TOGA", "PALLIUM"])
]

####################
# Weapon Materials #
####################
METALS = ["BRONZE", "IRON", "SILVER", "STEEL", "OBSIDIAN"]
HORN_MATERIALS = METALS + ["BONE"]
FABRICS = ["SILK", "SATIN", "VELVET", "FUR"]

METAL_GENERATOR = bag_pull(METALS)

WEAPON_TYPE_MATERIAL_GENERATORS = [
    METAL_GENERATOR,
    METAL_GENERATOR,
    METAL_GENERATOR,
    bag_pull(HORN_MATERIALS),
    bag_pull(FABRICS)
]

##################
# Weapon Affixes #
##################
class WeaponAffixes(Enum):
    FIRE = 0
    ICE = 1
    LIGHTNING = 2

class WeaponAffixType(Enum):
    PREFIX = 0
    SUFFIX = 1
    COMBO = 2

WEAPON_AFFIX_COMBO_LEGALITY_MAP = [ # prefix -> valid suffixes
    [2], # fire -> lightning
    [2], # ice -> lightning
    [0, 1] # lightning -> fire, ice
]

WEAPON_AFFIX_NAME_GENERATORS = [
    # format: ([PREFIX_LIST], [SUFFIX_LIST])
    (
        bag_pull(["EMBER", "SMOKE-WREATHED", "FLAME-LICKED", "BLAZING", "INFERNAL"]), 
        bag_pull(["INFLAMMATA", "ABLAZE", "INFERIUM", "of the ETERNAL FLAME"])
    ),(
        bag_pull(["NUMBING", "FROSTBOUND", "GLACIAL", "HOARFROST"]), 
        bag_pull(["of PERMAFROST", "FRIGIUS"])
    ),(
        bag_pull(["SPARKWOVEN", "SURGETOUCHED", "SKYRENDING"]), 
        bag_pull(["of the EVERSTORM", "of FRACTAR", "of the HEAVENS' WRATH"])
    )
]

#################
# Actual Shtuff #
#################
def get_weapon_seed(weapon_type: WeaponTypes = None, weapon_affix: WeaponAffixes = None, weapon_affix_type: WeaponAffixType = None) -> tuple:
    if weapon_type == None:
        weapon_type = next(WEAPON_TYPE_GENERATOR)
    elif type(weapon_type) == list:
        weapon_type = get_random_list_value(weapon_type)
    
    if weapon_affix == None:
        weapon_affix = get_random_enum_value(WeaponAffixes)
    elif type(weapon_affix) == list:
        weapon_affix = get_random_list_value(weapon_affix)
    
    if weapon_affix_type == None:
        weapon_affix_type = get_random_enum_value(WeaponAffixType)
    elif type(weapon_affix_type) == list:
        weapon_affix_type = get_random_list_value(weapon_affix_type)
    
    return (weapon_type, weapon_affix, weapon_affix_type)

def get_weapon_name(weapon_seed: tuple = None):
    if weapon_seed == None:
        weapon_seed = get_weapon_seed()

    weapon_type, weapon_affix, weapon_affix_type = weapon_seed

    resolved_weapon_type = next(WEAPON_TYPE_NAME_GENERATORS[weapon_type.value])

    if weapon_affix_type == WeaponAffixType.COMBO:
        resolved_weapon_prefix = next(WEAPON_AFFIX_NAME_GENERATORS[weapon_affix.value][WeaponAffixType.PREFIX.value])
        legal_suffix_types = WEAPON_AFFIX_COMBO_LEGALITY_MAP[weapon_affix.value]
        resolved_suffix_type = get_random_list_value(legal_suffix_types)
        resolved_weapon_suffix = next(WEAPON_AFFIX_NAME_GENERATORS[resolved_suffix_type][WeaponAffixType.SUFFIX.value])
        weapon_name_tokens = [resolved_weapon_prefix, resolved_weapon_type, resolved_weapon_suffix]

    else:
        resolved_weapon_affix = next(WEAPON_AFFIX_NAME_GENERATORS[weapon_affix.value][weapon_affix_type.value])

        weapon_name_tokens = []

        # chance to include material_name
        include_material_name = get_random_bool()
        if include_material_name:
            material_name = next(WEAPON_TYPE_MATERIAL_GENERATORS[weapon_type.value])

        if weapon_affix_type == WeaponAffixType.PREFIX:
            weapon_name_tokens.append(resolved_weapon_affix)
            if include_material_name:
                weapon_name_tokens.append(material_name)
            weapon_name_tokens.append(resolved_weapon_type)
        else: # SUFFIX
            if include_material_name:
                weapon_name_tokens.append(material_name)
            weapon_name_tokens.append(resolved_weapon_type)
            weapon_name_tokens.append(resolved_weapon_affix)
    
    weapon_name = " ".join(weapon_name_tokens)

    return weapon_name
