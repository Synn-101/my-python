from board import Board
from RandomPlayer import RandomPlayer
from HumanPlayer import HumanPlayer
from AIPlayer import AIPlayer
from game import Game

if __name__ == '__main__':
    black_player=HumanPlayer("X")
    white_player=AIPlayer("O")
    game=Game(black_player, white_player)
    game.run()
