#Name: Eoin Stankard
#Date: 28/03/2019
#Problem One:Write a program that asks the user to input any positive integer and outputs the
#sum of all numbers between one and that number.


value=input("Enter a positive integer: ")

def SumOfNum(Val):
    ans ,x= 0,0
    while x != Val: # Wait until x is equal to the value given
        x = x + 1 #add one to current value of x
        ans = ans+x #set answer to current value of x plus current value of ans
    print(ans) #print final answer

try:
    if int(value)>0:
        SumOfNum(int(value))#Call the function created above to print the sum of all numbers between one and the value given 
    elif int(value)<0:#if number is negative
        raise ValueError#raise an exception
except ValueError:
    print("Incorrect Input Given")

