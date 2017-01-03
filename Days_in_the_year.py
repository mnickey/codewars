import calendar


def year_days(year):
    if calendar.isleap(year):
        return '{} has 366 days'.format(year)
    else:
        return '{} has 365 days'.format(year)
