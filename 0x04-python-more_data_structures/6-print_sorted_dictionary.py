#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    orderd_list = list(a_dictionary.keys())
    orderd_list.sort()
    for i in orderd_list:
        print("{}: {}".format(i, a_dictionary.get(i)))
