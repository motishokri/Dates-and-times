import calendar

# This function  counts the number of the given weekday for the specified
#  year and month and returns the result

def countdays(theyear, themonth, wichday):
    daycount = 0
    weeklist = calendar.monthcalendar(theyear, themonth)
    for week in weeklist:
        if week[wichday] != 0:
            daycount += 1
    return daycount

print("--Day Counter Program--\n")        

run = True
while(run):
    try:
        print("Wich Day Of The Week Do yo Want to Count?")
        print("0: Monday")
        print("1: Tuesday")
        print("2: Wednesday")
        print("3: Thursday")
        print("4: Friday")
        print("5: Saturday")
        print("6: Sunday")
        print("Or 'exit' to quit")
        
        theday = input("? ")
        if theday == "exit":
            run = False
            break
        day = int(theday)
        
        yearstr = input("Enter Year: ")
        year = int(yearstr)
        
        monthstr = input("Enter Month: ")
        month = int(monthstr)
        
        result = countdays(year, month, day)
        print("There are " + str(result) + " of those days in the month and year specified")
        print("-----------\n")
    except Exception as e :
        print(e)
        print("Sorry, that's not valid input")
        
        
        