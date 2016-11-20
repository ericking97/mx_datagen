# -*- coding: utf-8 -*-
"""Names module"""
from random import choice

import json
import constants as c


class Name():
    """Generates names"""
    def __init__(self):
        with open(c.ROOT + '/data_source/info_names.json', 'r') as jfile:
            self.data = json.load(jfile)

    def firstname(self, gender=None, common=False):
        """Returns a first name
        :param gender
        :param common"""
        if gender in c.MALES:
            if common is True:
                return choice(self.data['Common Male Names'])
            else:
                return choice(self.data['Male Names'])
        elif gender in c.FEMALES:
            if common is True:
                return choice(self.data['Common Female Names'])
            else:
                return choice(self.data['Female Names'])
        elif gender not in c.MALES and gender not in c.FEMALES:
            if common is True:
                return choice(self.data['Common Male Names'] +
                              self.data['Common Female Names'])
            else:
                return choice(self.data['Male Names'] +
                              self.data['Female Names'])

    def surname(self, culture=None):
        """Returns a surname
        :param surname"""
        if culture in c.CULTURES:
            return choice(self.data[culture])
        else:
            return choice(self.data['Common'] +
                          self.data['Mayan'] +
                          self.data['Nahuatl'] +
                          self.data['Yaqui'])
