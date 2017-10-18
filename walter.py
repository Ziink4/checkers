# Florian Brenot -- github.com/Ziink4
# =======================================
# A checkers agent based on min-max exploration, alpha-beta pruning and ANN evaluation
#
# Last updated: October 18, 2017
import random

def move_function(board):
    return random.choice(board.get_moves())
