#!/usr/bin/python3
'''module to print status code'''


import sys


class Magic:
    '''Class to generates instances with dict and size'''

    def __init__(self):
        '''Init method'''
        self.dic = {}
        self.sz = 0

    def i_dic(self):
        '''Init dict'''

        self.dic['200'] = 0
        self.dic['301'] = 0
        self.dic['400'] = 0
        self.dic['401'] = 0
        self.dic['403'] = 0
        self.dic['404'] = 0
        self.dic['405'] = 0
        self.dic['500'] = 0

    def add_code(self, status):
        '''add repeated num to the status code'''

        if status in self.dic:
            self.dic[status] += 1

    def prnt_info(self, sig=0, frame=0):
        '''print status code'''

        print(f'File size: {self.sz:d}')
        for idx in sorted(self.dic.keys()):
            if self.dic[idx] is not 0:
                print(f'{idx}: {self.dic[idx]:d}')


if __name__ == "__main__":
    mag = Magic()
    mag.init_dic()
    nlines = 0

    try:
        for line in sys.stdin:
            if nlines % 10 == 0 and nlines is not 0:
                mag.prnt_info()

            try:
                ls_line = [i for i in line.split(" ") if i.strip()]
                mag.add_code(ls_line[-2])
                mag.sz += int(ls_line[-1].strip("\n"))
            except Exception:
                pass
            nlines += 1
    except KeyboardInterrupt:
        mag.prnt_info()
        raise
    mag.prnt_info()
