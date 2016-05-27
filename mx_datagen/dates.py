# -*- coding: utf-8 -*-
"""Dates module"""
from __future__ import unicode_literals
from dateutil.relativedelta import relativedelta
import datetime
import random


class Date:
    """Dates module"""
    @staticmethod
    def create_date(after=None, before=None):
        """Returns a date between 2 dates
        :param before
        :param after"""
        if not before and not after:
            now = datetime.datetime.now()
            days = datetime.timedelta(days=int(random.random() * 1000))
            stt = random.choice(['+', '-'])
            if stt is '+':
                date = now + days
            elif stt is '-':
                date = now - days
            return date.strftime('%Y-%m-%d')
        elif before and not after:
            try:
                now = datetime.datetime.strptime(before, '%Y-%m-%d')
            except ValueError:
                raise ValueError('Invalid date format, should be YYYY-MM-DD')
            days = datetime.timedelta(days=int(random.random() * 1000))
            date = now - days
            return date.strftime('%Y-%m-%d')
        elif before is None and after is not None:
            try:
                now = datetime.datetime.strptime(after, '%Y-%m-%d')
            except ValueError:
                raise ValueError('Invalid date format, should be YYYY-MM-DD')
            days = datetime.timedelta(days=int(random.random() * 1000))
            date = now + days
            return date.strftime('%Y-%m-%d')
        elif before is not None and after is not None:
            try:
                bef = datetime.datetime.strptime(before, '%Y-%m-%d')
                aft = datetime.datetime.strptime(after, '%Y-%m-%d')
            except ValueError:
                raise ValueError('Invalid date format, should be YYYY-MM-DD')
            difference = bef - aft
            days = datetime.timedelta(days=random.randint(1, difference.days - 1))
            stt = random.choice(['+', '-'])
            if stt == '+':
                date = aft + days
            elif stt == '-':
                date = bef - days
            return date.strftime('%Y-%m-%d')
        else:
            raise ValueError('Unexpected error')

    @staticmethod
    def create_date_old(year):
        """Returns a date before or after params years
        :param year"""
        if type(year) == int and year is not 0:
            now = datetime.datetime.now()
            mins = now + relativedelta(years=-year - 1, days=1)
            days = datetime.timedelta(days=random.randint(0, 364))
            date = mins + days
            return date.strftime('%Y-%m-%d')
        elif year == 0:
            now = datetime.datetime.now()
            mins = now - relativedelta(days=364)
            days = datetime.timedelta(days=random.randint(0, 364))
            date = mins + days
            return date.strftime('%Y-%m-%d')
        else:
            raise ValueError('Expected int object, got ', type(year))

    @staticmethod
    def create_age_between(min, max):
        """Returns a random date with age between two ages
        :param min
        :param max"""
        if type(min) is int and type(max) is int:
            if min < max:
                now = datetime.datetime.now()
                mins = now + relativedelta(years=-min - 1, days=1)
                maxs = now + relativedelta(years=-max - 1, days=1)
                dif = mins - maxs
                days = datetime.timedelta(days=random.randint(0, dif.days))
                date = maxs + days
                return date.strftime('%Y-%m-%d')
            else:
                raise ValueError('Please send before age as first arg, and after age as second arg')
        else:
            raise ValueError('Expected int objects, got ', type(min), ' and ', type(max))

    @staticmethod
    def next_payment_day(pivot=None):
        """Calculates the next payment date
        :param pivot"""
        if not pivot:
            now = datetime.datetime.now()
            if now.day < 15:
                now += datetime.timedelta(days=(15 - now.day))
            elif now.day >= 15:
                if now.month in [1, 3, 5, 7, 8, 10, 12]:
                    if now.day == 31:
                        now += datetime.timedelta(days=15)
                    else:
                        now += datetime.timedelta(days=(31 - now.day))
                elif now.month == 2:
                    if now.year % 4 == 0:
                        if now.day == 29:
                            now += datetime.timedelta(days=15)
                        else:
                            now += datetime.timedelta(days=(29 - now.day))
                    else:
                        if now.day == 28:
                            now += datetime.timedelta(days=15)
                        else:
                            now += datetime.timedelta(days=(28 - now.day))
                else:
                    if now.day == 30:
                        now += datetime.timedelta(days=15)
                    else:
                        now += datetime.timedelta(days=(30 - now.day))
            return datetime.datetime.strftime(now, '%Y-%m-%d')
        elif pivot:
            try:
                pivot_date = datetime.datetime.strptime(pivot, '%Y-%m-%d')
            except ValueError:
                raise ValueError('Invalid date format, should be YYYY-MM-DD')
            now = datetime.datetime.now()
            if now > pivot_date:
                while pivot_date < now:
                    pivot_date += datetime.timedelta(days=14)
            elif now < pivot_date:
                while pivot_date > now:
                    pivot_date -= datetime.timedelta(days=14)
                pivot_date += datetime.timedelta(days=14)
            else:
                raise ValueError('Unexpected pivot day')
            return datetime.datetime.strftime(pivot_date, '%Y-%m-%d')
        else:
            raise ValueError('Please enter a string object')

    @staticmethod
    def last_payment_day(pivot=None):
        """Calculates the last payment date
        :param pivot"""
        if not pivot:
            now = datetime.datetime.now()
            if now.day <= 15:
                now -= datetime.timedelta(days=(15 - (15 - now.day)))
            elif now.day > 15:
                if now.month in [1, 3, 5, 7, 8, 10, 12]:
                    if now.day == 31:
                        pass
                    else:
                        now -= datetime.timedelta(days=now.day - 15)
                elif now.month in [4, 6, 9, 11]:
                    if now.day == 30:
                        pass
                    else:
                        now -= datetime.timedelta(days=now.day - 15)
                elif now.month == 2:
                    if now.year % 4 == 0:
                        if now.day == 29:
                            pass
                        else:
                            now -= datetime.timedelta(days=now.day - 15)
                    else:
                        if now.day == 28:
                            pass
                        else:
                            now -= datetime.timedelta(days=now.day-15)
            return datetime.datetime.strftime(now, '%Y-%m-%d')
        elif pivot:
            try:
                pivot_date = datetime.datetime.strptime(pivot, '%Y-%m-%d')
            except ValueError:
                raise ValueError('Invalid date format, should be YYYY-MM-DD')
            now = datetime.datetime.now()
            if now > pivot_date:
                while pivot_date < now:
                    pivot_date += datetime.timedelta(days=14)
                pivot_date -= datetime.timedelta(days=14)
            elif now < pivot_date:
                while pivot_date > now:
                    pivot_date -= datetime.timedelta(days=14)
            else:
                raise ValueError('Unexpected pivot day')
            return datetime.datetime.strftime(pivot_date, '%Y-%m-%d')
        else:
            raise ValueError('Please enter a string object')
