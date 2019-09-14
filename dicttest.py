#!/usr/bin/env python3
import sys

output_dict = {}

def handle_data(arg):
    a_split = arg.split(':')
    a_key = a_split[0]
    a_value = a_split[1]
    output_dict[a_key] = a_value
    

def print_data(id_num, name):
    print('ID:{} Name:{}'.format(id_num, name))

    
if __name__ == '__main__':
   
    for arg in sys.argv[1:]:
        handle_data(arg)

    for key in output_dict:
        print_data(key, output_dict[key])



  

