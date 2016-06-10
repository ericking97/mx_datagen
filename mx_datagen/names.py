# -*- coding: utf-8 -*-
"""Names module"""
from __future__ import unicode_literals
import random
import json
import os


class Name():
    """Names class"""
    global data
    route = '%s/data_source/names.json' % os.path.dirname(os.path.realpath(__file__))
    with open(route, 'r') as data_file:
        data = json.load(data_file)

    @staticmethod
    def first_name(gender=None, common=False):
        """Return a first name that can be female or male
        :param gender Choose the gender you want if no gender is send it selects a random name
        :param common If you want common names send true (Less diversity of names)
        """
        if gender in ['male', 'Male', 'M', 'Hombre']:
            if common is True:
                return random.choice(data['Common male names'])
            else:
                return random.choice(data['Male Names'])
        elif gender in ['female', 'Female', 'F', 'Mujer']:
            if common is True:
                return random.choice(data['Common female names'])
            else:
                return random.choice(data['Female Names'])
        elif not gender:
            if common is True:
                return random.choice(data['Common male names'] + data['Common female names'])
            else:
                return random.choice(data['Male Names'] + data['Female Names'])
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
            return random.choice(data['Common Surnames'])
        elif arg == 'mayan':
            return random.choice(data['Mayan Surnames'])
        elif arg == 'nahuatl':
            return random.choice(data['Nahuatl Surnames'])
        elif arg == 'yaqui':
            return random.choice(data['Yaqui Surnames'])
        elif not arg:
            return random.choice(data['Surnames'])
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
            first_name = random.choice(data['Male Names'] + data['Female Names'])
            paternal_surname = random.choice(
                data['Surnames'] + data['Mayan Surnames'] + data['Nahuatl Surnames'] + data['Yaqui Surnames'])
            maternal_surname = random.choice(
                data['Surnames'] + data['Mayan Surnames'] + data['Nahuatl Surnames'] + data['Yaqui Surnames'])
            fullname = first_name + ' ' + paternal_surname + ' ' + maternal_surname
            return fullname
        elif not gender and culture in ['mayan', 'nahuatl', 'yaqui']:
            first_name = random.choice(data['Male Names'] + data['Female Names'])
            if culture == 'mayan':
                paternal_surname = random.choice(data['Mayan Surnames'])
                maternal_surname = random.choice(data['Mayan Surnames'])
            elif culture == 'nahuatl':
                paternal_surname = random.choice(data['Nahuatl Surnames'])
                maternal_surname = random.choice(data['Nahuatl Surnames'])
            elif culture == 'yaqui':
                paternal_surname = random.choice(data['Yaqui Surnames'])
                maternal_surname = random.choice(data['Yaqui Surnames'])
            fullname = first_name + ' ' + paternal_surname + ' ' + maternal_surname
            return fullname
        elif gender in ['Male', 'M', 'Hombre'] and not culture:
            first_name = random.choice(data['Male Names'])
            paternal_surname = random.choice(
                data['Surnames'] + data['Mayan Surnames'] + data['Nahuatl Surnames'] + data['Yaqui Surnames'])
            maternal_surname = random.choice(
                data['Surnames'] + data['Mayan Surnames'] + data['Nahuatl Surnames'] + data['Yaqui Surnames'])
            fullname = first_name + ' ' + paternal_surname + ' ' + maternal_surname
            return fullname
        elif gender in ['Male', 'M', 'Hombre'] and culture in ['mayan', 'nahuatl', 'yaqui']:
            first_name = random.choice(data['Male Names'])
            if culture == 'mayan':
                paternal_surname = random.choice(data['Mayan Surnames'])
                maternal_surname = random.choice(data['Mayan Surnames'])
            elif culture == 'nahuatl':
                paternal_surname = random.choice(data['Nahuatl Surnames'])
                maternal_surname = random.choice(data['Nahuatl Surnames'])
            elif culture == 'yaqui':
                paternal_surname = random.choice(data['Yaqui Surnames'])
                maternal_surname = random.choice(data['Yaqui Surnames'])
            fullname = first_name + ' ' + paternal_surname + ' ' + maternal_surname
            return fullname
        elif gender in ['Female', 'F', 'Mujer'] and not culture:
            first_name = random.choice(data['Female Names'])
            paternal_surname = random.choice(
                data['Surnames'] + data['Mayan Surnames'] + data['Nahuatl Surnames'] + data['Yaqui Surnames'])
            maternal_surname = random.choice(
                data['Surnames'] + data['Mayan Surnames'] + data['Nahuatl Surnames'] + data['Yaqui Surnames'])
            fullname = first_name + ' ' + paternal_surname + ' ' + maternal_surname
            return fullname
        elif gender in ['Female', 'F', 'Mujer'] and culture in ['mayan', 'nahuatl', 'yaqui']:
            first_name = random.choice(data['Female Names'])
            if culture == 'mayan':
                paternal_surname = random.choice(data['Mayan Surnames'])
                maternal_surname = random.choice(data['Mayan Surnames'])
            elif culture == 'nahuatl':
                paternal_surname = random.choice(data['Nahuatl Surnames'])
                maternal_surname = random.choice(data['Nahuatl Surnames'])
            elif culture == 'yaqui':
                paternal_surname = random.choice(data['Yaqui Surnames'])
                maternal_surname = random.choice(data['Yaqui Surnames'])
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
