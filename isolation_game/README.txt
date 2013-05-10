ISOLATION BOARDGAME
+++++++++++++++++++

This is a simple command-line implementation of Isolation, a rather boring boardgame.
This was a submission for Columbia's Artificial Intelligence COMSW 4701 class with Professor Sal Stolfo.
Please *DO NOT* use this code for your own homework: you can do better anyways.

This demonstrates basic Game Theory concepts using the Minimax Game-Playing algorithm with Alpha-Beta pruning. (More info here: http://en.wikipedia.org/wiki/Minimax)

Extra parameters for class purposes include: computational time limit, undo capacity

THE RULES OF THE GAME:
++++++++++++++++++++++

The game has two players: x and o. The players alternate turns, with player x moving first at the beginning of each game.

Player x starts at position (1,1) while o starts at (8,8).

Each turn, a player can move like a queen in chess (in any of the eight directions) as long as her path does not cross a square already filled in or occupied. After moving, the space vacated by the player is designated as filled and cannot be moved to again. Notice that only the space that was occupied is filled, not the entire path.

The game ends when one player can no longer move, leaving the other player as the winner.

The coordinate (1 1) indicates the top left hand side of the board.

The board is specified as a list of rows. Each row is a list of entries:

      - is an empty square
      * is a filled in square
      x is the current position of the x player
      o is the current position of the o player
The board will always be 8 by 8.


Evaluation Function
    The evaluation function that I have designed, called "get_score", is very simple. It returns -infinity for a loss, +infinity for a win, and otherwise simply the number of valid actions for the current player. Therefore, the more number of moves the player can take, the higher value this move has. Although simple, this provides a pretty good heuristic to approximate the "goodness" of a particular board, *especially* if we can look several plys ahead, since the goal of the game is to avoid steps that will lead to a trap-- or zero moves, by choosing spots with lots of move options.

    Furthermore, using a very simple evaluation function increases the speed to calculate each ply-- leading to a more accurate prediction by searching deeper in the game tree. It focuses more on quickness rather than preciseness.

No extensions implemented, aside from rollback and time parameters added by TA's instructions.
