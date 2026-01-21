#!/usr/bin/env python

def exit_with_msg(msg):
    print("{}\n\n Usage: {} <arg1> <arg2>".format(msg, sys.argv[0]))

class Calculator:

def calc(add, sub, mul, div, clr, a1, b1):
    def add(a1,b1):
        c = a1 + b1
        return c

    def sub(a1,b1):
        c = a1 - b1
        return c

    def mul(a1,b1):
        c = a1 * b1
        return c

    def div(a1,b1):
        c = a1 / b1
        return c

        except ZeroDivisionError as err:
            exit_with_msg("Error: {}. You cannot divide <arg1> by <arg2> since <arg2> is zero. Please try again.".format(msg))

    def clr():
        c = 0
        return c

    except ValueError as e:
        exit_with_msg("Error: {}. All arguments must be numbers. Please try again.".format(e))

Calculator = calc()

def welcome(message):
    print("Welcome to Akhila's calculator!")

def inputs(a1, b1):
    a1 = float(input("Please enter the first number you want")
    b1 = float(input("please enter the second number you want") 
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

    elif pick == '6':
        exit
    
    else except ValueError as e:
        exit_with_msg("Error: {}. You need to enter an integer from 1 to 4.".format(e))


