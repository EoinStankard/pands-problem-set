#Name: Eoin Stankard
#Date: 13/03/2019
#Problem Three: Write a program that prints all numbers between 1,000 and 10,000 that are divisible
#by 6 but not 12.

x=0
print("Numbers divisable by 6 but not 12 between 1000-10000")
for i in range (1000,10000,1): #Start current value of i at 1000 and count to 10000 in increments of 1
    if (i%6 == 0) and (i%12 != 0): #if the current value modulus 6 is zero and current value modulus 12 is not equal to zero
        print("\t",i) #tab in one and print the value
        x=x+1
print("There are",x,"Numbers divisable by 6 but not 12 between 1000-10000")#Print amount of values
