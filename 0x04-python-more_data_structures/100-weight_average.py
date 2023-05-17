#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return (0)

    av_num = 0
    n = 0

    for idx in my_list:
        av_num += idx[0] * idx[1]
        n += idx[1]

    return (av_num / n)
