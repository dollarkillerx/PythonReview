# -*- coding: utf-8 -*- 
# @Time : 2019-11-02 17:55 
# @Author : DollarKillerx
# @Description :

import sys

if __name__ == '__main__':
    print('the command line arguments are:')
    for i in sys.argv:
        print(i)
    print('\n\nThe PYTHONPATH is',sys.path,'\m')