# import pygame

class Drawer:
    def __init__(self, drawer_mode) -> None:
        self.drawer_mode = drawer_mode

    def draw_possible_attacks(self, list_of_possible_attacks):
        for index, possible_attack in enumerate(list_of_possible_attacks):
            print(f'{index+1}. {possible_attack.name}')

    def draw_print_moves(self, pairs, cur_pair_num):
        moves_str = ''
        for num, pair in enumerate(pairs):
            if num == cur_pair_num:
                moves_str = f'{moves_str} | *{pair[0]+1}, {pair[1]+1}*'
            else:
                moves_str = f'{moves_str} | {pair[0]+1}, {pair[1]+1}'
        # moves_str = ' | '.join(str(pairs))
        print(f'\n{moves_str}')

    def draw_print_teams(self, teams, team_size, team_turn, cur_hero_turn):
        # print(f'\n\n{team_turn=}\n{cur_hero_turn=}\n\n')
        assert len(teams) == 2, 'implemented only for 2 players mode'
        MAX_STR_LEN = 100
        str_situation = ''
        for i in range(team_size):
            name1 = teams[0][i].name
            name2 = teams[1][i].name
            state1 = teams[0][i].return_general_state()
            state2 = teams[1][i].return_general_state()
            num_spaces = MAX_STR_LEN - len(name1) - len(name2)
            if cur_hero_turn == i:
                if team_turn == 0:
                    cur_str_names = ('*' + name1 + ' ' * num_spaces + name2 + '\n')
                else:
                    cur_str_names = (name1 + ' ' * num_spaces + '*' + name2 + '\n')
            else:
                cur_str_names = (name1 + ' ' * num_spaces + name2 + '\n')
            state_str1 = str(state1)
            state_str2 = str(state2)
            num_spaces = MAX_STR_LEN - len(state_str1) - len(state_str2)
            cur_str_states = (state_str1 + ' ' * num_spaces + state_str2 + '\n')
            str_situation += (cur_str_names + cur_str_states)

        print(str_situation)

    def draw(self, world):
        if self.drawer_mode == 'terminal':
            team_size = len(world.teams[0])
            self.draw_print_teams(world.teams, team_size, world.current_team_turn, world.current_turn)
