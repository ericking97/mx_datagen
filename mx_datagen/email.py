# -*- encoding:utf-8 -*-
"""Communications module"""
from __future__ import unicode_literals

import random

from data_source.emails_data import *
from data_source.names import *


class Email:
    """Email module"""
    @staticmethod
    def random():
        """Returns a completely random email"""
        user_name = random.choice(male_names + female_names)
        hosts = random.choice(host)
        domains = random.choice(domain)
        email = '%s@%s%s' % (user_name, hosts, domains)
        return email

    @staticmethod
    def name_email(name):
        """Returns an email starting by the name send by parameter
        :param name"""
        hosts = random.choice(host)
        domains = random.choice(domain)
        email = '%s@%s%s' % (name, hosts, domains)
        return email

    @staticmethod
    def alias_email(email):
        """Returns an alias email
        :param email"""
        if email.find('@') is not -1 and email.find('.') is not -1:
            header = email.split('@')[0]
            body = email.split('@')[1]
            final_email = header + '+' + str(random.randint(00000000, 99999999)) + '@' + body
            return final_email
        else:
            raise ValueError('Not valid email, please check syntax')
