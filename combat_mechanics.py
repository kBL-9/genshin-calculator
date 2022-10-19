from basestats import BaseStats
from fullstats import FullStats
from character import Character
from enemy import Enemy
from stats import Stats
from effect.effect import Effect
from constants import DamageType

# Reference
# https://library.keqingmains.com/combat-mechanics/damage/damage-formula

def clamp(n: float):
    return max(0.0, min(100.0, n))

def get_damage(
    character: Character,
    enemy: Enemy,
    skill_multiplier: float,
    effect_list = list(),
    damage_type: DamageType = DamageType.PHYSICAL
):
    # apply all effects here first
    for effect in effect_list:
        break
    
    # get damage
    char_stats = character.base_stats
    enemy_stats = enemy.stats
    char_level = character.level + 100
    enemy_level = enemy.level + 100
    def_reduce = enemy_stats.get_def_reduction()
    def_ignore = enemy_stats.get_def_ignore()
    base_resistence = enemy_stats.get_resist_bonus(damage_type)
    resistence_shred = enemy_stats.get_resist_reduction(damage_type)
    
    
    current_damage = char_stats.get_base_atk() * skill_multiplier                   # basic atk
    if "flat_dmg" in char_stats: current_damage += char_stats.get_flat_damage()     # flat dmg from various sources
    current_damage *= (1 + char_stats.get_damage_bonus(damage_type) - 0)            # MISSING: damange reduction here
    current_damage *= (1 + clamp(char_stats.get_cr()) * char_stats.get_cd())        # avg crit dmg
    current_damage *= char_level / (char_level + enemy_level * (1 - def_reduce) * (1 - def_ignore))
    current_damage *= 
    
