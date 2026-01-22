#!/usr/bin/env python

class Calculator:
    def __init__(self, original=0):
        self.total = original

    def add(self, a):
        self.total = self.total + a
        return self.total

    def sub(self, a):
        self.total = self.total - a
        return self.total

    def mul(self, a):
        self.total = self.total * a
        return self.total

    def div(self, a):
        self.total = self.total / a
        return self.total

    def clr(self):
        self.total = 0
        return self.total

    def result(self):
        return self.total

calculations = Calculator()

def welcome():
    print("Welcome to Akhila's calculator!")

def inputs(value):
    while True:
        try:
            return float(input(value))
        except ValueError:
            print("Please only enter an integer or float. Try again!")

def operations(pick):

    if pick == 1:
        x = inputs("Enter the number you want to add:")
        print("Result:", calculations.add(x))

    elif pick == 2:
        x = inputs("Enter the number you want to subtract:")
        print("Result:", calculations.sub(x))

    elif pick == 3:
        x = inputs("Enter the number you want to multiply:")
        print("Result:", calculations.mul(x))

    elif pick == 4:
        while True:
            x = inputs("Enter the number you want to divide:")
            try:
                print("Result:", calculations.div(x))
                return
            except ZeroDivisionError:
                print("You cannot divide by zero!! Please divide by a different number.")

    elif pick == 5:
        print("You have cleared the calculator back to:", calculations.clr())

    elif pick == 6:
        exit()

welcome()

calculations.total = inputs("Please enter the number you want to operate on:")
print("Thanks. Now you will select what operation you want, corresponding to the listed numbers below")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Clear the calculator.")
print("6. Exit the program.")

while True:
    try:
        pick = int(input("Please enter the number of what operation you want:"))
        if pick <1:
            print("You can only select an integer 1-6. Try again.")
            continue
        elif pick >6:
            print("You can only select an integer 1-6. Try again.")
            continue
        break
    except ValueError:
        print("You can only enter an integer 1-6. Make your life easier.")
        continue

operations(pick)

print("Here is your current result:", calculations.total)
