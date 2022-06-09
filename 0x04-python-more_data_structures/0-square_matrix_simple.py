#!/usr/bin/python3
def search_replace(my_list, search, replace):
    nl = my_list.copy()
    for n in range(len(nl)):
        if nl[n] == search:
            nl[n] = replace
    return nl
