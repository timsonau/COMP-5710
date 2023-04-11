'''
Author: Tim Son
Code needed for Workshop 8
'''

import traceback
from ast import operator
import random 

def divide(v1, v2):
    temp = 0 
    if (isinstance(v1, int))  and (isinstance(v2, int)): 
       if v2 >  0:
          temp =  v1 / v2
       elif v2 < 0:
          temp = v1 / v2 
       else:
          print("Divisor is zero. Provide non-zero values.")
    else: 
       temp = "Invalid input. Please provide numeric values."    
    return temp 

def simpleCalculator(v1, v2, op):
    try:
        if (op == '/'):
            return v1 / v2
        elif (op == '*'):
            return v1 * v2  
        elif(op == "-"):
            return v1 - v2
        elif(op == "+"):
            return v1+v2
        else:
            print('Invalid Operand')
            return 0
    except Exception as e:
        print("\n*****ERROR*****")
        traceback.print_exc()
    
def fuzzValues():
    #In-Class
    # positive or expected software testing 
    #res = divide(2, 1)
    # negative software testing: > 0 divisor test 
    #res = divide(2, 0)
    # negative software testing: <0 divisor test 
    #res = divide(2, -1)
    # negative software testing: check types: example 1  
    res = divide(2, '1')  
    # negative software testing: check types: example 2 
    res = divide('2', '1') 
    print(res)   
    print('='*100)

    #Workshop 8
    #error 1 v1=String and v2=int divider
    simpleCalculator('8', 2, '/')
    #error 2 Zero divider
    simpleCalculator(3, 0, '/')
    #error 3 v1=String sequence and v2=non-int multiply
    simpleCalculator('🏳0🌈️', ' ॣh ॣ ॣ冗', '*')
    #error 4  v1=float and v2=string divider
    print(simpleCalculator(-777E+02332434422132, '-555333E+102', '/'))
    #error 5 v1=nonetype and v2=int addition
    simpleCalculator(None, 7, '+')
    #error 6 v1=list and v2=list multipliy
    simpleCalculator([8], [8], '*')
    #error 7 v1=int and v2=set multiply 
    simpleCalculator(0xA0F, {22}, '*')

def simpleFuzzer(): 
    fuzzValues()

if __name__=='__main__':
    simpleFuzzer()