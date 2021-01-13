from cal_days_helper import is_valid_input, next_day, is_leap, days_in_month

def days_between_dates(year1, month1, day1, year2, month2, day2):
    """
    Calculate how many days there are between two given dates.
    
    Params:
    -------
        year1: int. The number of the year as start.
        month1: int. The number of the month as start.
        day1: int. The number of day as start.
        year2: int. The number of the year as end.
        month2: int. The number of the month as end.
        day2: int. The number of day as end.
        
    Returns:
    --------
        int: Return the days between two given dates.
        
    Raise AssertionError if the input dates are invalid.
    """
    
    # if the start date is the same as end date, return 0
    assert not is_valid_input(year2, month2, day2, year1, month1, day1)
    days = 0
    while is_valid_input(year1, month1, day1, year2, month2, day2):
        year1, month1, day1 = next_day(year1, month1, day1)
        days += 1
        
    return days


if __name__ == '__main__':
    dates = input("Please enter two dates (using comma as delimiter): ").split(',')
    year1, month1, day1, year2, month2, day2 = map(int, dates)
    output = "The days between {1}/{2}/{3} and {4}/{5}/{6} are {0} days.".format(days_between_dates(year1, month1, day1, year2, month2, day2), year1, month1, day1, year2, month2, day2)
    print("\n{:=^50}".format("OUTPUT"))
    print('\n', output, sep='', end='\n\n')