# -*- encoding:utf-8 -*-
"""Communications module"""
import random
from .data_source.emails_data import *
from .data_source.names import *


class Emails:
    """Email module"""
    @staticmethod
    def random_email():
        """Returns a completely random email"""
        user_name = random.choice(male_names + female_names)
        hosts = random.choice(host)
        domains = random.choice(domain)
        return user_name + '@' + hosts + domains

    @staticmethod
    def alias_email(email):
        """Returns an alias email"""
        if email.find('@') is not -1 and email.find('.') is not -1:
            header = email.split('@')[0]
            body = email.split('@')[1]
            final_email = header + '+' + str(random.randint(00000000, 99999999)) + '@' + body
            return final_email
        else:
            return "No ingresaste un email válido"
