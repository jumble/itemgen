# RPG Item Name Generator

Generates really over-the-top names of items that sound like they're from an RPG, anime or some such bullshit.
If you want, you can specify a seed to narrow down the kinds of item names that will be created.

```
In [1]: from name_generator import *

In [2]: for _ in range(5):
   ...:     print(get_weapon_name())
   ...: 
SMOKE-WREATHED WALL of the EVERSTORM
SPARKWOVEN TOGA FRIGIUS
BLAZING FAUCHARD of the HEAVENS' WRATH
SURGETOUCHED GJALLARHORN
SKYRENDING DAO INFLAMMATA

In [3]: very_specific_seed = get_weapon_seed(
   ...:     weapon_type=WeaponTypes.SWORD,
   ...:     weapon_affix=WeaponAffixes.FIRE,
   ...:     weapon_affix_type=WeaponAffixType.PREFIX
   ...: )

In [4]: for _ in range(5):
   ...:     print(get_weapon_name(very_specific_seed))
   ...: 
INFERNAL STEEL KHOPESH
FLAME-LICKED BRONZE FALCHION
EMBER OBSIDIAN SCIMITAR
FLAME-LICKED SHOTEL
INFERNAL DAO

In [5]: arbitrary_seed = get_weapon_seed()

In [6]: arbitrary_seed
Out[6]: 
(<WeaponTypes.HORN: 3>,
 <WeaponAffixes.LIGHTNING: 2>,
 <WeaponAffixType.SUFFIX: 1>)

In [7]: for _ in range(5):
   ...:     print(get_weapon_name(arbitrary_seed))
   ...: 
OBSIDIAN HORN of FRACTAR
SILVER HORN of the HEAVENS' WRATH
BONE GJALLARHORN of FRACTAR
BRONZE GJALLARHORN of the EVERSTORM
HORN of FRACTAR
```