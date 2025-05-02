from random import randint

from attack_functions import attacks_dict

def create_hero_by_name(name):
    attack_simple = Attack(function=attacks_dict['simple_attack'])
    if name == 'handswing':
        attack_1 = Attack(function=attacks_dict['attack_headshot'], mana_cost=3)
        hero = Hero(name, 500, 100, 100, 3, [attack_simple, attack_1])
    elif name == 'smut':
        attack_1 = Attack(function=attacks_dict['massive_strike'], mana_cost=4)
        hero = Hero(name, 560, 118, 79, 4, [attack_simple, attack_1])
    else:
        raise ValueError(f'Unknown type of Hero: "{name}"')
    return hero


def create_effect(name, properties):
    pass


class Hero:
    def __init__(self, name, health, defense, attack, abilities) -> None:
        self.name = name
        self.health = health
        self.defense = defense
        self.attack = attack
        self.abilities = abilities
        self.accuracy = 100  # HARDCODE

    def init_battle(self):
        self.cur_health = self.health
        self.cur_defense = self.defense
        self.cur_attack = self.attack
        self.cur_mana = 1
        self.cur_accuracy = self.accuracy
        self.is_busy = False
        self.is_defeated = False
        self.cur_possible_attacks = 0
        self.cur_effects = []

    def return_general_state(self):
        state_dict = {'hp': self.cur_health, 'att': self.cur_attack,
                      'def': self.cur_defense, 'mp': self.cur_mana}
        return state_dict


class Attack:
    def __init__(self, function, hit_function=None, mana_cost=None, get_busy=None) -> None:
        self.function = function
        self.name = function.__name__
        if hit_function:
            self.hit_function = hit_function
        else:
            self.hit_function = self.default_hit_function
        if mana_cost:
            self.mana_cost = mana_cost
        else:
            self.mana_cost = 0
        if get_busy:
            self.get_busy = get_busy
        else:
            self.get_busy = False

    # @classmethod
    def default_hit_function(self, who, target):
        is_hit = who.accuracy >= randint(1, 100)
        return is_hit
    
    def attack(self, team_one, team_two, who, target, damage_factor):
        self.function(self.hit_function, team_one, team_two, who, target, damage_factor)
    