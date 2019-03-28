#Name: Eoin Stankard
#Date: 28/03/2019
#Problem Seven: Write a program that that takes a positive floating point number as input and outputs
#an approximation of its square root.

#Square root generated Newtons Square Root Formula
rootof = input("Please enter Value to get square root: " )


def Calc(r):
    estimate =6.0
    while abs((estimate*estimate)-float(r)) > 0.1:
       estimate -= ((estimate*estimate)-float(r))/(2*estimate)

    print(f"The square root of {r} is approx. {round(estimate,3)}")

try:
    if float(rootof)<0:#Check for value greater than zero
        raise ValueError#Raise Exception
    elif float(rootof)>0:#Greater than zero
        Calc(float(rootof))#Call function to calculate
    
except ValueError:
    print("Incorrect input given")
