#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    counts = 0

    for i in range(x):
        try:
            print("{}".format(my_list[i]), end='')
        except:
            break
        else:
            counts += 1

    print()
    return (counts)
