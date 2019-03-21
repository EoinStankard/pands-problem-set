#Name: Eoin Stankard
#Date: 13/03/2019
#Problem Two:Write a program that outputs whether or not today is a day that begins with the
#letter T. An example of running this program on a Thursday is as follows.
#References: https://docs.python.org/3/library/datatypes.html

import datetime
weekdays = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]#Days of the week
day = datetime.datetime.today().weekday() #Gets the value for day of the week
if (day == 1) or (day==3): # 1=Tuesday and 3= Thursday
  print("Yes. Today begins with T")
  print("Today is "+weekdays[day]) #gets the day of the week from weekdays list
else:
  print("No. Today does not begin with T")
  print("Today is "+weekdays[day]) #gets the day of the week from weekdays list