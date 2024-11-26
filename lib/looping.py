#!/usr/bin/env python3

def happy_new_year():
    # code goes here!
    i= 10
    while( i>0):
        print (i)
        i-=1
        print("Happy New Year!")
         

def square_integers(int_list):
    # code goes here!
    squared_integer = [item*item for item in int_list]
    return squared_integer

def fizzbuzz():
    # code goes here!
    for i in range(1,101):
        if i % 15 == 0:
            print ('FizzBuzz')
        elif i % 3 == 0:
            print ('Fizz')
        elif i % 5 == 0:
            print ('Buzz')
        else:
            print (i)