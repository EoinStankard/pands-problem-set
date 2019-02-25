#Name: Eoin Stankard
#Date: 25/02/2019
#Problem Four: Write a program that asks the user to input any positive integer and outputs the
#successive values of the following calculation. At each step calculate the next value
#by taking the current value and, if it is even, divide it by two, but if it is odd, multiply
#it by three and add one. Have the program end if the current value is one

value=int(input("Please enter a positive integer: "))

while value != 1: #While the value is not equal to 1
    if value%2 ==0: # if the current value divides evenly Even
        value = value/2 # Divide the current value by two
        print(int(value))
    else: #Else if the current value does not divide evenly 
        value = (value*3)+1 #Multiply the current value by three and add one
        print(int(value))
