# -*- coding: utf-8 -*-
"""This generator file is the core of the project"""
import random
from .email import Emails
from .data_source.ladas import *
from .names import GenNames

class Name:
    """Name module
    Methods:
        *male_fullname
        *female_fullname
        *male_first_name
        *female_first_name
        *first_name
        *surname"""

    @staticmethod
    def male_fullname():
        """Returns a male fullname"""
        first_name = GenNames.create_first_name('male')
        paternal_surname = GenNames.create_surname()
        maternal_surname = GenNames.create_surname()
        fullname = first_name + ' ' + paternal_surname + ' ' + maternal_surname
        return fullname

    @staticmethod
    def female_fullname():
        """Returns a female fullname"""
        first_name = GenNames.create_first_name('female')
        paternal_surname = GenNames.create_surname()
        maternal_surname = GenNames.create_surname()
        fullname = first_name + ' ' + paternal_surname + ' ' + maternal_surname
        return fullname

    @staticmethod
    def male_first_name():
        """Returns a male first name"""
        return GenNames.create_first_name('male')

    @staticmethod
    def female_first_name():
        """Returns a female first name"""
        return GenNames.create_first_name('female')

    @staticmethod
    def first_name():
        """Returns a random first name male/female"""
        return GenNames.create_first_name()

    @staticmethod
    def surname(param=None):
        """Returns a random surname, if you want an specific type of surname send it as a param
        :param param:
        """
        if param is None:
            return GenNames.create_surname()
        else:
            return GenNames.create_surname(param)


class Phone:
    """Phone module"""
    @staticmethod
    def create_phone(args=None):
        """Returns a phone number"""
        if args is None:
            base = random.choice(base_numbers)
            if len(base) is 2:
                phone = base + str(random.randint(11111111, 99999999))
            elif len(base) is 3:
                phone = base + str(random.randint(1111111, 9999999))
            return phone
        else:
            status = args in base_numbers
            if status is True:
                if len(args) is 2:
                    phone = args + str(random.randint(11111111, 99999999))
                elif len(args) is 3:
                    phone = args + str(random.randint(1111111, 9999999))
                return phone
            else:
                return "La lada que mandaste no es valida"

class Email:
    """Email module"""
    @staticmethod
    def create_email(args=None):
        """Returns an email, arg only if you want to make an email from an alias Ex:'your-email+123@gmail.com' """
        if args is None:
            return Emails.random_email()
        else:
            return Emails.alias_email(args)
