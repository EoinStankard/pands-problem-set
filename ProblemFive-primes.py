#Name: Eoin Stankard
#Date: 28/02/2019
#Problem Five: Write a program that asks the user to input a positive integer and tells the user
#whether or not the number is a prime.

value=int(input("Please enter a positive integer: "))
#initial number the input value will be divided by
divisor = 1
#Count for how may numbers can divide into the input
divisorCount = 0
#Variable that determines when the program finishes
done =0
#This code will keep looping until the done variable is given 1. I used this as i will need to do multiple cycles
#through each if statement to determine if it is a prime or not
while done != 1:
    #This will look for the modulus of the input value divided by the divisor, I used this as the input value will always be divided by one to start
    #so this will always give a value equal to zero, I will then increment divisorCount as a prime number can only be divided by itself and one.
    #This means that once it enters the first if statement it already has 1/2 numbers
    #It will also increment the divisor. so the divisor will now go to 2
    if value%divisor ==0 and divisorCount == 0:
        divisorCount = divisorCount +1
        divisor = divisor+1
    #If the divisorCount equals 1 and the divisor equals the input value modulus the divisor equals zero 
    #Then this number is a prime,The divisorcount will only increment is it finds a value that can divide into it 
    #So if the divisor count reachs the input value then the value is a prime  
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