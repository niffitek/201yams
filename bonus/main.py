#!/usr/bin/env python3
import sys
from math import factorial

from input import check_input
from bonus.bonus_func import *


def main():
    check_input()
    dice_list = []
    for i in range(1, 6):
        dice_list.append(int(sys.argv[i]))
    comb = str(sys.argv[6])
    if comb == "-a" or comb == "--all":
        calc_bonus(dice_list)
    if comb == "-s" or comb == "--sort":
        sort_bonus(dice_list)
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
