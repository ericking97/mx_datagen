# -*- coding: utf-8 -*-
"""Address module"""
import json
import random
import os

from collections import Counter


class PostalCode:
    """Class address"""
    global data

    route = '%s/data_source/CP.json' % os.path.dirname(os.path.realpath(__file__))
    with open(route, 'r') as data_file:
        data = json.load(data_file)

    @staticmethod
    def random(info=None):
        """Returns a random postal code
        :param info"""
        number = random.randint(0, 145954)
        postal_code = data['Postal Code'][number]
        if not info:
            return postal_code
        elif info == 'Basic':
            colony = data['Colony'][number]
            municipality = data['Municipality'][number]
            state = data['State'][number]
            city = data['City'][number]
            return postal_code, colony, municipality, city, state
        elif info == 'All':
            colony = data['Colony'][number]
            municipality = data['Municipality'][number]
            state = data['State'][number]
            city = data['City'][number]
            col_type = data['Type of Colony'][number]
            col_number = data['Colony number'][number]
            return postal_code, col_type, colony, municipality, city, state, col_number
        else:
            raise ValueError('Please enter one of the following param\n'
                             '* Basic       * All')

    @staticmethod
    def get_info(postal_code, *info):
        """Returns the info from a postal code
        :param postal_code
        :param info"""
        if postal_code in data['Postal Code']:
            counter = Counter(data['Postal Code'])
            if counter[postal_code] == 1:
                number = data['Postal Code'].index(postal_code)
                if not info:
                    colony = data['Colony'][number]
                    municipality = data['Municipality'][number]
                    state = data['State'][number]
                    city = data['City'][number]
                    col_type = data['Type of Colony'][number]
                    col_number = data['Colony number'][number]
                    return col_type, colony, municipality, city, state, col_number
                elif len(info) == 1:
                    if info[0] == 'Basic':
                        colony = data['Colony'][number]
                        municipality = data['Municipality'][number]
                        state = data['State'][number]
                        return colony, municipality, state
                    elif info[0] in ['Colony', 'Municipality', 'State', 'Type of Colony', 'Colony number']:
                        return data[info[0]][number]
                    else:
                        raise ValueError("Please enter a true info param here's the list of valid params\n"
                                         "* Colony\n"
                                         "* Municipality\n"
                                         "* State\n"
                                         "* Type of Colony\n"
                                         "* Colony number")
                else:
                    ndata = []
                    for x in range(0, len(info)):
                        if info[x] in ['Colony', 'Municipality', 'State', 'Type of Colony', 'Colony number']:
                             ndata.append(data[info[x]][number])
                        else:
                            raise ValueError("Please enter a true info param here's the list of valid params\n"
                                             "* Colony\n"
                                             "* Municipality\n"
                                             "* State\n"
                                             "* Type of Colony\n"
                                             "* Colony number")
                    return ndata
            else:
                number = data['Postal Code'].index(postal_code)
                nums = counter[postal_code]
                colonies = []
                col_types = []
                col_numbers = []
                if not info:
                    for x in range(0, nums):
                        colonies.append(data['Colony'][number+x])
                        col_types.append(data['Type of Colony'][number+x])
                        col_numbers.append(data['Colony number'][number+x])
                    municipality = data['Municipality'][number]
                    state = data['State'][number]
                    city = data['City'][number]
                    return col_types, colonies, municipality, state, city, col_numbers
                elif len(info) == 1:
                    if info[0] == 'Basic':
                        for x in range(0, nums):
                            colonies.append(data['Colony'][number+x])
                        municipality = data['Municipality'][number]
                        state = data['State'][number]
                        return colonies, municipality, state
                    elif info[0] in ['Colony', 'Municipality', 'State', 'Type of Colony', 'Colony number']:
                        if info[0] == 'Colony':
                            for x in range(0, nums):
                                colonies.append(data[info[0]][number+x])
                            return colonies
                        elif info[0] == 'Type of Colony':
                            for x in range(0, nums):
                                col_types.append(data[info[0]][number+x])
                            return col_types
                        elif info[0] == 'Colony number':
                            for x in range(0, nums):
                                col_numbers.append(data[info[0]][number+x])
                            return col_numbers
                        else:
                            return data[info[0]][number]
                    else:
                        raise ValueError("Please enter a true info param here's the list of valid params\n"
                                         "* Colony\n"
                                         "* Municipality\n"
                                         "* State\n"
                                         "* Type of Colony\n"
                                         "* Colony number")
                else:
                    datas = []
                    for x in range(0, len(info)):
                        if info[x] in ['Colony', 'Municipality', 'State', 'Type of Colony', 'Colony number']:
                            if info[x] == 'Colony':
                                for y in range(0, nums):
                                    colonies.append(data[info[x]][number+y])
                                datas.append(colonies)
                            elif info[x] == 'Type of Colony':
                                for y in range(0, nums):
                                    col_types.append(data[info[x]][number+y])
                                datas.append(col_types)
                            elif info[x] == 'Colony number':
                                for y in range(0, nums):
                                    col_numbers.append(data[info[x]][number+y])
                                datas.append(col_numbers)
                            else:
                                datas.append(data[info[x]][number])
                        else:
                            raise ValueError("Please enter a true info param here's the list of valid params\n"
                                             "* Colony\n"
                                             "* Municipality\n"
                                             "* State\n"
                                             "* Type of Colony\n"
                                             "* Colony number")
                    return datas
        else:
            raise Exception("Postal code don't exist in database")

    @staticmethod
    def state_postal_code(state):
        """Returns a postal code from a param state
        :param state"""
        options = ['Coahuila de Zaragoza', 'Guerrero', 'Querétaro', 'Veracruz de Ignacio de la Llave', 'Guanajuato'
                   'Michoacán de Ocampo', 'Sinaloa', 'Tamaulipas', 'Chihuahua', 'Aguascalientes', 'Nuevo León',
                   'Tlaxcala', 'Nayarit', 'Chiapas', 'Zacatecas', 'Baja California', 'San Luis Potosí', 'Quintana Roo',
                   'Colima', 'Sonora', 'Tabasco', 'Baja California Sur', 'Puebla', 'México', 'Jalisco',
                   'Distrito Federal', 'Campeche', 'Durango', 'Oaxaca', 'Yucatán', 'Morelos', 'Hidalgo']
        if state in options:
            counter = Counter(data['State'])
            nums = counter[state.decode('utf-8')]
            num = random.randint(0, nums-1)
            number = data['State'].index(state.decode('utf-8'))
            return data['Postal Code'][number+num]
        else:
            raise ValueError("The state you send doesn't exist, here's the list\n"
                             "* Coahuila de Zaragoza        * Querétaro\n"
                             "* Guerrero                    * Veracruz de Ignacio de la Llave\n"
                             "* Guanajuato                  * Michoacán de Ocampo\n"
                             "* Sinaloa                     * Tamaulipas\n"
                             "* Chihuahua                   * Aguascalientes\n"
                             "* Nuevo León                  * Tlaxcala\n"
                             "* Nayarit                     * Chiapas\n"
                             "* Zacatecas                   * Baja California\n"
                             "* San Luis Potosí             * Quintana Roo\n"
                             "* Colima                      * Sonora\n"
                             "* Tabasco                     * Baja California Sur\n"
                             "* Puebla                      * México\n"
                             "* Jalisco                     * Distrito Federal\n"
                             "* Campeche                    * Durango\n"
                             "* Oaxaca                      * Yucatán\n"
                             "* Morelos                     * Hidalgo")
