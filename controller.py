from abc import ABC, abstractmethod
from random import randint, sample
from time import sleep


class Player(ABC):
    @abstractmethod
    def wait_for_response(self, battle_info):
        pass


class HumanPlayer(Player):
    def __init__(self):
        pass

    def wait_for_response(self, battle_info, attacks_list):
        action = input(f'action: ')
        assert len(action) == 3  # HARDCODE  like this '2 4'

        # for element in attack_list:
        #     print(f'mana need: {element[0]}, attack: {element[1].__name__}')
        # print(f'wait')

        action_list = action.split(' ')
        act_index = int(action_list[0]) - 1
        target_index = int(action_list[1]) - 1

        chosen_attack_function = attacks_list[act_index]
        # target = self.teams[abs(1 - self.team_turn)][target-1]
        # if act == len(attacks_list) + 1:
        #     current_hero.current_energy += 2
        #     break
        # elif attack_list[act - 1][0] <= current_hero.current_energy:
        #     attack_func = attack_list[act-1][1]
        #     current_hero.current_energy -= attack_list[act-1][0]
        #     attack_func(self.teams[self.team_turn], self.teams[abs(1 - self.team_turn)],
        #                 current_hero, target, self.damage_factor)  # HARDCODED for 2 teams
        #     break
        # else:
        #     pass

        # action = input()
        return chosen_attack_function, target_index


class RuleBasedPlayer(Player):
    def __init__(self):
        pass

    def wait_for_response(self, battle_info):
        action = 1
        return action


class RandomPlayer(Player):
    def __init__(self):
        pass

    def wait_for_response(self, battle_info, attacks_list):
        sleep(1)
        actions_num = len(attacks_list)
        chosen_attack_function = attacks_list[randint(0, actions_num-1)]
        
        possible_targets = []
        for hero_num, hero in enumerate(battle_info['team_two']):
            if hero.cur_health > 0:
                possible_targets.append(hero_num)

        target_index = sample(possible_targets, 1)[0]

        return chosen_attack_function, target_index
