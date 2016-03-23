# -*- encode: utf-8 -*-
"""Phone module"""
from __future__ import unicode_literals
from data_source.ladas import *
import random


class Phone:
    """Phones module"""
    @staticmethod
    def random():
        """Returns a random phone"""
        base = random.choice(base_numbers)
        if len(base) == 2:
            phone = base + str(random.randint(11111111, 99999999))
        elif len(base) == 3:
            phone = base + str(random.randint(1111111, 9999999))
        return phone

    @staticmethod
    def lada_phone(lada=None):
        """Returns a phone with the lada you send
        :param lada """
        if lada is not None:
            status = lada in base_numbers
            if status is True:
                if len(lada) == 2:
                    phone = lada + str(random.randint(11111111, 99999999))
                elif len(lada) == 3:
                    phone = lada + str(random.randint(1111111, 9999999))
                return phone
            else:
                raise ValueError('Invalid lada, check if your lada is here', base_numbers)
        elif lada is None:
            raise ValueError('Please check ladas list in docs')

    @staticmethod
    def company():
        """Returns a phone company"""
        return random.choice(companies)