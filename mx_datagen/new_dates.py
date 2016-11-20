# -*- coding: utf-8 -*-
"""Dates module"""
from datetime import timedelta, date, datetime
from random import randint, choice


class Dates:
    """Dates class"""
    @staticmethod
    def create_date(limit=10, before=None, after=None):
        """Creates a date in YYYY-MM-DD format
        :param limit Years of difference today can have with the generated
                     (Default 10 years)
        :param before Generates a date before a given date
        :param after Generates a date after a given date"""
        max_days = limit * 365
        if not before and not after:
            today = date.today()
            days = timedelta(days=randint(1, max_days))
            if choice(['-', '+']) == '+':
                return today + days
            else:
                return today - days
        elif before and not after:
            try:
                pre_date = datetime.strptime(before, "%Y-%m-%d").date()
            except ValueError:
                raise ValueError("Date format must be YYYY-MM-DD")
            available = pre_date - date(0001, 01, 01)
            days = timedelta(days=randint(1, max_days))
            if days > available:
                days = timedelta(days=randint(0, available.days))
            return pre_date - days
        elif not before and after:
            try:
                post_date = datetime.strptime(after, "%Y-%m-%d").date()
            except ValueError:
                raise ValueError("Date format must be YYYY-MM-DD")
            days = timedelta(days=randint(1, max_days))
            return post_date + days
        elif before and after:
            try:
                pre_date = datetime.strptime(before, "%Y-%m-%d").date()
                post_date = datetime.strptime(after, "%Y-%m-%d").date()
            except ValueError:
                raise ValueError("Date format must be YYYY-MM-DD")
            if pre_date <= post_date:
                raise Exception("Before date must be greater than after")
            difference = pre_date - post_date
            days = timedelta(days=randint(0, difference.days))
            if choice(['-', '+']) == '+':
                return pre_date - days
            else:
                return post_date + days
        else:
            raise ValueError("Unexpected error")

    @staticmethod
    def create_date_old(year):
        if type(year) is int and year is not 0:
            today = date.today()
            print today - timedelta(days=year*365)

Dates.create_date_old(18)
