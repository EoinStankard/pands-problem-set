#Name: Eoin Stankard
#Date: 28/02/2019
#Problem Six: Write a program that takes a user input string and outputs every second word

string = str(input("Please enter a sentence: "))
#split the input string
spl = string.split(" ")
#Add each word to a list
#I done this as i thought it would be easiest to print every
#second word
l = list(spl)
#Second list created to store every second word
#This would make it easy to print all words together
l2 = []
#print(len(l))

#variable to count every second word
x=0
#while loop to go through the list
#Even length string will finish on the last word
#Odd number length string will finish on the second last word
while x < len(l):
    #print(l[x])
    #Insert first word into list l2 and then add 2 to x
    #and then add that word to the list
    l2.insert(x,l[x])
    x=x+2
#print(l2)
print(' '.join(l2))

##Below is how i origionally started 
#for x in range(len(l)):
    #l[x] = l[x+2]
 #   print(l[x],l[x+1])