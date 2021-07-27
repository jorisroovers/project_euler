########################################################################################################################
# Problem 19
########################################################################################################################
# You are given the following information, but you may prefer to do some research for yourself.

# 1 Jan 1900 was a Monday.
# Thirty days has September,
# April, June and November.
# All the rest have thirty-one,
# Saving February alone,
# Which has twenty-eight, rain or shine.
# And on leap years, twenty-nine.
# A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
########################################################################################################################
# NOTES
# - This problem is obviously much more easily solvable by using python's standard library, but that defeats the purpose
# - The solution asks for counting Sunday's from 190*1*, while the description starts from Monday Jan 1, 190*0*.
#   This means you need to start iterating through days from 1900-01-01 to get the correct weekdays, but only start
#   counting Sundays from 1901 onwards.
########################################################################################################################

def is_leap_year(year):
    is_leap = (year % 4 == 0)
    if is_leap:
        is_century = (year % 100 == 0)
        if is_century:
            return (year % 400 == 0)
    return is_leap

def run(args):

    sundays_on_first = 0

    # day, month, year. month offset by 1 to make it indexable in months array
    current_date = [1, 0, 1900]
    end_date = [31, 11, 2000]
    
    day_of_week = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    day_of_week_index = 0
    months_length = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    while current_date != end_date:
        # print(day_of_week[day_of_week_index], current_date)

        # increment date, deal with leap years
        if current_date[1] == 1 and is_leap_year(current_date[2]):
            month_length = 29
            # print("LEAP MONTH", day_of_week[day_of_week_index], current_date)
        else:
            month_length = months_length[current_date[1]]

        if current_date[0] < month_length:
            current_date[0] += 1
        else: #  end of month
            if current_date[1] < 11:
                current_date[0] =  1
                current_date[1] += 1
            else: # end of year
                current_date =  [1, 0, current_date[2]+1]

        # increment weekday
        day_of_week_index = (day_of_week_index + 1) % len(day_of_week)

        # count Sunday's on first day of month, solution asks for starting from 1901 onwards
        if current_date[2] > 1900 and current_date[0] == 1 and day_of_week_index == 6:
            sundays_on_first += 1

    print("Sundays of first day of month", sundays_on_first)
