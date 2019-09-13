#!/usr/bin/env python3
# --*--coding:utf-8--*--
import sys

try:
    salary = int(sys.argv[1])
except:
    print('must be int!')
    
Taxalbe_income = salary - 5000
      
if Taxalbe_income<=3000:
    Final_salary = Taxalbe_income*0.03 
elif 3000<Taxalbe_income<=12000:
    Final_salary = Taxalbe_income*0.1 -210
elif 12000<Taxalbe_income<=25000:
    Final_salary = Taxalbe_income*0.2 -1410
elif 25000<Taxalbe_income<=35000:
    Final_salary = Taxalbe_income*0.25 -2660
elif 35000<Taxalbe_income<=55000:
    Final_salary = Taxalbe_income*0.30 -4410
elif 55000<Taxalbe_income<=80000:
    Final_salary = Taxalbe_income*0.35 -7160
elif 80000<Taxalbe_income:
    Final_salary = Taxalbe_income*0.45 -15160

print(format(Final_salary,".2f"))


