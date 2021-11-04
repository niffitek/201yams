#!/usr/bin/env python3
import sys
from math import factorial

from input import check_input


def binomial(n, k):
    return factorial(n) / (factorial(k) * (factorial(n - k))) * pow(1 / 6, k) * pow(5 / 6, n - k)


def calc_prob(expected, number, dice_list):
    prob = 0.0
    dice_count = dice_list.count(number)
    if dice_count >= expected:
        prob = 1.0
    else:
        for i in range(expected - dice_count, 5 - dice_count + 1):
            prob += binomial(5 - dice_count, i)
    prob *= 100.0
    return prob


def calc_straight_prob(number, dice_list):
    prob = 0.0
    count = 0
    for i in range(0, 5):
        if dice_list.count(number) >= 1:
            count += 1
        number -= 1
    if count == 5:
        prob = 1.0
    else:
        prob = (1.0 / 6.0**(5.0 - count)) * factorial(5.0 - count)
    if count == 0:
        prob *= 2
    return prob * 100


def calc_full_prob(number1, number2, dice_list):
    prob = 1.0
    count1 = dice_list.count(number1)
    count2 = dice_list.count(number2)
    if number1 == number2:
        exit(84)
    if count1 > 3:
        count1 = 3
    if count2 > 2:
        count2 = 2
    fullhouse = float(factorial(5 - count1 - count2) / (factorial(3 - count1) * factorial(2 - count2)))
    return (fullhouse / pow(6, 5 - count1 - count2)) * 100.0


def main():
    check_input()
    dice_list = []
    for i in range(1, 6):
        dice_list.append(int(sys.argv[i]))
    comb = str(sys.argv[6])
    if comb.startswith("pair"):
        print("Chances to get a " + comb[5] + " pair: %0.2f%%" % calc_prob(2, int(comb[5]), dice_list))
    if comb.startswith("three"):
        print("Chances to get a " + comb[6] + " three-of-a-kind: %0.2f%%" % calc_prob(3, int(comb[6]), dice_list))
    if comb.startswith("four"):
        print("Chances to get a " + comb[5] + " four-of-a-kind: %0.2f%%" % calc_prob(4, int(comb[5]), dice_list))
    if comb.startswith("yams"):
        print("Chances to get a " + comb[5] + " yams: %0.2f%%" % calc_prob(5, int(comb[5]), dice_list))
    if comb.startswith("straight"):
        print("Chances to get a " + comb[9] + " straight: %0.2f%%" % calc_straight_prob(int(comb[9]), dice_list))
    if comb.startswith("full"):
        print("Chances to get a " + comb[5] + " full of " + comb[7] + ": %0.2f%%" % calc_full_prob(int(comb[5]), int(comb[7]), dice_list))
