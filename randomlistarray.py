import math
import os
from os import *

os.system('cls') #clear screen like clrscr  from 'uses crt;' crt lib
# Finding Prime Number
def isPrime(num):
    #print(math.sqrt(i) % round(math.sqrt(i)) != 0)
    if (num > 1):
        #True
        for i in range(2, int(math.sqrt(num)+1)):
            if num % i == 0:
                return False
    else: 
        #False
        return False
    return True
# Display and Position Index
def displayArray(list):
    numPrimeCounted = 0
    print("Prime numbers:")
    for num in list:
        # print("\n")
        # print(num,end=" ")
        if isPrime(num) == True:
            print(num,end =" ")
            numPrimeCounted += 1
        else:
            print(0,end =" ")

    print("\n")
    print("List:")
    for num in list:
        print(num, end =" ")
    
    print("\n")
    print("List Indexs:")
    numPrimeCounted = 0
    for num in list:
        print(numPrimeCounted, end =" ")
        numPrimeCounted += 1
# Count
def countArray(list):
    numPrimeCounted = 0
    numCounted = 0
    for num in list:
        numCounted += 1
    for num in list:
        if isPrime(num) == True:
            numPrimeCounted += 1
    print("\n")
    print("\nNumber of prime numbers in that list:" + str(numPrimeCounted))
    print("\nNumber of numbers in that list:" + str(numCounted))
# Postion as 0 and 1
def posArray(list):
    print("\n")
    print("Boolean indexPos prime number:")
    for num in list:
        if isPrime(num) == True:
            print("1", end =" ")
        else:
            print("0", end =" ")
# Basic calculation: ADD SUB MUL DIV MAX MIN
# TODO: Calculate Prime numbers smarter // Switch pls no IF pls.
def calculateNum(list,operation):
    #Implement switch case Python doesn't have it so... How many IF ELIF ELSE im not gonna go insane with it
    def add(list):
        numCalc = 0
        for num in list:
            if isPrime(num):
                # print(numCalc)
                numCalc += num
        return numCalc
    def subtract(list):
        numCalc = 0
        for num in list:
            if isPrime(num):
                # print(numCalc)
                numCalc -= num
        return numCalc
    def multiply(list):
        numCalc = list[0]
        for num in list:
            if isPrime(num) & num != list[0]:
                #print(numCalc)
                numCalc *= num
        return numCalc
    def divide(list):
        numCalc = list[0]
        for num in list:
            if isPrime(num) & num != list[0]:
                #print(numCalc)
                numCalc /= num
        return numCalc
    def min(list):
        minPrime = list[0]
        numPrimeCounted = 0
        for num in list:
            # Un-comment if you want to display compare
            ## print(str(minPrime) + " > " + str(num))
            if isPrime(num) == True & (minPrime > num) == True:
                # print(str(minPrime) + " > " + str(num))
                minPrime = num
                numPrimeCounted += 1
        return minPrime
    def max(list):
        maxPrime = list[0]
        numPrimeCounted = 0
        for num in list:
            # print(str(maxPrime) + " < " + str(num))
            if isPrime(num) == True & (maxPrime < num) == True:
                # Un-comment if you want to display compare
                # print(str(maxPrime) + " < " + str(num))
                maxPrime = num
                numPrimeCounted += 1
        return maxPrime
    def default(list):
        return "NO You... I'm not letting you to do that."

    switcher = {
        1: add,
        2: subtract,
        3: multiply,
        4: divide,
        5: min,
        6: max
        }

    def switch(list,operation):
        return switcher.get(operation, default)(list)
    if operation == 6:
        return print("Max: " + str(max(list)))
    elif operation == 5:
        return print("Min: " + str(min(list)))
    else:
        return print(switch(list,operation))

# Array
Array = [31,47,13,15,17,14,19,17,3,1,4,2,9,51]

# TODO: I'm too lazy to do the prompt to display on terminal on debugging. Finish it if you want.
def prompt():
    inputNumber = 0
    Array = [0]
    print('Finding prime number with extras: (type `-1` if done typing)')
    while inputNumber != -1:
        # I'm lazy ok don't blaming me. I have a lot of stuffs to do like Nod...
        print(None)
    
    print(Array)

# numIndex = 31
# print("Vị trí số: "+ str(Array[numIndex])+ " Là số nguyên tố: " + str(isPrime(Array[numIndex])))

# displayArray(Array)
# posArray(Array)
# countArray(Array)
# Tính căn bản 1: Cộng 2: Trừ 3:Nhân 4:Chia 5:Min 6:Max
calculateNum(Array,8)
# prompt()
