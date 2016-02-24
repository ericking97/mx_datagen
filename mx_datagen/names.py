# -*- coding: utf-8 -*-
"""Names module"""
from __future__ import unicode_literals
from data_source.names import *
import random


class Name:
    """Names class"""
    @staticmethod
    def first_name(gender=None):
        """Return a first name that can be female or male
        :param gender:
        """
        if gender in ['male', 'Male', 'M', 'Hombre']:
            return random.choice(male_names)
        elif gender in ['female', 'Female', 'F', 'Mujer']:
            return random.choice(female_names)
        elif not gender:
            return random.choice(male_names + female_names)
        else:
            raise ValueError('Please enter one of the following gender options:\n'
                             '* Male    * male      * M     * Hombre\n'
                             '* Female  * female    * F     * Mujer')

    @staticmethod
    def surname(arg=None):
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
            raise ValueError('Please enter one of the following culture options\n'
                             '* common\n'
                             '* mayan\n'
                             '* nahuatl\n'
                             '* yaqui')

    @staticmethod
    def fullname(gender=None, culture=None):
        """Returns a random fullname
        :param gender
        :param culture"""
        if not gender and not culture:
            first_name = random.choice(male_names+female_names)
            paternal_surname = random.choice(surnames+mayan_surnames+nahuatl_surnames+yaqui_surnames)
            maternal_surname = random.choice(surnames+mayan_surnames+nahuatl_surnames+yaqui_surnames)
            fullname = first_name + ' ' + paternal_surname + ' ' + maternal_surname
            return fullname
        elif not gender and culture in ['mayan', 'nahuatl', 'yaqui']:
            first_name = random.choice(male_names+female_names)
            if culture == 'mayan':
                paternal_surname = random.choice(mayan_surnames)
                maternal_surname = random.choice(mayan_surnames)
            elif culture == 'nahuatl':
                paternal_surname = random.choice(nahuatl_surnames)
                maternal_surname = random.choice(nahuatl_surnames)
            elif culture == 'yaqui':
                paternal_surname = random.choice(yaqui_surnames)
                maternal_surname = random.choice(yaqui_surnames)
            fullname = first_name + ' ' + paternal_surname + ' ' + maternal_surname
            return fullname
        elif gender in ['Male', 'M', 'Hombre'] and not culture:
            first_name = random.choice(male_names)
            paternal_surname = random.choice(surnames+mayan_surnames+nahuatl_surnames+yaqui_surnames)
            maternal_surname = random.choice(surnames+mayan_surnames+nahuatl_surnames+yaqui_surnames)
            fullname = first_name + ' ' + paternal_surname + ' ' + maternal_surname
            return fullname
        elif gender in ['Male', 'M', 'Hombre'] and culture in ['mayan', 'nahuatl', 'yaqui']:
            first_name = random.choice(male_names)
            if culture == 'mayan':
                paternal_surname = random.choice(mayan_surnames)
                maternal_surname = random.choice(mayan_surnames)
            elif culture == 'nahuatl':
                paternal_surname = random.choice(nahuatl_surnames)
                maternal_surname = random.choice(nahuatl_surnames)
            elif culture == 'yaqui':
                paternal_surname = random.choice(yaqui_surnames)
                maternal_surname = random.choice(yaqui_surnames)
            fullname = first_name + ' ' + paternal_surname + ' ' + maternal_surname
            return fullname
        elif gender in ['Female', 'F', 'Mujer'] and not culture:
            first_name = random.choice(female_names)
            paternal_surname = random.choice(surnames+mayan_surnames+nahuatl_surnames+yaqui_surnames)
            maternal_surname = random.choice(surnames+mayan_surnames+nahuatl_surnames+yaqui_surnames)
            fullname = first_name + ' ' + paternal_surname + ' ' + maternal_surname
            return fullname
        elif gender in ['Female', 'F', 'Mujer'] and culture in ['mayan', 'nahuatl', 'yaqui']:
            first_name = random.choice(female_names)
            if culture == 'mayan':
                paternal_surname = random.choice(mayan_surnames)
                maternal_surname = random.choice(mayan_surnames)
            elif culture == 'nahuatl':
                paternal_surname = random.choice(nahuatl_surnames)
                maternal_surname = random.choice(nahuatl_surnames)
            elif culture == 'yaqui':
                paternal_surname = random.choice(yaqui_surnames)
                maternal_surname = random.choice(yaqui_surnames)
            fullname = first_name + ' ' + paternal_surname + ' ' + maternal_surname
            return fullname
        elif gender not in ['Male', 'M', 'Hombre', 'Female', 'F', 'Mujer']:
            raise ValueError('Please enter one of the following gender options\n'
                             '* Male        *M      *Hombre\n'
                             '* Female      *F      *Mujer')
        elif culture not in ['mayan', 'nahuatl', 'yaqui']:
            raise ValueError('Please enter one of the following culture options\n'
                             '* mayan\n'
                             '* nahuatl\n'
                             '* yaqui')
