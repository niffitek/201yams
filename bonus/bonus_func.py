import sys
from math import factorial


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


def calc_bonus(dice_list):
    probString = []
    prob = 0.0
    for i in range(1, 7):
        tmp = calc_prob(2, i, dice_list)
        probString.append("Chances to get a " + str(i) + " pair: %0.2f%%" % calc_prob(2, int(i), dice_list))
        print("Chances to get a " + str(i) + " pair: %0.2f%%" % calc_prob(2, int(i), dice_list))
    print()
    for i in range(1, 7):
        tmp = calc_prob(3, i, dice_list)
        probString.append("Chances to get a " + str(i) + " three-of-a-kind: %0.2f%%" % calc_prob(3, int(i), dice_list))
        print("Chances to get a " + str(i) + " three-of-a-kind: %0.2f%%" % calc_prob(3, int(i), dice_list))
    print()
    for i in range(1, 7):
        tmp = calc_prob(4, i, dice_list)
        probString.append("Chances to get a " + str(i) + " four-of-a-kind: %0.2f%%" % calc_prob(4, int(i), dice_list))
        print("Chances to get a " + str(i) + " four-of-a-kind: %0.2f%%" % calc_prob(4, int(i), dice_list))
    print()
    for i in range(1, 7):
        tmp = calc_prob(5, i, dice_list)
        probString.append("Chances to get a " + str(i) + " yams: %0.2f%%" % calc_prob(5, int(i), dice_list))
        print("Chances to get a " + str(i) + " yams: %0.2f%%" % calc_prob(5, int(i), dice_list))
    print()
    tmp = calc_straight_prob(5, dice_list)
    probString.append("Chances to get a 5 straight: %0.2f%%" % calc_straight_prob(5, dice_list))
    print("Chances to get a 5 straight: %0.2f%%" % calc_straight_prob(5, dice_list))
    tmp = calc_straight_prob(6, dice_list)
    probString.append("Chances to get a 6 straight: %0.2f%%" % calc_straight_prob(6, dice_list))
    print("Chances to get a 6 straight: %0.2f%%" % calc_straight_prob(6, dice_list))
    print()
    for i in range(1, 7):
        for j in range(1, 7):
            if i == j:
                continue
            probString.append("Chances to get a " + str(i) + " full of " + str(j) + ": %0.2f%%" % calc_full_prob(i, j, dice_list))
            print("Chances to get a " + str(i) + " full of " + str(j) + ": %0.2f%%" % calc_full_prob(i, j, dice_list))
        print()


def takeFirst(element):
    return element[0]


def sort_bonus(dice_list):
    probString = []
    prob = 0.0
    for i in range(1, 7):
        tmp = calc_prob(2, i, dice_list)
        probString.append([tmp, "Chances to get a " + str(i) + " pair: %0.2f%%" % calc_prob(2, int(i), dice_list)])
    for i in range(1, 7):
        tmp = calc_prob(3, i, dice_list)
        probString.append([tmp, "Chances to get a " + str(i) + " three-of-a-kind: %0.2f%%" % calc_prob(3, int(i), dice_list)])
    for i in range(1, 7):
        tmp = calc_prob(4, i, dice_list)
        probString.append([tmp, "Chances to get a " + str(i) + " four-of-a-kind: %0.2f%%" % calc_prob(4, int(i), dice_list)])
    for i in range(1, 7):
        tmp = calc_prob(5, i, dice_list)
        probString.append([tmp, "Chances to get a " + str(i) + " yams: %0.2f%%" % calc_prob(5, int(i), dice_list)])
    tmp = calc_straight_prob(5, dice_list)
    probString.append([tmp, "Chances to get a 5 straight: %0.2f%%" % calc_straight_prob(5, dice_list)])
    tmp = calc_straight_prob(6, dice_list)
    probString.append([tmp, "Chances to get a 6 straight: %0.2f%%" % calc_straight_prob(6, dice_list)])
    for i in range(1, 7):
        for j in range(1, 7):
            if i == j:
                continue
            tmp = calc_full_prob(i, j, dice_list)
            probString.append([tmp, "Chances to get a " + str(i) + " full of " + str(j) + ": %0.2f%%" % calc_full_prob(i, j, dice_list)])

    probString.sort(key=takeFirst, reverse=True)
    counter = 0
    for i in probString:
        print(i[1])
        if counter % 5 == 0:
            print()
        counter += 1
