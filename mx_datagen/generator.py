# -*- coding: utf-8 -*-
"""Returns functions"""
import names


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
        first_name = names.GenNames().create_first_name('male')
        paternal_surname = names.GenNames().create_surname()
        maternal_surname = names.GenNames().create_surname()
        fullname = first_name + ' ' + paternal_surname + ' ' + maternal_surname
        return fullname

    @staticmethod
    def female_fullname():
        """Returns a female fullname"""
        first_name = names.GenNames().create_first_name('female')
        paternal_surname = names.GenNames().create_surname()
        maternal_surname = names.GenNames().create_surname()
        fullname = first_name + ' ' + paternal_surname + ' ' + maternal_surname
        return fullname

    @staticmethod
    def male_first_name():
        """Returns a male first name"""
        return names.GenNames().create_first_name('male')

    @staticmethod
    def female_first_name():
        """Returns a female first name"""
        return names.GenNames().create_first_name('female')

    @staticmethod
    def first_name():
        """Returns a random first name male/female"""
        return names.GenNames().create_first_name()

    @staticmethod
    def surname(param=None):
        """Returns a random surname, if you want an specific type of surname send it as a param
        :param param:
        """
        if param is None:
            return names.GenNames().create_surname()
        else:
            return names.GenNames().create_surname(param)
