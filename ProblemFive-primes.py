#Name: Eoin Stankard
#Date: 28/03/2019
#Problem Five: Write a program that asks the user to input a positive integer and tells the user
#whether or not the number is a prime.

value=input("Please enter a positive integer: ")

#This code will keep looping until the done variable is given 1. I used this as i will need to do multiple cycles
#through each if statement to determine if it is a prime or not
def printprimes(value):
    #initial number the input value will be divided by
    divisor = 1
    #Count for how may numbers can divide into the input
    divisorCount = 0
    #Variable that determines when the program finishes
    done =0
    while done != 1:
        #This will look for the modulus of the input value divided by the divisor, I used this as the input value will always be divided by one to start
        #so this will always give a value equal to zero, I will then increment divisorCount as a prime number can only be divided by itself and one.
        #This means that once it enters the first if statement it already has 1/2 numbers
        #It will also increment the divisor. so the divisor will now go to 2
        if value%divisor ==0 and divisorCount == 0:
            divisorCount = divisorCount +1
            divisor = divisor+1
        elif divisorCount ==1 and divisor == value and value%divisor==0:
            print("This is a prime")
            done = 1
        #If the divisorCount is equal to one and the value divided by the divisor equals zero and
        #The divisor does not equal the input value then this number is not a prime
        elif value%divisor == 0 and divisorCount ==1 and divisor != value:
            print("This is not a prime")
            done=1
        #For any other scenario, increment the divisor by one
        else:
            divisor=divisor+1


try:
    if int(value)>0:
        printprimes(int(value))#Call the function created above to calculate the output values
    elif int(value)<0:#if number is less than zero 
        raise ValueError #raise exception
except ValueError:
    print("Incorrect Input Given")# incorrect input
