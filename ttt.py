#!/usr/bin/env python3

class TicTacToe:
    def __init__(self):
        self.board = [[" ", " ", " "],[" ", " ", " "],[" ", " ", " "]]

    def print_board(self):
        for i, row in enumerate(self.board):
            print("|".join(row))
            if i < 2:
                print("-----")
            else:
                print("")

    def add_move(self, x, y, type):
        self.board[x-1][y-1] = type

    def has_won(self):
        # Work out whether a player has won the game

        # Check rows
        for row in self.board:
            if (row[0] == row[1] == row[2]) & (row[0] != " "):
                print("Woop, we have a winner horozontally (%s)!" % row[0])
                
        # Check columns
        if (self.board[0][0] == self.board[1][0] == self.board[2][0]) & (self.board[0][0] != " "):
            print("Woop, we have a winner vertically (%s)!" % self.board[0][0])
        if (self.board[0][1] == self.board[1][1] == self.board[2][1]) & (self.board[0][1] != " "):
            print("Woop, we have a winner vertically (%s)!" % self.board[0][1])
        if (self.board[0][2] == self.board[1][2] == self.board[2][2]) & (self.board[0][2] != " "):
            print("Woop, we have a winner vertically (%s)!" % self.board[0][2])
        # Check diagonal
        if (self.board[0][0] == self.board[1][1] == self.board[2][2]) & (self.board[0][0] != " "):
            print("Woop, we have a winner diagonally (%s)!" % self.board[0][0])
        if (self.board[2][0] == self.board[1][1] == self.board[0][2]) & (self.board[0][0] != " "):
            print("Woop, we have a winner diagonally (%s)!" % self.board[2][0])

if __name__ == "__main__":
    ttt = TicTacToe()

    ttt.add_move(1,2, "X")
    ttt.add_move(1,1, "O")
    ttt.add_move(2,3, "X")
    ttt.add_move(2,1, "O")
    ttt.add_move(3,1, "X")
    ttt.add_move(3,3, "O")
    ttt.add_move(2,2, "X")
    ttt.add_move(3,2, "O")
    ttt.add_move(1,3, "X")
    ttt.print_board()

    ttt.has_won()