#!/bin/python3

import datetime

def get_next_friday(date):
    days_to_friday = (4 - date.weekday()) % 7
    return date + datetime.timedelta(days=days_to_friday)

def find_next_friday_13th(date):
    friday = get_next_friday(date)
    while friday.day != 13:
        friday += datetime.timedelta(weeks=1)
    return friday

if __name__ == "__main__":
    today = datetime.date.today()
    friday = get_next_friday(today)
    friday_13th = find_next_friday_13th(today)
    print("Next friday will be at: " + str(friday))
    print("Next friday the 13th will be at: " + str(friday_13th))
