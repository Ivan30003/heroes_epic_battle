import argparse
from core import World
from drawer import Drawer


def parse_args():
    parser=argparse.ArgumentParser()
    parser.add_argument('--debug', action='store_true', help='whether print info in all steps')
    parser.add_argument('--drawer_mode', choices=['terminal', 'pygame'], help='choose how to draw battlefield. \
                        Choices: terminal or pygame')
    parser.add_argument('--auto_fill', action='store_true', help='whether to randomly autofill heroes deck')
    parser.add_argument('--record_game', action='store_true', help='whether to record game')
    parsed_args = parser.parse_args()
    return parsed_args


def main():
    print("launch\n------------------------------\n")
    parsed_args = parse_args()
    debug = parsed_args.debug
    record = parsed_args.record_game
    games_count = 1
    drawer_mode = parsed_args.drawer_mode

    drawer = Drawer(drawer_mode)
    world = World(drawer)

    auto_fill = parsed_args.auto_fill

    for game in range(games_count):
        world.prepare_game(auto_fill)
        world.game()


if __name__ == '__main__':
    main()
