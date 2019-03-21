#Name: Eoin Stankard
#Date: 21/03/2019
#Problem Eight: Write a program that outputs today’s date and time in the format ”Monday, January
#10th 2019 at 1:15pm”
#References: https://docs.python.org/3/library/datatypes.html
#            https://docs.python.org/2/library/string.html

import datetime
import calendar
dt = datetime.datetime.strftime(datetime.datetime.now(),"%Y-%m-%d-%H:%M-%S") #prints the values for the date and time
day = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
month = ["January","February","March","April","May","June","July","August","September","October","November","December"]
dateAdd = ["st","nd","rd","th","th","th","th","th","th","th","th","th","th","th","th","th","th","th","th","th","st","nd","rd","th","th","th","th","th","th","th","st"]
l = dt.split("-") #Splits the date and time in line 7 into separate values

dayNum = datetime.datetime.today().weekday() #Gets value for day of the week
monthNum = int(l[1]) #gets the value for month
dateNum = int(l[2]) #gets the value for date
year = l[0] #gets the year
hourMinuteNum =l[3] #gets the hour of the day
hourMinuteSpl = hourMinuteNum.split(":") #Splits the hours from the minutes of the day eg 12:30 will get the value 12

if int(hourMinuteSpl[0]) >00 and int(hourMinuteSpl[0])<12: #if the hour of the day is between 01:00 and 11:00
    print(day[dayNum]+",",month[monthNum-1],str(dateNum)+dateAdd[dateNum],year,"at",hourMinuteNum+"am")#prints day
elif int(hourMinuteSpl[0]) >11 and int(hourMinuteSpl[0])<24:#if the hour of the day is between 00:00 and 23:00
    print(day[dayNum]+",",month[monthNum-1],str(dateNum)+dateAdd[dateNum],year,"at",hourMinuteNum+"pm")#prints day