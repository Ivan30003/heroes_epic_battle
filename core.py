from random import randint, sample, choices
from heroes import create_hero_by_name
from controller import HumanPlayer, RandomPlayer

class World:
    def __init__(self, drawer, debug=None, damage_factor=None) -> None:
        self.teams = [[],[]]
        self.current_turn = 0
        self.current_team_turn = 0
        self.players = []
        self.drawer = drawer
        if damage_factor:
            self.damage_factor = damage_factor
        else:
            self.damage_factor = 65

    def auto_fill_all(self):
        names_1 = ['handswing', 'smut', 'handswing']
        names_2 = ['smut', 'handswing', 'smut']
        for name in names_1:
            self.teams[0].append(create_hero_by_name(name))
        for name in names_2:
            self.teams[1].append(create_hero_by_name(name))

        player_1 = HumanPlayer()  # HARDCODE
        player_2 = RandomPlayer()  # HARDCODE
        self.players.append(player_1)
        self.players.append(player_2)

    def prepare_game(self, auto_fill):
        if auto_fill:
            self.auto_fill_all()
        else:
            pass
            # self.choose_game()
            # self.choose_heroes()

        for team in self.teams:
            for hero in team:
                hero.init_battle()

        # self.total_teams_length = sum([len(team) for team in self.teams])

    def get_team_hp(self, team):
        total_health = 0
        for hero in team:
            total_health += hero.cur_health

        return total_health

    def get_possible_heroes_to_turn(self):
        possible_heroes_to_turn = []
        for team_number, team in enumerate(self.teams):
            for hero_number, hero in enumerate(team):
                if hero.cur_health > 0:
                    possible_heroes_to_turn.append((team_number, hero_number))
                
        return possible_heroes_to_turn

    def get_possible_attacks_list(self, cur_hero):
        possible_attacks_list = []
        for attack in cur_hero.attacks:
            if attack.mana_cost <= cur_hero.cur_mana:
                possible_attacks_list.append(attack)

        return possible_attacks_list

    def turn(self, pair):
        cur_hero = self.teams[pair[0]][pair[1]]
        team_one = self.teams[self.current_team_turn]
        team_two = self.teams[1 - self.current_team_turn]
        battle_info = {'team_two': team_two}  # TODO make battle info

        list_of_possible_attacks = self.get_possible_attacks_list(cur_hero)
        self.drawer.draw_possible_attacks(list_of_possible_attacks)

        chosen_attack, target_index = self.players[self.current_team_turn].wait_for_response(battle_info ,list_of_possible_attacks)
        cur_hero.cur_mana -= chosen_attack.mana_cost

        target = self.teams[1 - pair[0]][target_index]
        chosen_attack.attack(team_one, team_two, cur_hero, target, self.damage_factor)

    def game(self):
        team_1_hp = self.get_team_hp(self.teams[0])
        team_2_hp = self.get_team_hp(self.teams[1])
        possible_heroes_to_turn = self.get_possible_heroes_to_turn()
        num_of_heroes_to_turn = randint(5,7) # HARDCODE  round(0.7 * self.total_teams_length)
        heroes_to_turn = choices(population=possible_heroes_to_turn, k=num_of_heroes_to_turn)
        # self.drawer.draw_print_teams(self.teams, len(self.teams[0]), self.current_team_turn, self.current_turn)
        while team_1_hp > 0 and team_2_hp > 0:
            # One round
            for pair_num, pair in enumerate(heroes_to_turn):
                self.current_team_turn = pair[0]
                self.current_turn = pair[1]
                self.drawer.draw_print_teams(self.teams, len(self.teams[0]), self.current_team_turn, self.current_turn)
                self.drawer.draw_print_moves(heroes_to_turn, pair_num)
                self.turn(pair)
                # print(f'\n\n{self.current_team_turn=}\n{self.current_turn=}\n\n')

            for team in self.teams:
                for hero in team:
                    if hero.max_mana > hero.cur_mana:
                        hero.cur_mana += 1

            possible_heroes_to_turn = self.get_possible_heroes_to_turn()
            num_of_heroes_to_turn = randint(5,7) # HARDCODE  round(0.7 * self.total_teams_length)
            heroes_to_turn = choices(population=possible_heroes_to_turn, k=num_of_heroes_to_turn)
