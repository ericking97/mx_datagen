# -*- coding: utf-8 -*-
"""Names module"""

from __future__ import unicode_literals
import random

from .data_source.names import *

class GenNames:
    """Names class"""
    @staticmethod
    def create_first_name(arg=None):
        """Return a First name that can be female or masculin
        :param arg:
        """
        if arg in ['male', 'Male', 'M']:
            return random.choice(male_names)
        if arg in ['female', 'Female', 'F']:
            return random.choice(female_names)

        return random.choice(male_names + female_names)

    @staticmethod
    def create_surname(arg=None):
        """Return a complete random surname
        :param arg:
        """

        if not arg:
          return random.choice(surnames + mayan_surnames + nahuatl_surnames + yaqui_surnames)

        if arg not in ['common', 'mayan', 'nahuatl', 'yaqui']:
          raise ValueError('arg is not valid')

        if arg is 'common':
            return random.choice(surnames)
        if arg is 'mayan':
            return random.choice(mayan_surnames)
        elif arg is 'nahuatl':
            return random.choice(nahuatl_surnames)
        elif arg is 'yaqui':
            return random.choice(yaqui_surnames)