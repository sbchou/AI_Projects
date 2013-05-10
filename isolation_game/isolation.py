"""
Sophie Chou
sbc2125
sbc2125_player.py

AI HW 3

USAGE: python sbc2125_player.py 
then read instructions in game

"""
from copy import deepcopy
from ast import literal_eval
import time

class Game:

    def __init__(self):
        "Init params: game board, moves stack, winner"
        self.board =  [ ['-' for i in range(8) ] for j in range(8)]
        self.board[0][0] = 'x'
        self.board[7][7] = 'o'
        self.winner = None
        self.lastmoves = []

    def print_board(self):
        "Pretty print of nested lists."
        print "  1 2 3 4 5 6 7 8"
        for i in range(len(game.board)):
            string = str(i+1)
            row = game.board[i]
            for item in row:
                string += " " + item
            print string

    def get_posn(self, player):
        "get posn of player on board."

        posn = [(i, row.index(player)) for i, row in enumerate(self.board) 
                if player in row]

        if posn:
            return posn[0]
        else:
            print 'not in list'
            print player
            self.print_board


    # actions == get_free_positions
    def actions(self, player):
        "generate all possible next moves, given current self.board. return in form of list of tuple posns (row, col)."
        actions = []
        row, col = self.get_posn(player)

        #check N (-, *)
        x, y = row-1, col
        while x in range(8) and y in range(8) and self.board[x][y] == '-':
            actions.append((x,y))
            x -= 1

        #check S (+, *)
        x, y = row+1, col
        while x in range(8) and y in range(8) and self.board[x][y] == '-':
            actions.append((x,y))
            x += 1

        #check E (*, +)
        x, y = row, col+1
        while x in range(8) and y in range(8) and self.board[x][y] == '-':
            actions.append((x,y))
            y += 1

        #check W (*, -)
        x, y = row, col-1
        while x in range(8) and y in range(8) and self.board[x][y] == '-':
            actions.append((x,y))
            y -=1

        #check NE (-, +)
        x, y = row-1, col+1
        while x in range(8) and y in range(8) and self.board[x][y] == '-':
            actions.append((x,y))
            x-=1
            y+=1

        #check NW (-, -)
        x, y = row-1, col-1
        while x in range(8) and y in range(8) and self.board[x][y] == '-':
            actions.append((x,y))
            x-=1
            y-=1

        #check SE (+, +)
        x, y = row+1, col+1
        while x in range(8) and y in range(8) and self.board[x][y] == '-':
            actions.append((x,y))
            x+=1
            y+=1

        #check SW (+, -)
        x, y = row+1, col-1
        while x in range(8) and y in range(8) and self.board[x][y] == '-':
            actions.append((x,y))
            x+=1
            y-=1

        return actions

    def mark(self, player, action):
        "apply the action to the current self.board and return new self.board"

        old_row, old_col = self.get_posn(player)
        self.board[old_row][old_col] = '*' 
        new_row, new_col = action
        self.board[new_row][new_col] = player

        self.lastmoves.append(((old_row, old_col), (new_row, new_col), player))

        #print 'LAST MOVES', self.lastmoves

        return self.board #MUTABLE WATCH OUT

    def revert_last_move(self):
        "Reset the last move"
        #print "WE'RE REVERTING THAT SHIT"

        posn, action, player = self.lastmoves.pop()

        x1, y1 = posn
        x2, y2 = action

        self.board[x1][y1] = player
        self.board[x2][y2] = '-'

        self.winner = None

    # === is_gameover
    def is_terminal(self):
        "return true if game over for *either* x or o, false otherwise. Note that we don't need to know any other params! NOTE: Endgame in this implementation is *complete* isolation of a player. May be redundant"

        x_moves = len(self.actions('x'))
        o_moves = len(self.actions('o'))

        if x_moves == 0:
            self.winner = 'o'
            #print "TERMINAL"
            return True

        elif o_moves == 0:
            self.winner = 'x'
            return True

        elif o_moves == 0 and x_moves == 0:
            self.winner = '-'
            #print "TERMINAL"
            return True

        else:
            return False

    
    def play(self,player1,player2):
        "Execute the game play with players"
        self.x = None
        self.o = None

        if player1.marker == 'x':
            self.x = player1
            self.o = player2

        else:
            self.x = player2
            self.o = player1

        print
        print "Welcome to Isolation!"
        time = int(raw_input("Enter computational time restriction (seconds): "))
        print "Here is the starting board."
        print
        self.print_board()

        while not self.is_terminal():

            #x goes first
            print
            print "x's turn"
            
            if self.x.type == 'AI':
                self.x.move(self, time)
            else:
                self.x.move(self)

            self.print_board()

            if self.is_terminal():
                if self.winner == '-':
                    print "\nGame over with Draw"
                else:
                    print "\nWinner : %s" %self.winner
                
                return

            #then o goes
            print
            print "o's turn"
            
            if self.o.type == 'AI':
                self.o.move(self, time)
            else:
                self.o.move(self)
            
            self.print_board()

            if self.is_terminal():
                if self.winner == '-':
                    print "\nGame over with Draw"
                else:
                    print "\nWinner : %s" %self.winner
                
                return

