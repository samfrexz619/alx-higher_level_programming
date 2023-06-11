#!/usr/bin/python3
'''module that inherits the attr ref '''


class MyList(list):
    '''class that inherits the attr ref of a class

    Arg:
        list: class list

    '''


    def print_sorted(self):
        '''method to print sorted list'''
        ls_sorted = self.copy()
        ls_sorted.sort()
        print(ls_sorted)
