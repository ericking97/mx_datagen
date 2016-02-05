# -*- coding: utf-8 -*-
"""Dates module"""
import datetime
# TODO: Create Dates module
class Dates:
    """Dates module"""
    @staticmethod
    def create_date(before=None, after=None):
        if before is None and after is None:
            datetime.datetime.time()