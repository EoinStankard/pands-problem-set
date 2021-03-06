#Name: Eoin Stankard
#Date: 28/03/2019
#Problem Four: Write a program that asks the user to input any positive integer and outputs the
#successive values of the following calculation. At each step calculate the next value
#by taking the current value and, if it is even, divide it by two, but if it is odd, multiply
#it by three and add one. Have the program end if the current value is one
#References: https://docs.python.org/2/tutorial/datastructures.html
InputValue=input("Please enter a positive integer: ")


def calculate(value):
    x=0 #variable for list location 
    l=[] #list to hold values
    while value != 1: #While the value is not equal to 1
        if value%2 ==0: # if the current value divides evenly Even
            value = value/2 # Divide the current value by two
            l.insert(x,int(value))
            x=x+1
        else: #Else if the current value does not divide evenly 
            value = (value*3)+1 #Multiply the current value by three and add one
            l.insert(x,int(value))
            x=x+1
    print(*l,sep=" ")#prints list without square brackets and quotation


try:
    if int(InputValue)>0:
        calculate(int(InputValue))#Call the function created above to calculate the output values
    elif int(InputValue)<0:#if number is less than zero 
        raise ValueError #raise exception
except ValueError:
    print("Incorrect Input Given")# incorrect input
