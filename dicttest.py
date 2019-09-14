#!/usr/bin/env python3
import sys

a_dict = {}
a_list = sys.argv[1:]

for i in a_list:
    a_split = i.split(':')
    a_key = a_split[0]
    a_value = a_split[1]
    a_dict[a_key]=a_value

for key,value in a_dict.items():
    print('ID:{}, Name:{}'.format(key, value))

  
