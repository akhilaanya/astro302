#!/usr/bin/env python

def exit_with_msg(msg):
    print("{}\n\n Usage: {} <arg1> <arg2>".format(msg, sys.argv[0]))

class Calculator:
    def calculation(add, sub, mul, div, clr, a1, b1):
        def add(c1,c2):
            c = c1 + c2
            return c

        def sub(c1,c2):
            c = c1 - c2
            return c

        def mul(c1,c2):
            c = c1 * c2
            return c

        def div(c1,c2):
            c = c1 / c2
            return c

        def clr():
            c = 0
            return c


Calculator = calculation()

def welcome(message):
    print("Welcome to Akhila's calculator!")

def inputs(c1, c2):
    c1 = float(input("Please enter the first number you want")
    c2 = float(input("please enter the second number you want") 
    return "Thanks. Now you will select what operations you want."

def operations():     
    pick = int(input("Please type in the number of what operation you pick")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Clear the calculator.")
    print("6. Exit the program.")

    if pick == '1':
        add()

    elif pick == '2':
        sub()

    elif pick == '3':
        mul()

    elif pick == '4':
        div()

    elif pick == '5':
        clr()

    else pick == '6':
        exit
    
