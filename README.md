# pands-problem-set Solutions

This repository contains my solutions to the problem set 2019 for the module Programming and Scripting in GMIT

##How to download this repository
1. Go To Github
2. click the download button

##How to run the code
1. Make sure Python is installed
2. Go to the location of the python scripts and open a command window
3. Enter 'Python' followed by one of the scripts that i have mentioned below

##The Problem set and short description
1. Name: 
    ProblemOne-sumupto.py
    
   How to Run:
    python ProblemOne-sumupto.py
    
   Description: 
    Write a program that asks the user to input any positive integer and outputs the
    sum of all numbers between one and that number.
    
   How I wrote the Code:
    This program asks the user for a positive integer input. This input is then put into a function where the ouput will be generated. The while loop will keep adding until the variiable x is equal to the input value. This variable starts at zero and then adds one with every loop of the code. 
    
2. Name:
     ProblemTwo-begins-with-t.py
     
   How to Run:
     python ProblemTwo-begins-with-t.py

   Description:
     Write a program that outputs whether or not today is a day that begins with the
     letter T. An example of running this program on a Thursday is as follows.
     
   How i wrote the Code:
    This is a very basic script where i use the datetime library, I then use this library to give me the current day, The value returned is an integer between 0 and 6. These value are the days of the week eg. 1 = Monday. So i implemented a simple if statement to check if the day of the week starts with 'T'.
     
3. Name:
     ProblemThree-divisors.py
   
   How to Run:
     python ProblemThree-divisors.py
     
   Description:
     Write a program that prints all numbers between 1,000 and 10,000 that are divisible
     by 6 but not 12.
    
   How i wrote the Code:
    The code uses a for loop the increments by 1 in the range between 1000 and 10000. It then check to see if the current value is divisable by 6 and not 12 by using modulus. If the value is divisable by 6 and not 12 then the value is printed.
     
4. Name:
     ProblemFour-collatz.py
     
   How to Run:
     python ProblemFour-collatz.py
     
   Description:
     Write a program that asks the user to input any positive integer and outputs the
     successive values of the following calculation. At each step calculate the next value
     by taking the current value and, if it is even, divide it by two, but if it is odd, multiply
     it by three and add one. Have the program end if the current value is one.

    How i wrote the Code:
      This code is implemented by asking for a positive integer, This integer is then a variable of a while loop where the loop will keep running until this number is equal to 1. If the value is divisable by two evenly then i have to divide that value by two. this then becomes the input value and it is also added to a list, The same is done for if the value is not divisable by two, By instead of dividing by two the value gets multiplied by three and then one is added, This also gets added to the list, This will keep running until the value equals one, The whole list is then printed.
    
5. Name:
     ProblemFive-primes.py
     
   How to Run:
     python ProblemFive-primes.py
     
   Description:
     Write a program that asks the user to input a positive integer and tells the user
     whether or not the number is a prime
     
   How i wrote the Code:
     A prime is only divisable by itself and 1,The user is asked to give a positive interger input,I used a while loop and created a variable that would increment by one until it is equal to the input value, Multiple if statement were also used. I also used a second variable that would store the count of the divisors, So for the first run of the code if the input is 7 this value will be divided by one and since one is one of two number that determine if a number is a prime or not, this will then increment the divisor count, The code will keep cycling until the divisor count is equal to 2 and the incremented variable is equal to the input value.
   
6. Name:
     ProblemSix-secondstring.py
    
   How to Run:
     python ProblemSix-secondstring.py
     
   Description:
     Write a program that takes a user input string and outputs every second word
     
   How i wrote the Code:
     This script asks the user to enter a string, The string is then split by spaces and put into a list, Awhile loop is then used to cycle through this list and put every second word into a second list, The second list is then printed to the user.
      
7. Name:
     ProblemSeven-squareroot.py
     
   How to Run:
     python ProblemSeven-squareroot.py
     
   Description:
     Write a program that that takes a positive floating point number as input and outputs
     an approximation of its square root.
     
   How i wrote the Code:
     The user is ased to enter a value and the output will be output. This was programmed using Newtons Square Root Formula.
 
8. Name:
     ProblemEight-datetime.py
     
   How to Run:
     python ProblemEight-datetime.py
   
   Description:
     Write a program that outputs today’s date and time in the format ”Monday, January
     10th 2019 at 1:15pm”.
    
    How i wrote the Code:
      This was creted using the DateTime and Calendar libraries,When getting values for the date and month integer values are returned, I created multiple lists that stored the days, Months and the superscripts, Using these and the integer values i was able to create a script that would print the date and time in the correct format
   
9. Name:
     ProblemNine-second.py
    
   How to Run:
     python ProblemNine-second.py moby-dick.txt
     
   Description:
     Write a program that reads in a text file and outputs every second line. The program
     should take the filename from an argument on the command line.
     
   How i wrote the Code:
     The script is created using arguments, The script will ask for a text file input on the command line, The script will then read the file and print every second line of text, It will skip each line of text that has a blank line. This is done by reading each line and if the length of the line is greater then one then that line contains text, I use greater than one as a blank line contains the newline character.
   
10. Name:
     ProblemTen-plot.py
    
   How to Run:
     python ProblemTen-plot.py
     
   Description:
     Write a program that displays a plot of the functions x, x^2 and 2^x
     in the range [0, 4].
     
   How i wrote the Code:
     The script uses matplotlib and numpy libraries to implement the script. I user is given some choices of what sort graph they want displayed, The graph displayed depends on the user input, all graphs are in the range o-4 and in time steps of 1ms. all graphs are printed with labels and a grid.
     


##References

