#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return (None)
    else:
        largest_number = my_list[0]
        for num in my_list:
            if num > largest_number:
                largest_number = num
    return largest_number
