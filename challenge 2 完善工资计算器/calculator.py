#!/usr/bin/env pythn3
import sys


def count_salary(salary):
    Taxalbe_income = salary-salary*0.165-5000
    if Taxalbe_income<0:
    	tax =0
    elif Taxalbe_income<=3000:
    	tax =Taxalbe_income*0.03
    elif 3000<Taxalbe_income<=12000:
    	tax =Taxalbe_income*0.1-210
    elif 12000<Taxalbe_income<=25000:
    	tax =Taxalbe_income*0.2-1410
    elif 25000<Taxalbe_income<35000:
    	tax =Taxalbe_income*0.25-2660
    elif 35000<Taxalbe_income<=55000:
    	tax =Taxalbe_income*0.3-4410
    elif 55000<Taxalbe_income<=80000:
    	tax =Taxalbe_income*0.35-7160
    else:
    	80000<Taxalbe_income
    	tax =Taxalbe_income*0.45-15160
    
    finally_salary = salary -salary*0.165-tax
    return finally_salary
    

def print_finally_salary(num_id, salary):
	print('{}:{:.2f}'.format(num_id, salary))


if __name__ == "__main__":
    for arg in sys.argv[1:]:
        salary_list = arg.split(':')
        finally_salary = count_salary(int(salary_list[1]))
        try:
        	print_finally_salary(salary_list[0],finally_salary)
        except (ValueError, TypeError):
            print('Parameter Error')


