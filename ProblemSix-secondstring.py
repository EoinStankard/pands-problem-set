#Name: Eoin Stankard
#Date: 21/03/2019
#Problem Six: Write a program that takes a user input string and outputs every second word
#References: https://docs.python.org/2/tutorial/datastructures.html

string = input("Please enter a sentence: ")

spl = string.split(" ")#split the input string using spaces

l = list(spl)#Add each word to a list
l2 = []#Second list created to store every second word
x = 0#variable to count every second word

#while loop to go through the list
#Even length string will finish on the last word (Even amount of words)
#Odd number length string will finish on the second last word (Odd amount of words)
while x < len(l):
    #Insert first word into list l2 and then add 2 to x
    #and then add that word to the list
    l2.insert(x,l[x])
    x=x+2
print(' '.join(l2))