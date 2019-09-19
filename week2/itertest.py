#!/usr/bin/env python3

testlist = ['Linux','Java','Python','DevOps','Go']

print("Loop Start...")
it = iter(testlist)

try:
    while True:
        course = next(it)
        print(course)
except StopIteration:
    pass
     
print('Loop End')
