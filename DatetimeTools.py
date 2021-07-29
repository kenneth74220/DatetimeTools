from datetime import datetime, timedelta

def week_range(date: datetime, first_day: 'set the first day. Default is 7(Sun).'=7) \
        -> 'Start and end of week data.':
    '''
    Return start and end of week data from a given date.
    It can set the first day of the week.
    '''

    # isocalendar calculates the year, week of the year, and day of the week.
    # dow is Mon = 1, Sat = 6, ..., Sun = 7
    FIRST_DAY = first_day
    year, week, dow = date.isocalendar()

    # Find the first day of the week.
    if dow == 7:
        # Since we want to start with Sunday, let's test for that condition.
        start_date = date
    else:
        # Otherwise, subtract `dow` number days to get the first day
        start_date = date - timedelta(dow)

    # Now, add 6 for the last day of the week:
    end_date = start_date + timedelta(6)

    # Shift FIRST_DAY:
    if (start_date + timedelta(FIRST_DAY)) <= date:
        start_date += timedelta(FIRST_DAY)
        end_date   += timedelta(FIRST_DAY)
    else:
        start_date -= timedelta(7-FIRST_DAY)
        end_date   -= timedelta(7-FIRST_DAY)

    return start_date, end_date


if __name__ == '__main__':
    print (week_range.__annotations__)
    for days in range(0, 30):
    #if True:
        now = datetime.now().date() + timedelta(days=days)
        #now  = datetime(2021, 3, 29)
        yaha = week_range(now, first_day=5)
        print (now, yaha)
