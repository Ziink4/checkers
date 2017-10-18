import checkers
import agent
import arthur
import kevin

BLACK, WHITE = 0, 1

f = open('logfile', 'w')

for i in range(10):
    print "game: " + str(i)
    B = checkers.CheckerBoard()
    cpu_1 = agent.CheckersAgent(lambda board: random_agent.move_function(board))
    cpu_2 = agent.CheckersAgent(lambda board: random_agent.move_function(board))
    current_player = B.active
    turn = 1

    f.write(str(B))
    while not B.is_over():
        if turn % 100 == 0:
            print "# of turns: " + str(turn)
        B.make_move(cpu_1.make_move(B))
        f.write(str(B))
        if B.active == current_player:
            continue
        current_player = B.active
        turn += 1
        while not B.is_over() and B.active == current_player:
            B.make_move(cpu_2.make_move(B))
            f.write(str(B))
        current_player = B.active

    f.write(str(B))

    if B.is_draw():
        print "It's a draw !"
    elif B.active == WHITE:
        print "Congrats Black, you win!"
    else:
        print "Congrats White, you win!"

    print "Game took %i turns" % turn
