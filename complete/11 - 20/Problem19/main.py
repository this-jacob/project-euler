import time

def main():

    start_time = time.time()

    total = 0

    daysInMonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    weekday = 1
    leap = False

    #Iterate through the years
    for year in range(1901, 2001):

        #check for leap year    -- flags leap as true if it is a leap year
        if year % 1000 == 0:
            if year % 400 == 0:
                leap = True
        else:
            if year % 4 == 0:
                leap = True

        #give feb one more day if it is a leap year
        if leap:
            daysInMonth[1] += 1

        #go through the months
        for month in range(0, 12):
            #go through the days
            for day in range(1, daysInMonth[month] + 1):

                print month , day , weekday

                if day == 1 and weekday == 6:
                    total += 1

                weekday += 1

                if weekday > 6:
                    weekday = 0

        #reset the leap year
        if leap:
            daysInMonth[1] -= 1

        leap = False


    #print the totals
    print total
    print time.time() - start_time

if __name__ == '__main__':
    main()
