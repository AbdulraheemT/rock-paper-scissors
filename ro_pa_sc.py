#!/usr/bin/env python3
import random
"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""


class Player:

    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):

        self.my_move = my_move
        self.their_move = their_move


class RandomPlayer(Player):

    def move(self):
        return(random.choice(moves))


class HumanPlayer(Player):

    def move(self):

        return input("rock , paper , scissors? ").lower()


class ReflectPlayer(Player):
    def __init__(self):
        self.first_move = None

    def move(self):
        if self.first_move is None:
            self.first_move = 'rock'
            return moves[0]
        else:
            return self.their_move


class CyclePlayer(Player):
    def __init__(self):
            self.x = 0

    def move(self):
        if self.x == 0:
            self.x = self.x + 1
            return moves[0]

        elif self.x == 1:
            self.x = self.x + 1
            return moves[1]
        if self.x == 2:
            self.x = self.x - 2
            return moves[2]


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:

    def __init__(self, p1, p2,):
        self.p1 = p1
        self.p2 = p2
        self.score1 = 0
        self.score2 = 0

    def play_round(self):
        move1 = ""
        while move1 != 'rock' and move1 != 'scissors' and move1 != 'paper':
            move1 = self.p1.move()
        move2 = ""
        while move2 != 'rock' and move2 != 'scissors' and move2 != 'paper':
            move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)
        if move1 == move2:
            print("tie")
        else:
            score = beats(move1, move2)
            if score:
                print("player 1 win ")
                self.score1 = self.score1 + 1

            else:
                print("player 2 win")
                self.score2 = self.score2 + 1

    def play_game(self):
        print("Game start!")
        again = ''
        round = 1
        while again != 'quit':
            print(f"Round {round}:")
            self.play_round()
            p1s = self.score1
            p2s = self.score2
            while again != 'quit' and again != 'yes':
                again = input("do you want to play round more"
                              "enter yes or quit : ").lower()
            round = round + 1
            if again == 'yes':
                again = ""
        if p1s < p2s:
            print(f"score is player 1 = {p1s} player 2 = {p2s} \n"
                  f"player 2 win")
        elif p1s == p2s:
            print(f"score is player 1 = {p1s} player 2 = {p2s} \n"
                  f"it is tie ")
        elif p1s > p2s:
            print(f"score is player 1 = {p1s} player 2 = {p2s} \n"
                  f"player 1 win")
        print("Game over!")


if __name__ == '__main__':
    game = Game(HumanPlayer(), RandomPlayer())
    game.play_game()
