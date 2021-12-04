#In this file, I will attemp to make a calculator.

#Taking Inputs
from os import close


opr = str(input("Choose an operation (+, -, *, /): "))
a = int(input("Enter a number: "))
b = int(input("Enter another number: "))

#Performing Operations

if opr == "+":
    c = a + b

elif opr == "-":
    c = a - b

elif opr == "*":
    c = a * b

elif opr == "/":
    c = a / b

#Secret Feature

elif opr == "do the freaky":
    c = a ** b

#Giving Answers
print(c)