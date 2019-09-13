#!/usr/bin/env python3
import sys
list1=[]
list2=[]
for i in sys.argv[1:]:
    if len(i)<=3:
        list1.append(i)
    else:
    	len(i)>3
    	list2.append(i)

print(' '.join(list1))
print(' '.join(list2))


