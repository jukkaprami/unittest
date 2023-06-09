# TOOLS FOR DATE AND TIME CALCULATIONS
# ====================================

# LIBARARIES AND MODULES
import datetime # Python's internal date-time library

def datediff(d1, d2):
    """Calculates the difference between two dates in days

    Args:
        d1 (str): A date in ISO format YYYY-MM-DD
        d2 (str): A date in ISO format YYYY-MM-DD

    Returns:
        int: absolute differnce in days
    """
    d1 = datetime.datetime.strptime(d1, "%Y-%m-%d")
    d2 = datetime.datetime.strptime(d2, "%Y-%m-%d")
    difference = abs((d2 - d1).days)
    units = 'days'
    DifferenceData = (difference, units)
    return DifferenceData

def timediff(t1, t2):
    """Calculates the difference between two time values

    Args:
        t1 (str): time value in format hh:mm:ss
        t2 (str): time value in format hh:mm:ss

    Returns:
        float: time difference in hours
    """
    t1 = datetime.datetime.strptime(t1, "%H:%M:%S")
    t2 = datetime.datetime.strptime(t2, "%H:%M:%S")

    # To get absolute value check if t2 is greater than t1
    if t2 > t1:
        # Function calcultates a timedelta which supports only seconds or microseconds
        seconds = abs((t2 - t1).seconds)
    else:
        seconds = abs((t1-t2).seconds)
    
    hours = seconds / 3600 # minute 60 seconds, hour 60 minutes
    return hours

def dateTimeDiff(start, end):
    """Returns difference between two moments

    Args:
        start (str): date time value in format YYYY-MM-dd hh:mm:ss
        end (str): date time value in format YYYY-MM-dd hh:mm:ss

    Returns:
        float: difference in hours
    """
    v1 = datetime.datetime.strptime(start, "%Y-%m-%d %H:%M:%S")
    v2 = datetime.datetime.strptime(end, "%Y-%m-%d %H:%M:%S")
    difference = v2 -v1

    # Total_seconds calculates also seconds in the date part of dates
    seconds = difference.total_seconds()
    hours = seconds / 3600
    return hours

def datediff2(d1, d2, unit):
    """Returns difference between 2 dates in chosen unit (day, month or year)

    Args:
        d1 (str): 1 st date in ISO format (YYYY-mm-dd)
        d2 (str): 2 nd date in ISO format (YYYY-mm-dd)
        unit (str): unit to return

    Returns:
        float: diffrence between dates in desired units
    """
    d1 = datetime.datetime.strptime(d1, "%Y-%m-%d")
    d2 = datetime.datetime.strptime(d2, "%Y-%m-%d")
    difference = abs((d2 - d1).days) # Timedelta in days
    units = {'day':1, 'year': 365, 'month': 30} # Dictionary for unit dividers
    divider = units[unit] # Choose by unit argument
    value = round(difference / divider , 1)
    return value

def timediff2(startTime, endTime, unit):
    """Calculates the difference between two time values in chosen unit (hour, minute or second)

    Args:
        startTime (str): time value in format hh:mm:ss
        endTime (str): time value in format hh:mm:ss
        unit (str): unit to return (second, minute, hour)
    Returns:
        float: time difference in chosen units
    """
    startTime = datetime.datetime.strptime(startTime, "%H:%M:%S")
    endTime = datetime.datetime.strptime(endTime, "%H:%M:%S")
    units = {'hour': 3600, 'minute': 60, 'second': 1}
    seconds = abs((endTime - startTime).seconds)
    divider = units[unit] # Choose divider according to unit argument
    value = seconds / divider
    return value

def dateTimeDiff2(start, end, unit):
    """Calculates difference between date time values in given units

    Args:
        start (str): date time value in format YYYY-MM-dd hh:mm:ss
        end (str): date time value in format YYYY-MM-dd hh:mm:ss
        unit (str): name of time unit: day, hour, minute or second

    Returns:
        float: difference in given units
    """
    v1 = datetime.datetime.strptime(start, "%Y-%m-%d %H:%M:%S")
    v2 = datetime.datetime.strptime(end, "%Y-%m-%d %H:%M:%S")
    difference = v2 -v1
    units = {'day':86400, 'hour': 3600, 'minute': 60, 'second': 1}
    divider = units[unit]
    # Total_seconds calculates also seconds in the date part of dates
    seconds = difference.total_seconds()
    value = seconds / divider
    return value

def finnishWeekdayOrder(weekday):
    weekdayNumber = {'maanantai': 1, 'tiistai': 2, 'keskiviikko' : 3,
     'torstai' : 4, 'perjantai': 5, 'lauantai': 6, 'sunnuntai': 7}
    try:
        value = f'{weekday} on viikon {weekdayNumber[weekday]}. päivä'
    except Exception as error:
        value = f'{weekday} ei ole viikonpäivä, tarkista syötteesi'
    return value
    

    

if __name__ == "__main__":
    
    # Let's test date difference
    date1 = '2023-03-21'
    date2 = '2023-03-17'

    ero = datediff2(date1, date2, 'day')
    print('ero oli', ero, 'päivää')

    # Let's test time difference
    time1 = '10:00:00'
    time2 = '15:25:00'
    ero = timediff2(time1, time2, 'minute')
    print('ero oli', ero, 'minuuttia')

    print(dateTimeDiff('2023-04-28 10:00:00', '2023-04-29 11:00:00'), 'on v1')