class Human:
    "Class for opponent player"
    def __init__(self, marker):
        self.marker = marker
        self.type = 'Human'

        if self.marker == "x":
            self.opp_marker = "o"
        else:
            self.opp_marker = "x"


    def move(self, game):

        undo = False
        while True:
            m = raw_input("Enter your move, in form (row col).\nEnter UNDO to undo the computer's last move: ")
            
            if m.upper() == "UNDO":
                undo = True
                if game.lastmoves:
                    game.revert_last_move()
                else:
                    print "No moves to undo."
                print
                break

            else:
                m = m.replace(" ", ",")
                print

            try:
                m = literal_eval(m)
                m = (m[0]-1, m[1]-1)
            except:
                m = -1
            if m not in game.actions(self.marker):
                print "INVALID MOVE"
            else:
                break
        if not undo:
            game.mark(self.marker, m)
       
class AI:
    "Class for AI-powered Player"
    def __init__(self, marker):
        self.marker = marker
        self.type = 'AI'

        if self.marker == "x":
            self.opp_marker = "o"
        else:
            self.opp_marker = "x"

    def move(self, game, max_t):
        undo = raw_input("Do you want to undo your last move? Enter Y/N: ")
        if undo.upper() == "Y":
            if game.lastmoves:
                game.revert_last_move()
            else:
                print "No moves to undo."
            print

        else:
            print self.marker + " is thinking..."
           
            if max_t < 20:
                depth = 1
            elif max_t >= 20 and max_t < 120:
                depth = 3
            else:
                depth = 5

            start = time.time()
            move_position, score = self.maximized_move(game, depth, -float('inf'), float('inf'))
            game.mark(self.marker, move_position)
            stop = (time.time() - start)
            #print "That took " + str(stop) + " seconds!"
            print

    def maximized_move(self, game, depth, alpha, beta):
        "MINIMAX ALGORITHM, depth-limited. YOU are max"
        
        bestmove = None
 
        for m in game.actions(self.marker):
            game.mark(self.marker, m)

            #if leaf or terminal return utility
            if depth < 0 or game.is_terminal():
                score = self.get_score(game)
           
            else:
                #get to the leaf nodes!
                move_position, score = self.minimized_move(game, depth-1, alpha, beta)
            
            #go one back to parent, to get scores of children
            game.revert_last_move()

            if score > alpha: #we have found a better best score
                alpha = score 
                bestmove = m

            if alpha >= beta: #cut off
                return m, alpha

        return bestmove, alpha


    def minimized_move(self, game, depth, alpha, beta):
        "Find the min move (depth-limited). OPP is MIN"

        bestmove = None
   
        for m in game.actions(self.opp_marker):

            game.mark(self.opp_marker, m)

            #if leaf or terminal return utility
            if depth < 0 or game.is_terminal():
                score = self.get_score(game)

            else:
                #get to the leaf nodes!
                move_position, score = self.maximized_move(game, depth-1, alpha, beta)

            #go one back to parent, to get scores of children
            game.revert_last_move()

            if score < beta: #found a new min upper bound, opponent has new worst move for you
                beta = score
                bestmove = m

            if alpha >= beta: #cut off
                return m, beta

        return bestmove, beta


    def get_score(self, game):
        "Evaluation Function"
        if game.is_terminal():
            if game.winner == self.marker:
                return float('inf') #won
            elif game.winner == self.opp_marker:
                return -float('inf')
            else:
                return 0 #draw
        else: #nonterminal
            return len(game.actions(self.marker))
            

if __name__ == '__main__':

    game=Game()  

    print
    
    while True:
        marker = raw_input("Enter your marker, x or o: ").lower()
        if marker == 'x' or marker == 'o':
            break
        else:
            print "Try again."

    player1 = Human(marker)
    player2 = AI(player1.opp_marker)

    game.play(player1, player2)




