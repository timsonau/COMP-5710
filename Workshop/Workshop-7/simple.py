import logging_example


def simpleDiv(a, b):
    return a/b 


if __name__=='__main__': 
   print('Welcome to the simple division calculator!')
   print('*'*50)
   a=input('Provide first input:')
   print('Thanks') 
   b=input('Provide second input:')
   a, b = int(a), int(b)
   res=simpleDiv(a, b) 
   print('The answer is:', res)