#Name: Eoin Stankard
#Date: 18/03/2019
#Problem Seven: Write a program that that takes a positive floating point number as input and outputs
#an approximation of its square root.

#Square root generated Newtons Square Root Formula
rootof = float(input("Please enter Value to get square root: " ))
estimate =6.0
while abs((estimate*estimate)-rootof) > 0.1:
    estimate -= ((estimate*estimate)-rootof)/(2*estimate)

print(f"the square root of {rootof} is approx. {round(estimate,3)}")
