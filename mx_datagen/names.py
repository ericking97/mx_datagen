# -*- coding: utf-8 -*-
"""Names module"""
<<<<<<< HEAD
import random
from .data_source.names import *
=======

from __future__ import unicode_literals
import random
>>>>>>> 8cc28ad05ab71722baca34f0a1aab7e4812ca047

from .data_source.names import *

class GenNames:
    """Names class"""
    @staticmethod
    def create_first_name(arg=None):
        """Return a First name that can be female or masculin
        :param arg:
        """
<<<<<<< HEAD
        if arg is 'male' or arg is 'Male' or arg is 'M':
            first_name = random.choice(male_names)
        elif arg is 'female' or arg is 'Female' or arg is 'F':
            first_name = random.choice(female_names)
        else:
            first_name = random.choice(male_names + female_names)
        return first_name
=======
        if arg in ['male', 'Male', 'M']:
            return random.choice(male_names)
        if arg in ['female', 'Female', 'F']:
            return random.choice(female_names)

        return random.choice(male_names + female_names)
>>>>>>> 8cc28ad05ab71722baca34f0a1aab7e4812ca047

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
