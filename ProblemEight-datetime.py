#Name: Eoin Stankard
#Date: 11/03/2019
#Problem Eight: Write a program that outputs today’s date and time in the format ”Monday, January
#10th 2019 at 1:15pm”
import datetime
import calendar
dt = datetime.datetime.strftime(datetime.datetime.now(),"%Y-%m-%d-%H:%M-%S")
day = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
month = ["January","February","March","April","May","June","July","August","September","October","November","December"]
dateAdd = ["st","nd","rd","th","th","th","th","th","th","th","th","th","th","th","th","th","th","th","th","th","st","nd","rd","th","th","th","th","th","th","th","st"]
l = dt.split("-")

dayNum = datetime.datetime.today().weekday()
monthNum = int(l[1])
dateNum = int(l[2])
year = l[0]
#hourNum = int
hourMinuteNum =l[3]
hourMinuteSpl = hourMinuteNum.split(":")
#print(int(hourMinuteSpl[0]))
if int(hourMinuteSpl[0]) >00 and int(hourMinuteSpl[0])<12:
    print(day[dayNum]+",",month[monthNum-1],str(dateNum)+dateAdd[dateNum],year,"at",hourMinuteNum+"am")#prints day
    #print(dt)#prints day
    #print(l)
elif int(hourMinuteSpl[0]) >11 and int(hourMinuteSpl[0])<24:
    print(day[dayNum]+",",month[monthNum-1],str(dateNum)+dateAdd[dateNum],year,"at",hourMinuteNum+"pm")#prints day