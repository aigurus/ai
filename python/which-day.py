def isYearLeap(year):
    if(year % 4 == 0 and year % 100 != 0):
        return True
    elif(year % 100 == 0 and year % 400 != 0):
        return False
    elif(year % 400 == 0):
        return True
    else:
        return False
#
# your code from LAB 4.1.3.6
#

def daysInMonth(year, month):
    if(isYearLeap(year)==True and month == 2):
        return 29
    elif(isYearLeap(year)!=True and month == 2):
        return 28
    elif(month in [4,6,9,11]):
        return 30
    elif(month in [1,3,5,7,8,10,12]):
        return 31
    else:
        return None
#
# your code from LAB 4.1.3.7
#

def dayOfYear(year, month, day):
    if(month==12):
        month = 2
    elif(month == 11):
        month = 1
    else:
        month = month-2
    ltd = year%100
    ftd = int(year//100)
    print(ltd)
    print(ftd)
    #Zeller’s Rule
    #F=k+ [(13*m-1)/5] +D+ [D/4] +[C/4]-2*C
    F = day + int((((13*month)-1)/5)) + ltd + int((ltd/4)) + int((ftd/4)) - 2 * ftd
    print(F)
    T = int(F) % 7
    print(T)
    if(T == 0):
        return "Sunday"
    elif(T == 1):
        return "Monday"
    elif(T == 2):
        return "Tuesday"
    elif(T == 3):
        return "Wednesday"
    elif(T == 4):
        return "Thursday"
    elif(T == 5):
        return "Friday"
    elif(T == 6):
        return "Saturday"
    else:
        return None
#
# put your new code here
#
#F=k+ [(13*m-1)/5] +D+ [D/4] +[C/4]-2*C where

#k is  the day of the month.
#m is the month number.
#D is the last two digits of the year.
#C is the first two digits of the year.

print(dayOfYear(1920, 6, 10))