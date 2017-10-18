# Florian Brenot -- github.com/Ziink4
# =======================================
# A checkers agent based on min-max exploration,
# Alpha-beta pruning and ANN evaluation
#
# Last updated: October 18, 2017
#
# The Minmax algorithm is an optimisation algorithm, seeking to maximise
# one player's score while minimizing the other.
# Negamax is an implementaiton of the Minmax algorithm for a
# zero-sum 2-player game.
# In addition to minmax, The Negamax algorithm provides alpha-beta pruning
# a technique used to avoid exploring useless nodes in a tree
# Learn more :
# https://en.wikipedia.org/wiki/Minimax
# https://en.wikipedia.org/wiki/Negamax
# https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning
# https://en.wikipedia.org/wiki/Transposition_table

import random
import sys

# Constants
INFINITY = sys.maxsize

def score(board_old, board_new):
    if board_old.is_draw() or board_new.is_draw():
        return 0
    if board_old.is_over():
        return -INFINITY
    if board_new.is_over():
        return INFINITY

    board_score = 0 # NEURAL NETWORK OUTPUT SHOULD COME HERE

    return board_score

def negamax(board_old, board_new, depth, alpha, beta, color):
    if depth == 0 or board_new.is_over():
        return score(board_old, board_new)*color
    best_value = -INFINITY
    for move in board_new.get_moves():
        B = board_new.peek_move(move)
        if B.active != board_new.active:
            val = -negamax(board_new, B, depth - 1, -beta, -alpha, -color)
        else:
            val = negamax(board_new, B, depth, alpha, beta, color)
        best_value = max(best_value, val)
        alpha = max(alpha, val)
        if alpha >= beta:
            break
    return best_value

def move_function(board, depth=7):
    def search(move):
        B = board.peek_move(move)
        if B.active == board.active:
            return negamax(board, B, depth, -INFINITY, INFINITY, 1)
        else:
            return negamax(board, B, depth, -INFINITY, INFINITY, -1)

    return max(board.get_moves(), key=search)
    """
    # Old method used by the original author to compute AND display move scores
    pairs = zip(zip(board.get_moves(), board.get_move_strings()),
                map(search, board.get_moves()))
    print "Moves and ratings"
    for pair in pairs:
        print pair[0][1] + " with a rating of " + str(pair[1])
    print ""
    best_pair = max(pairs, key=lambda x: x[1])
    return best_pair[0][0]
    """
