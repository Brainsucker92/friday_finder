#!/bin/python3

import datetime


class FridayFinder:
    
    def __init__(self, date):
        self.__date = date
    
    def get_days_to_friday(self):
        weekday = self.__date.weekday()
        return (4 - weekday) % 7
    
    def get_next_friday(self):
        days_to_friday = self.get_days_to_friday()
        return self.__date + datetime.timedelta(days=days_to_friday)
    
    def find_next_friday_13th(self):
        friday = self.get_next_friday()
        while friday.day != 13:
            friday += datetime.timedelta(weeks=1)
        return friday

if __name__ == "__main__":
    today = datetime.date.today()
    finder = FridayFinder(today)
    friday = finder.get_next_friday()
    friday_13th = finder.find_next_friday_13th()
    print("Next friday will be at: " + str(friday))
    print("Next friday the 13th will be at: " + str(friday_13th))
