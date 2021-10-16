# https://www.hackerrank.com/challenges/ctci-comparator-sorting/problem

from functools import cmp_to_key


def compareName(name_a, name_b):
    for index, letter in enumerate(name_a):
        if index <= len(name_b) - 1:
            if ord(letter) < ord(name_b[index]):
                return -1
            elif ord(letter) > ord(name_b[index]):
                return 1
        else:
            return 1  # a is longer than b and everything has been the same

    return -1  # if b is longer than a and everything has been the same


class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __repr__(self):
        print(f"{self.name} {self.score}")

    def comparator(a, b):
        # todo: invert the 1 and -1 since we are doing highest to lowest
        if (a.score > b.score):
            return -1
        elif (a.score < b.score):
            return 1
        else:
            return compareName(a.name, b.name)

        # if a has less characters than b, it comes lower in value
        # i.e if person with name john and johnathon, john is lower
        # i.e if person with name johnathon and john, john is lower


n = int(input())
data = []
for i in range(n):
    name, score = input().split()
    score = int(score)
    player = Player(name, score)
    data.append(player)

data = sorted(data, key=cmp_to_key(Player.comparator))
for i in data:
    print(i.name, i.score)