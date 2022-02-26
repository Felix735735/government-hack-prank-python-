import time
#This is a government hack piece of code
#Initialising
#20%
#40%
#60#
#100#

government = input("What government do you want to hack? (example: British, Chinese)")
database = input("What database do you want to hack?")
time = input("What time do you want to start this hack?")
project = input("What will this project be called?")
name = ("And lastly, what is your name?")
time.sleep(5)

print(" The " + government + " has been hacked,the " + database + " database has been hacked,this project will take place at " + time + " .This project will be called " + project + " .This has been executed by " + name)



time.sleep(5)
print("STARTING")
time.sleep(2)
print("INTIALISING")
time.sleep(1)
print("10%")
time.sleep(3)
print("70%")
time.sleep(1)
print("100%")
time.sleep(0.3)
print("Completed!")

time.sleep(2)
print("NOT A SCAM, PLEASE READ THE FULL SENTENCE! PLEASE VERIFY YOUR NOT A ROBOT BY COMPLETING THIS MATH QUIZ")

time.sleep(3)
import random
import operator

def quiz():

    print('Hello. This is a 10 question math quiz\n. Complete all 10 questions for government hack to start.')
    name = input("Please enter your name")
    print("Hello", name," Let's begin the quiz!")
    score = 0
    for i in range(10):
        correct = askQuestion()
        if correct:
            score += 1
            print('Correct!\n')
            print(score)
            break
        else:
            print('Incorrect!\n')

    return 'Your score was {}/10'.format(score)


def askQuestion():
    answer = randomCalc()
    guess = float(input())
    return guess == answer

def randomCalc():
    ops = {'+':operator.add,
    '-':operator.sub,
    '*':operator.mul,
    '/':operator.truediv}
    num1 = random.randint(0,11)
    num2 = random.randint(1,11)   
    op = random.choice(list(ops.keys()))
    answer = ops.get(op)(num1,num2)
    print('What is {} {} {}?\n'.format(num1, op, num2))
    return answer
    print(score)

quiz()
askQuestion()
randomCalc()

time.sleep(0.5)
from turtle import *

color('green')
speed(11)
for i in range(120):
    circle(i * 1.5)
    right(4)

hideturtle()
done()

print('The hack has been successful')
