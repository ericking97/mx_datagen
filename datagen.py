# -*- coding: utf-8 -*-
"""Returns functions"""
from personal.names import Names

Name = Names()

class Datagen():
    """Datagenerator class"""

    def female_fullname(self):
        """Return female fullname"""
        first_name = Name.create_female_first_name()
        paternal_surname = Name.create_surname()
        maternal_surname = Name.create_surname()
        fullname = first_name + ' ' + paternal_surname + ' ' + maternal_surname
        return fullname

    def male_fullname(self):
        """Return male fullname"""
        first_name = Name.create_female_first_name()
        paternal_surname = Name.create_surname()
        maternal_surname = Name.create_surname()
        fullname = first_name + ' ' + paternal_surname + ' ' + maternal_surname
        return fullname

    def female_first_name(self):
        """Returns female first name"""
        return Name.create_female_first_name()

    def male_first_name(self):
        """Returns male first name"""
        return Name.create_male_first_name()

    def first_name(self):
        """Returns randomly a first name"""
        return Name.create_first_name()

    def surname(self):
        """Return randomly a surname"""
        return Name.create_surname()
