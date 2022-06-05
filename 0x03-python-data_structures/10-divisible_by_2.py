#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    by_2 = []
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            by_2.append(True)
        else:
            by_2.append(False)
    return by_2
