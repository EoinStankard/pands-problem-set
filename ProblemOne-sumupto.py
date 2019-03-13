#Name: Eoin Stankard
#Date: 13/03/2019
#Problem One:Write a program that asks the user to input any positive integer and outputs the
#sum of all numbers between one and that number.


value=input("Enter a positive integer: ")

def SumOfNum(Val):
    ans ,x= 0,0
    while x != Val: # Wait until x is equal to the value given
        x = x + 1 #add one to current value of x
        ans = ans+x #set answer to current value of x plus current value of ans
    print(ans) #print final answer

if(value.isdigit()): #Check if the input is an positive integer
    SumOfNum(int(value))#Call the function created above to print the primes
else:
    print("Incorrect Input Given")# incorrect input
