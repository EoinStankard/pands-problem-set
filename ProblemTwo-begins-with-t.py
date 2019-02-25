#Name: Eoin Stankard
#Date: 25/02/2019
#Problem Two:Write a program that outputs whether or not today is a day that begins with the
#letter T. An example of running this program on a Thursday is as follows.

import datetime
day = datetime.datetime.today().weekday() #Gets the day of the week
if (day == 1) or (day == 3): # 1=Tuesday and 3= Thursday
  print("Yes. Today begins with T")
else:
  print("No. Today does not begin with T", day)