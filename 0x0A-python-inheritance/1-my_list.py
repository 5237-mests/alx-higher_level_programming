#!/usr/bin/python3
class MyList(list):
    """ Class that inherits the attributes references of class list

    Args:
        list: class list

    """

    def print_sorted(self):
        """ Method that prints the sorted list """
        my_sorted = self.copy()
        my_sorted.sort()
        print(my_sorted)
