#Name: Eoin Stankard
#Date: 13/03/2019
#Problem Nine: Write a program that reads in a text file and outputs every second line. The program
#should take the filename from an argument on the command line.

#This program is created to display every second line, This does not include blank lines
#So only every second line of text will be printed

x = 0 #line count
with open('moby-dick.txt','r') as file:# Open the file moby-dick.txt as read only
    for line in file:
        # if the length of the line is greater that one character 
        #Lines with one character will be blank lines with the newline character at the end (\n)
        if len(line) > 1:
            #x will start at 0 and then get incremented when each line is read
            #It will then use modulus to see if it is an even number
            #If it is print the line
            if x % 2 == 0:
                print(line, end='')
            x = x + 1#Add one to the line count to read the next line