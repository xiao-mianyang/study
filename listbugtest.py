#!/usr/bin/env python3


def compute(value, *base):
    c = list(base)
    c.append(value)
    result = sum(c)
    print(result)
    

if __name__ == '__main__':
    testlist = (10,20,30)
    compute(15,*testlist)
    compute(25,*testlist)
    compute(35,*testlist)




