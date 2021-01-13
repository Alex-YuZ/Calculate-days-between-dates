def next_day(year, month, day):
    """
    Calculate the value of next day given a date consisted of year, month and day.
    
    Params:
    -------
        year: int. Value of year given a certain date.
        month: int. Value of month given a certain date.
        day: int. Value of year given a certain date.
        
    Returns:
    --------
        int: Ouptput the value of day
    """
    
    if day < days_in_month(year, month):
        return year, month, day + 1
    
    elif month < 12:
        return year, month + 1, 1
    
    else:
        return year + 1, 1, 1

    
def is_valid_input(year1, month1, day1, year2, month2, day2):
    """
    Check whether the first three args is before the last three in terms
    of input validity.
    
    Params:
    -------
        year1: int. The number of the year as start.
        month1: int. The number of the month as start.
        day1: int. The number of day as start.
        year2: int. The number of the year as end.
        month2: int. The number of the month as end.
        day2: int. The number of day as end.
        
    Returns:
    -------
        boolean: True/False. True is valid for inputs and vice versa.
        
    """
    
    if year1 < year2:
        return True
    
    elif year1 == year2:
        if month1 < month2:
            return True
        
        elif month1 == month2:
            return day1 < day2
        
        return False
    
    return False


def is_leap(year):
    """
    Check a given value of year is a leap year or not.
    
    Params:
    -------
        year: int. The value of a given year.
        
    Returns:
    --------
        boolean: True if the given year is a leap year and vice versa.
    """
    
    if year % 4 == 0:
        if year % 100 == 0:
            return year % 400 == 0
        return True
    return False


def days_in_month(year, month):
    """
    Calculate how many days there are in a given month.
    
    Params:
    -------
        year: int. The value of year for a given date.
        month: int. The value of month for a given date.
        
    Returns:
    -------
        int. For month in [1,3,5,7,8,10,12], return 31 days.
             For month in [4,6,9,11], return 30 days.
             For month of February, return 29 if a leap year, 
             otherwise, return 28 if a common year.
    """
    
    if month in [4, 6, 9, 11]:
        return 30
    elif month == 2:
        if is_leap(year): # check if the given year is a leap or not.
            return 29
        else:
            return 28
    else:
        return 31