# -*- coding: utf-8 -*-
"""Names module"""
import random
from .data_source.names import *


class GenNames:
    """Names class"""
    @staticmethod
    def create_first_name(arg=None):
        """Return a male name
        :param arg:
        """
        if arg is 'male' or arg is 'Male' or arg is 'M':
            first_name = random.choice(male_names)
        elif arg is 'female' or arg is 'Female' or arg is 'F':
            first_name = random.choice(female_names)
        else:
            first_name = random.choice(male_names + female_names)
        return first_name

    @staticmethod
    def create_surname(arg=None):
        """Return a complete random surname
        :param arg:
        """
        if arg is 'common':
            surname = random.choice(surnames)
        elif arg is 'mayan':
            surname = random.choice(mayan_surnames)
        elif arg is 'nahuatl':
            surname = random.choice(nahuatl_surnames)
        elif arg is 'yaqui':
            surname = random.choice(yaqui_surnames)
        else:
            surname = random.choice(surnames + mayan_surnames + nahuatl_surnames + yaqui_surnames)
        return surname
