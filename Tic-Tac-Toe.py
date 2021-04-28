"""
A program to play Tic-Tac-Toe

Author: KG
"""
import random


class TicTacToe:
    print('Welcome to the tic-tac-toe game!\nPlayer X starts the game.\nEnter: start user/level user/level '
          '(level: easy, medium, hard. To play 3 parameters are needed!) or "exit" or "help"\nGood luck!')

    def __init__(self):
        """
           Defining initial "self" arguments.
        """
        TicTacToe.menu(self)
        self.matrix = [[' ' for i in range(3)] for j in range(3)]
        self.player_sign = 'X'
        self.opponent = 'O'
        self.result = TicTacToe.game_win(self)

    def __str__(self):
        """
        Prints the returned game grid - complete with moves.
        """
        print(TicTacToe.grid_printing(self))
        TicTacToe.change_sign(self)
        TicTacToe.player_move(self)

    def matrix_reset(self):
        """
        Clears data from matrices and variables for a new gameplay.

        sets:
            empty matrix 3x3 - self.matrix
            prints a blank matrix - TicTacToe.grid_printing(self)
        next:
            creates an empty matrix diagram with frames: TicTacToe.grid_printing(self)
        """
        self.player_sign = 'X'
        self.opponent = 'O'
        self.matrix = [[' ' for i in range(3)] for j in range(3)]
        self.result = TicTacToe.game_win(self)
        TicTacToe.grid_printing(self)

    def player(self):
        """
        Determines whether players 1 and 2 are computer or a player.
        """
        if self.player1 == "user":
            self.game_type1 = 'player'
        else:
            self.game_type1 = 'computer'
        if self.player2 == "user":
            self.game_type2 = 'player'
        else:
            self.game_type2 = 'computer'

    def player_move(self):
        """
        Defines the alternating movement of the players: X and O.

        next:
            if the player is a computer and what difficulty of the opponent:
                    - TicTacToe.ai_game_easy(self)
                    - TicTacToe.ai_game_medium(self)
                    - TicTacToe.ai_game_hard(self)
            if the player is a user: TicTacToe.player_game(self)
        """
        while True:
            TicTacToe.is_game_finished(self)
            if self.player_sign == 'X':
                if self.game_type1 == 'player':
                    TicTacToe.player_start(self)
                if self.game_type1 == 'computer':
                    if self.player1 == 'easy':
                        TicTacToe.ai_game_easy(self)
                    elif self.player1 == 'medium':
                        TicTacToe.ai_game_medium(self)
                    else:
                        TicTacToe.ai_game_hard(self)
            if self.player_sign == 'O':
                if self.game_type2 == 'player':
                    TicTacToe.player_start(self)
                if self.game_type2 == 'computer':
                    if self.player2 == 'easy':
                        TicTacToe.ai_game_easy(self)
                    elif self.player2 == 'medium':
                        TicTacToe.ai_game_medium(self)
                    else:
                        TicTacToe.ai_game_hard(self)

    def is_game_finished(self):
        """
        Checks if one of the parties is win, or draw is.

        returns:
            prints game status - win X, O, or Draw.
        next:
            sends to the main menu:: TicTacToe.menu(self)
        """
        self.result = TicTacToe.game_win(self)
        if self.result == 'X':
            print(f'X wins\n')
            TicTacToe.menu(self)
        elif self.result == 'O':
            print(f'O wins\n')
            TicTacToe.menu(self)
        elif self.result == ' ':
            print('Draw\n')
            TicTacToe.menu(self)

    def game_win(self):
        """
        Called after each move - checks if any player has 3 of the same symbols in a column, row or diagonal.

        returns:
            game win result: self.matrix[j][i] sign
        """
        # Vertical win
        for i in range(0, 3):
            if (self.matrix[0][i] != ' ' and
                    self.matrix[0][i] == self.matrix[1][i] and
                    self.matrix[1][i] == self.matrix[2][i]):
                return self.matrix[0][i]
        # Horizontal win
        for i in range(0, 3):
            if (self.matrix[i] == ['X', 'X', 'X']):
                return 'X'
            elif (self.matrix[i] == ['O', 'O', 'O']):
                return 'O'
        # Main diagonal win
        if (self.matrix[0][0] != ' ' and
                self.matrix[0][0] == self.matrix[1][1] and
                self.matrix[0][0] == self.matrix[2][2]):
            return self.matrix[0][0]
        # Second diagonal win
        if (self.matrix[0][2] != ' ' and
                self.matrix[0][2] == self.matrix[1][1] and
                self.matrix[0][2] == self.matrix[2][0]):
            return self.matrix[0][2]

        for i in range(0, 3):  # Is whole board full?
            for j in range(0, 3):
                if (self.matrix[i][j] == ' '):  # There's an empty field, we continue the game
                    return None
        return ' '

    def ai_game_easy(self):
        """
        Easy computer game level randomly selects an empty cell in the matrix.

        returns:
            matrix with printed AI movement: print(TicTacToe.grid_printing(self))
            False - to end the WHILE loop to validate cell selection by the AI
        next:
            if randomly selected cell is full - repeat the draw from the AI matrix
            after printing the matrix with the approved move: print(TicTacToe.grid_printing(self))
            change of the X / O sign: TicTacToe.change_sign(self)
            next player's move: TicTacToe.player_move(self)
        """
        while True:
            y = random.randrange(3)
            x = random.randrange(3)
            cell_status = self.matrix[x][y]
            if cell_status == 'X' or cell_status == 'O':  # double check that the drawn cell is free
                TicTacToe.ai_game_easy(self)
            else:
                print(f'{self.player_sign} making move - level "easy"')
                self.matrix[x][y] = self.player_sign
                TicTacToe.__str__(self)
                return False

    def ai_game_medium(self):
        """
        Medium game level - AI is blocking moves and looking for a possible win.

        differences in level:
            - if it already has two in a row and can win with one further move, it does so
            - if its opponent can win with one move, it plays the move necessary to block this
            - otherwise, it makes a random move
        returns:
            matrix with printed AI movement: print(TicTacToe.grid_printing(self))
            False - to end the WHILE loop to validate cell selection by the AI
        next:
            if randomly selected cell is full - repeat the draw from the AI matrix
            after printing the matrix with the approved move: print(TicTacToe.grid_printing(self))
            change of the X / O sign: TicTacToe.change_sign(self)
            next player's move: TicTacToe.player_move(self)
        """
        while True:
            counter = 0
            # horizontal rows - check if 2 filled by AI and 3 is available:
            for i in range(3):
                if (self.matrix[i].count(self.player_sign) == 2) and (' ' in self.matrix[i]):
                    free_cell = self.matrix[i].index(' ')
                    self.matrix[i][free_cell] = self.player_sign
                    counter += 1
                    print(f'{self.player_sign} making move - level "medium"')
                    TicTacToe.__str__(self)
            # horizontal rows - check if 2 filled by opponent and 3 is available:
            for i in range(3):
                if (self.matrix[i].count(self.opponent) == 2) and (' ' in self.matrix[i]):
                    saving_cell = self.matrix[i].index(' ')
                    self.matrix[i][saving_cell] = self.player_sign
                    counter += 1
                    print(f'{self.player_sign} making move - level "medium"')
                    TicTacToe.__str__(self)
            # vertical columns - check if 2 filled by opponent and 3 is available:
            for i in range(3):
                if [self.matrix[0][i], self.matrix[1][i], self.matrix[2][i]].count(self.opponent) == 2 \
                        and (' ' in [self.matrix[0][i], self.matrix[1][i], self.matrix[2][i]]):
                    for cell in [self.matrix[0][i], self.matrix[1][i], self.matrix[2][i]]:
                        if cell == ' ':
                            saving_cell = [self.matrix[0][i], self.matrix[1][i], self.matrix[2][i]].index(cell)
                            self.matrix[saving_cell][i] = self.player_sign
                            counter += 1
                            print(f'{self.player_sign} making move - level "medium"')
                            TicTacToe.__str__(self)
            # diagonals - check if 2 filled by opponent and 3 is available:
            for i in range(3):
                if (self.matrix[i][i] == ' ') and (self.matrix[i][i] in
                                                   [self.matrix[2][0], self.matrix[1][1], self.matrix[0][2]]) and \
                        ([self.matrix[2][0], self.matrix[1][1], self.matrix[0][2]].count(self.opponent) == 2):
                    for j in range(3):
                        if (self.matrix[j][-(j + 1)] == ' ') and \
                                (self.matrix[j][-(j + 1)] in [self.matrix[2][0], self.matrix[1][1], self.matrix[0][2]]):
                            self.matrix[j][-(j + 1)] = self.player_sign
                            counter += 1
                            print(f'{self.player_sign} making move - level "medium"')
                            TicTacToe.__str__(self)
            for i in range(3):
                if (self.matrix[i][i] == ' ') and (self.matrix[i][i] in
                                                   [self.matrix[0][0], self.matrix[1][1], self.matrix[2][2]]) and \
                        ([self.matrix[0][0], self.matrix[1][1], self.matrix[2][2]].count(self.opponent) == 2):
                    for j in range(3):
                        if (self.matrix[j][-(j + 1)] == ' ') and\
                                (self.matrix[j][-(j + 1)] in [self.matrix[0][0], self.matrix[1][1], self.matrix[2][2]]):
                            self.matrix[j][-(j + 1)] = self.player_sign
                            counter += 1
                            print(f'{self.player_sign} making move - level "medium"')
                            TicTacToe.__str__(self)
            if counter == 0:
                y = random.randrange(3)
                x = random.randrange(3)
                cell_status = self.matrix[x][y]
                if cell_status == 'X' or cell_status == 'O':  # double check that the drawn cell is free
                    TicTacToe.ai_game_medium(self)
                self.matrix[x][y] = self.player_sign
                print(f'{self.player_sign} making move - level "medium"')
                TicTacToe.__str__(self)
            return False

    def ai_game_hard(self):
        """
        Hard level uses the minmax algorithm.

        description:
        A Minimax algorithm can be best defined as a recursive function that does the following things:
            - return a value if a terminal state is found (+1, 0, -1)
            - go through available spots on the board
            - call the minimax function on each available spot (recursion)
            - evaluate returning values from function calls
            - and return the best value
        """
        if self.player_sign == 'X':
            (m, px, py) = self.min()
            self.matrix[px][py] = 'X'
            print(f'{self.player_sign} making move - level "hard')
            TicTacToe.__str__(self)
        if self.player_sign == 'O':
            (m, px, py) = self.max()
            self.matrix[px][py] = 'O'
            print(f'{self.player_sign} making move - level "hard"')
            TicTacToe.__str__(self)

    def max(self):
        """
        Player 'O' is max.

        possible values for maxv are:
            -1 - loss
            0  - draw
            1  - win
        """
        maxv = -2  # We're initially setting it to -2 as worse than the worst case.
        px = None
        py = None
        result = TicTacToe.game_win(self)

        if result == 'X':
            return (-1, 0, 0)
        elif result == 'O':
            return (1, 0, 0)
        elif result == ' ':
            return (0, 0, 0)

        for i in range(0, 3):
            for j in range(0, 3):
                if self.matrix[i][j] == ' ':  # On the empty field player 'O' makes a move and calls Min
                    self.matrix[i][j] = 'O'
                    (m, min_i, min_j) = self.min()
                    if m > maxv:  # Fixing the maxv value if needed
                        maxv = m
                        px = i
                        py = j
                    self.matrix[i][j] = ' '  # Setting back the field to empty
        return (maxv, px, py)


    def min(self):
        """
        Player 'X' is min (also human).

        possible values for minv are:
            -1 - win
            0  - draw
            1  - loss
        """
        minv = 2  # We're initially setting it to 2 as worse than the worst case:
        qx = None
        qy = None
        result = TicTacToe.game_win(self)

        if result == 'X':
            return (-1, 0, 0)
        elif result == 'O':
            return (1, 0, 0)
        elif result == ' ':
            return (0, 0, 0)

        for i in range(0, 3):
            for j in range(0, 3):
                if self.matrix[i][j] == ' ':
                    self.matrix[i][j] = 'X'
                    (m, max_i, max_j) = self.max()
                    if m < minv:
                        minv = m
                        qx = i
                        qy = j
                    self.matrix[i][j] = ' '
        return (minv, qx, qy)


    def player_start(self):
        """
        Analyzes the coordinates entered by the player - whether they are correct - and introduces them to the matrix.

        returns:
            matrix with printed player movement: print(TicTacToe.grid_printing(self))
            False - to end the WHILE loop to validate the coordinates entered by the user
        next:
            if the coordinates are incorrectly entered - repeat entered
            after printing the matrix with the approved move: print(TicTacToe.grid_printing(self))
            change of the X / O sign: TicTacToe.change_sign(self)
            next player's move: TicTacToe.player_move(self)
        """
        while True:
            gamer_move = [x for x in input(f'Enter the coordinates: ')]
            delete = [' ', ',', ';']
            for x in gamer_move:
                if x in delete:  # if ' ' ',' ';' between the coordinates, delete it
                    gamer_move.remove(x)
            for x in gamer_move:
                if x.isalpha() is True:  # if letter - False and repeat input
                    print('You should enter numbers!')
                    return False
                elif 1 > int(x) or 3 < int(x):  # if coordinates are different than range 1-3  - False and repeat input
                    print('Coordinates should be from 1 to 3!')
                    return False
            x = int(gamer_move[0]) - 1
            y = int(gamer_move[1]) - 1
            if (self.matrix[x][y] == 'X') or (self.matrix[x][y] == 'O'):
                print('This cell is occupied! Choose another one!')
            else:
                self.matrix[x][y] = self.player_sign
                TicTacToe.__str__(self)
                return False

    def change_sign(self):
        """
        After making a move it changes the X / O sign between players.
        """
        TicTacToe.is_game_finished(self)
        if self.player_sign == 'X':
            self.player_sign = 'O'
            self.opponent = 'X'
        elif self.player_sign == 'O':
            self.player_sign = 'X'
            self.opponent = 'O'

    def grid_printing(self):
        """
        Prints the matrix - empty at the beginning of the game and after each move made.

        returns:
            matrix (empty or filled) to be printed - with a frame
        """
        grid = "---------\n"
        for i in range(3):
            grid += "| " + " ".join(self.matrix[i]) + " |\n"
        grid += "---------"
        return grid

    def menu(self):
        """
        Checks the correctness of the entered player's choices and the type of game.

        next:
            if wrong data - asks you to enter again: TicTacToe.enter_data(self)
            resetting data to the game (matrix, variables): TicTacToe.matrix_reset(self)
            game matrix printing: print(TicTacToe.grid_printing(self))
            refers to defining the type of players (AI or user): TicTacToe.player(self)
        """
        game = tuple(input('Input command: ').split())
        difficulty_levels = ['easy', 'medium', 'hard', 'user']
        if (len(game[1:]) == 2) and ('exit' not in game[1:]):
            if (game[1:][1] in difficulty_levels) and (game[1:][0] in difficulty_levels):
                print('\nHello!')
                TicTacToe.matrix_reset(self)
                self.player1 = game[1:][0]
                self.player2 = game[1:][1]
                print(TicTacToe.grid_printing(self))
                TicTacToe.player(self)
                TicTacToe.player_move(self)
            else:
                print('Bad parameters!')
                TicTacToe.menu(self)
        elif game[0] == 'exit':
            print('Bye!')
            exit()
        elif game[0] == 'help':
            help(TicTacToe)
            TicTacToe.menu(self)
        else:
            print('Bad parameters!')
            TicTacToe.menu(self)

game = TicTacToe()