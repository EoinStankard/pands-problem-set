#Name: Eoin Stankard
#Date: 04/03/2019
#Problem Seven: Write a program that that takes a positive floating point number as input and outputs
#an approximation of its square root.
import math
#Asks for an psoitive input value
value = float(input("Please enter a positive number: "))
dec = int(input("Number of decimal places: "))
#Created a variable called root that would hold the value of the square root
#Imported the math library and then used the sqrt function to calculate the square root
root = math.sqrt(value)
#Used the round function to round the square root to one decimal place
ans = round(root,dec)
print(ans)

