# -*- coding: utf-8 -*-
"""Company module"""
from __future__ import unicode_literals
from data_source.company import *

import random


class Company:
    """Company class"""
    @staticmethod
    def random(sufixed=False):
        """Returns a basic name of a company,
         choose if you want it to have a sufix
         :param sufixed"""
        pre = random.choice(prefix)
        des = random.choice(description)
        act = random.choice(activity)
        if sufixed:
            suf = random.choice(sufix)
            full_company = pre+' '+des+' '+act+' '+suf
        elif not sufixed:
            full_company = pre+' '+des+' '+act
        return full_company
