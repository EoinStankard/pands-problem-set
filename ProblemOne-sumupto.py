#Name: Eoin Stankard
#Date: 25/02/2019
#Problem One:Write a program that asks the user to input any positive integer and outputs the
#sum of all numbers between one and that number.

ans ,x= 0,0
try:
    i=int(input("Enter a positive integer: "))
    while x != i:
       x = x + 1
       ans = ans+x 
    print(ans)
except ValueError:
    print("Incorrect Input")
