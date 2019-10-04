 # -*- coding: utf-8 -*-

import re 
from datetime import datetime
from collections import Counter

def open_parser(filename):
    with open(filename) as logfile:
        
        pattern = (r''
                   r'(\d+.\d+.\d+.\d+)\s-\s-\s'  
                   r'\[(.+)\]\s'  
                   r'"GET\s(.+)\s\w+/.+"\s'  
                   r'(\d+)\s'  
                   r'(\d+)\s'  
                   r'"(.+)"\s'  
                   r'"(.+)"'  
                   )
        parsers = re.findall(pattern, logfile.read())
    return parsers

def logs_count():

    
    logs = open_parser('/home/shiyanlou/Code/nginx.log')

    ip_list=[]
    request404_list =[]

    for log in logs:
        dt =datetime.strptime(log[1][:-6], "%d/%b/%Y:%H:%M:%S")
        if int(dt.strftime("%d")) ==11:
            ip_list.append(log[0])

        if int(log[3])==404:
            request404_list.append(log[2])

    return ip_list, request404_list


def main():
    ip_list, request404_list = logs_count()
    ip_counts = Counter(ip_list)
    request404_counts = Counter(request404_list)

    sorted_ip = sorted(ip_counts.items(),key=lambda x:x[1])

    sorted_request404 = sorted(request404_counts.items(),key=lambda x:x[1])


    ip_dict = dict([sorted_ip[-1]])
    url_dict = dict([sorted_request404[-1]])

    print(ip_dict, url_dict)


if __name__ == '__main__':
    main()
