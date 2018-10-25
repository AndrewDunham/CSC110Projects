# Program 1-B: Date Calculator
# Andrew Dunham

# This program was created before the class had learned loops.

def main():
    
    leapYear = False #Setting leap year default to be false. 
    month = "Month" #Setting the month to print "month" as default
    day = 0 #Setting day to print 0 as default
    
    #Printing informative statements
    print("D A T E   C A L C U L A T O R")
    print("Outputs the month, day and year: \n")
    
    startingYear = int(input("Input year ==> "))#Takes input for the starting year
    daysPast = int(input("Input number of days passed ==>"))#Takes input for the days past in the year
   
    
    #Find if the year is a leap year
    if startingYear %100 == 0: 
        if startingYear %400 == 0:
            leapYear = True
    elif startingYear %4 == 0:
            leapYear = True
    else:
        leapYear = False
            
    
    #Depending on if it is a leap year, print what day and month it is.
    if leapYear == True:
        if daysPast <= 31:
            month = "January"
        elif daysPast <= 59 and daysPast > 31:
            month = "February"
        elif daysPast <= 90 and daysPast > 59:
            month = "March"
        elif daysPast <= 120 and daysPast > 90:
            month = "April"
        elif daysPast <= 151 and daysPast > 120:
            month = "May"
        elif daysPast <= 181 and daysPast > 151:
            month = "June"
        elif daysPast <= 212 and daysPast > 181:
            month = "July"
        elif daysPast <= 243 and daysPast > 212:
            month = "August"
        elif daysPast <= 273 and daysPast > 243:
            month = "September"
        elif daysPast <= 304 and daysPast > 273:
            month = "October"
        elif daysPast <= 334 and daysPast > 304 :
            month = "November"
        elif daysPast <= 365 and daysPast > 334 :
            month = "December"
       
    #If it is not a leap year, it is the following month.       
    if leapYear == False: 
        if daysPast <= 31:
            month = "January"
        elif daysPast <= 60 and daysPast > 31:
            month = "February"
        elif daysPast <= 91 and daysPast > 60:
            month = "March"
        elif daysPast <= 121 and daysPast > 91:
            month = "April"
        elif daysPast <= 152 and daysPast > 121:
            month = "May"
        elif daysPast <= 182 and daysPast > 152:
            month = "June"
        elif daysPast <= 213 and daysPast > 182:
            month = "July"
        elif daysPast <= 244 and daysPast > 213:
            month = "August"
        elif daysPast <= 274 and daysPast > 244:
            month = "September"
        elif daysPast <= 305 and daysPast > 274:
            month = "October"
        elif daysPast <= 335 and daysPast > 305 :
            month = "November"
        elif daysPast <= 366 and daysPast > 335 :
            month = "December"
            
   #Printing the day     
    if month == "January":
        day = daysPast
    elif month == "February":
        day = daysPast - 31
    elif month == "March" and leapYear == True:
        day = daysPast - 60
    elif month == "March" and leapYear == False:
        day = daysPast - 59
    elif month == "April" and leapYear == True:
        day = daysPast - 91
    elif month == "April" and leapYear == False:
        day = daysPast - 90
    elif month == "May" and leapYear == True:
        day = daysPast - 121
    elif month == "May" and leapYear == False:
        day = daysPast - 120
    elif month == "June" and leapYear == True:
        day = daysPast - 152
    elif month == "June" and leapYear == False:
        day = daysPast - 151
    elif month == "July" and leapYear == True:
        day = daysPast - 182
    elif month == "July" and leapYear == False:
        day = daysPast - 181
    elif month == "August" and leapYear == True:
        day = daysPast - 213
    elif month == "August" and leapYear == False:
        day = daysPast - 212
    elif month == "September" and leapYear == True:
        day = daysPast - 244
    elif month == "September" and leapYear == False:
        day = daysPast - 243
    elif month == "October" and leapYear == True:
        day = daysPast - 274
    elif month == "October" and leapYear == False:
        day = daysPast - 273
    elif month == "November" and leapYear == True:
        day = daysPast - 305
    elif month == "November" and leapYear == False:
        day = daysPast - 304
    elif month == "December" and leapYear == True:
        day = daysPast - 335
    elif month == "December" and leapYear == False:
        day = daysPast - 334
        
    #Final print statement
    print(month, day,",", startingYear)
        
if __name__ == '__main__':
    main()
