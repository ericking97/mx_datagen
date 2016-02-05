# -*- coding: utf-8 -*-
"""Names module"""
from __future__ import unicode_literals
from .data_source.names import *
import random

class GenNames:
    """Names class"""
    @staticmethod
    def create_first_name(arg=None):
        """Return a First name that can be female or masculin
        :param arg:
        """
        if arg in ['male', 'Male', 'M']:
            return random.choice(male_names)
        elif arg in ['female', 'Female', 'F']:
            return random.choice(female_names)
        else:
            return random.choice(male_names + female_names)


    @staticmethod
    def create_surname(arg=None):
        """Return a complete random surname
        :param arg:
        """
        if arg == 'common':
            return random.choice(surnames)
        elif arg == 'mayan':
            return random.choice(mayan_surnames)
        elif arg == 'nahuatl':
            return random.choice(nahuatl_surnames)
        elif arg == 'yaqui':
            return random.choice(yaqui_surnames)
        elif not arg:
            return random.choice(surnames + mayan_surnames + nahuatl_surnames + yaqui_surnames)
        else:
            raise ValueError('Not valid arg')