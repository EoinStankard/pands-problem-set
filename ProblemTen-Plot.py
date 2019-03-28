#Name: Eoin Stankard
#Date: 28/03/2019
#Problem Ten: Write a program that displays a plot of the functions x, x^2
# and 2^x
import matplotlib.pyplot as plt 
import numpy as np

print("Please select a function to Plot from [0,4]")
print("1. Function X")
print("2. Function x^2")
print("3. Function 2^x")
print("4. All Functions")
value = input("Choice 1-4: ")

def plot(v):#function for plotting graph
    x = np.arange(0.0, 4.0, 1) #Graph from 0-4 in steps of 1
    if (v==1):#input of 1
        plt.plot (x,'r--')#plot graph x
        plt.title('Plotting function x')#add heading
        plt.legend(['x'])#add legend
        
    elif (v==2):
        plt.plot (x**2,'b--')
        plt.title('Plotting function x^2')
        plt.legend(['x^2'])
        
    elif (v==3):
        plt.title('Plotting function 2^x')
        plt.legend(['2^x'])
        plt.plot (2**x,'g--')

    else:
        plt.plot ( x, 'r--', x**2, 'b--', 2**x, 'g--')
        plt.title('Plotting all functions')
        plt.legend(['x', 'x^2', '2^x'])

    plt.xlabel('X-Axis')#add x Label
    plt.ylabel('Y-Axis')#add y Label
    plt.grid(True) #Add grid
    plt.show()#Show graph

try:
    if int(value)==1 or int(value)==2 or int(value)==3 or int(value)==4:#check if value is between 1-4
        plot(int(value))#call function
    else:
        raise ValueError #raise exception
except ValueError:
    print("Incorrect Input Given")# incorrect input



