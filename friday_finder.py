#!/bin/python3

import datetime


class FridayFinder:
    
    @staticmethod
    def get_days_to_friday(date):
        return (4 - date.weekday()) % 7
    
    @staticmethod
    def get_next_friday(date):
        days_to_friday = FridayFinder.get_days_to_friday(date)
        return date + datetime.timedelta(days=days_to_friday)
    
    @staticmethod
    def find_next_friday_13th(date):
        friday = FridayFinder.get_next_friday(date)
        while friday.day != 13:
            friday += datetime.timedelta(weeks=1)
        return friday

if __name__ == "__main__":
    today = datetime.date.today()
    friday = FridayFinder.get_next_friday(today)
    friday_13th = FridayFinder.find_next_friday_13th(today)
    print("Next friday will be at: " + str(friday))
    print("Next friday the 13th will be at: " + str(friday_13th))
