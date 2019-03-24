#Name: Eoin Stankard
#Date: 24/03/2019
#Problem Ten: Write a program that displays a plot of the functions x, x^2
# and 2^x

print("Please select a function to Plot from [0,4]")
print("1. Function X")
print("2. Function x^2")
print("3. Function 2^x")
print("4. All Functions")
value = input("Choice: ")

import matplotlib.pyplot as plt 
import numpy as np

def plot(v):
    x = np.arange(0.0, 4.0, 1)
    if (v==1):
        plt.plot (x,'r--')
        plt.title('Plotting function x')
        plt.legend(['x'])
        
    elif (v==2):
        #x =np.arange(0.0, 4.0, 1)
        plt.plot (x**2,'b--')
        plt.title('Plotting function x^2')
        plt.legend(['x^2'])
        #plt.xlabel('X-Axis')
        #plt.ylabel('Y-Axis')
        #plt.show()
    elif (v==3):
        #x = np.arange(0.0, 4.0, 1)
        plt.title('Plotting function 2^x')
        plt.legend(['2^x'])
        plt.plot (2**x,'g--')
        #plt.xlabel('X-Axis')
        #plt.ylabel('Y-Axis')
        #plt.show()
    else:
        #x = np.arange(0.0, 4.0, 1)
        plt.plot ( x, 'r--', x**2, 'b--', 2**x, 'g--')
        plt.title('Plotting all functions')
        plt.legend(['x', 'x^2', '2^x'])
        #plt.xlabel('X-Axis')
        #plt.ylabel('Y-Axis')
        #plt.grid(True)
        #plt.show()
    plt.xlabel('X-Axis')
    plt.ylabel('Y-Axis')
    plt.grid(True)
    plt.show()

if(value.isdigit()): #Check if the input is an positive integer
    if int(value)==1 or int(value)==2 or int(value)==3 or int(value)==4:#check if value is between 1-4
        plot(int(value))
    else:
        print("Incorrect Input Given")# incorrect input
else:
    print("Incorrect Input Given")# incorrect input



