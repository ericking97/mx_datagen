# -*- coding: utf-8 -*-
"""Zipping module"""
from random import choice

import json
import constants as c


class PostalCode():
    """Zipping class"""
    def __init__(self):
        """Default init function"""
        with open(c.ROOT + '/data_source/Codes.json', 'r') as jfile:
            self.data = json.load(jfile)

    def random(self, info=None):
        """Returns a random zip
        :param info """
        if not info:
            return choice(self.data)['ZIP']
        elif info == 'Basic':
            option = choice(self.data)
            entry = {'ZIP': option['ZIP'],
                     'State': option['State'],
                     'Municipality': option['Municipality'],
                     'Settlement': option['Settlement']}
            return entry
        elif info == 'All':
            option = choice(self.data)
            return option

    def info(self, code, all_inf=False):
        """Send a postal code to return the information about it
        :param zip"""
        states = []
        municipality = []
        settlements = []
        city = []
        type_settlement = []
        number_settlement = []
        for item in self.data:
            if item['ZIP'] == code:
                state = item['State']
                municipality = item['Municipality']
                settlement = item['Settlement']    
                states.append(item['State'])
                municipality.append(item['Municipality'])
                settlements.append(item['Settlement'])
                if all_inf is True:
                    city.append(item['City'])
                    type_settlement.append(item['Type of Settlement'])
                    number_settlement.append(item['Number of Settlement'])
        for x in range(0, len(states)):
            print states[x], municipality[x], city[x], type_settlement[x], settlements[x], number_settlement[x]

# print PostalCode().random()
# print PostalCode().random('Basic')
# print PostalCode().random('All')
PostalCode().info('24026', True)
#PostalCode().info('57170', True)
