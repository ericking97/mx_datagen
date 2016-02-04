# -*- coding: utf-8 -*-
"""Names module"""
import random

male_names = ['Aarón', 'Ábaco', 'Abadón', 'Abdalá', 'Abdemelec', 'Abdénago',
              'Abdías', 'Abdón', 'Abdul', 'Abédnego', 'Abel', 'Abelardo',
              'Abelgario', 'Aberardo', 'Abner', 'Abraham', 'Absalon', 'Abudemio',
              'Abundancio', 'Abundio', 'Acaimo', 'Acario', 'Acayo', 'Acépsimas',
              'Acestes', 'Acilino', 'Acis', 'Acisclo', 'Acrisio', 'Acte',
              'Acteón', 'Acucio', 'Adalberto', 'Adalgiso', 'Adalvino', 'Adamán',
              'Adán', 'Adauco', 'Aday', 'Adelardo', 'Adelbergo', 'Adelfo',
              'Adelgiro', 'Adelino', 'Adelmo', 'Adelvino', 'Ademar', 'Adeodato',
              'Aderaldo', 'Adolfo', 'Adonias', 'Adonino', 'Adonis', 'Adrasto',
              'Adrián', 'Adulfo', 'Adventor', 'Aecio', 'Afraates', 'Afranio',
              'Africano', 'Áfrico', 'Afro', 'Afrodisio', 'Aftonio', 'Agabio',
              'Agabo', 'Agacio', 'Agamenón', 'Ágapa', 'Ágape', 'Agapito',
              'Agar', 'Agatángelo', 'Agatocles', 'Agatodoro', 'Agatón',
              'Agatónico', 'Agatopo', 'Agatópodo', 'Agenor', 'Ageo', 'Agerico',
              'Agesilao', 'Agila', 'Agilberto', 'Agileo', 'Agilo', 'Agilulfo',
              'Agis', 'Agliberto', 'Agnelo', 'Agoardo', 'Agobardo', 'Agofredo',
              'Agomar', 'Agricio', 'Agripino', 'Agrippinus', 'Águedo',
              'Agustín', 'Ahmed', 'Aiberto', 'Aicardo', 'Aidano', 'Aigulfo',
              'Ailbe', 'Aimardo', 'Aimón', 'Aitor', 'Ajab', 'Ajaz', 'Akenatón',
              'Alacrino', 'Alan', 'Alano', 'Albano', 'Albarico', 'Alberico',
              'Alberón', 'Albertino', 'Alberto', 'Albino', 'Albrado', 'Albuino',
              'Alceo', 'Alcibíades', 'Alcinoo', 'Alcuino', 'Aldeberto',
              'Alderico', 'Aldo', 'Aldobrando', 'Alefrido', 'Alejandro',
              'Alejo', 'Alexis', 'Alfano', 'Alfardo', 'Alfeo', 'Alfiero',
              'Alfio', 'Alfonso', 'Alfredo', 'Alicio', 'Alipio', 'Almaquio',
              'Almárico', 'Aloisio', 'Alonso', 'Alpiniano', 'Álvaro', 'Alvito',
              'Amabel', 'Amable', 'Amadeo', 'Amadís', 'Amado', 'Amador',
              'Amalarico', 'Amalberto', 'Amalio', 'Amancio', 'Amando',
              'Amaranto', 'Amarino', 'Amaro', 'Amasías', 'Amasio', 'Amberto',
              'Ambiorige', 'Ambrosio', 'Amenofis', 'Américo', 'Amiano',
              'Amideo', 'Amílcar', 'Aminta', 'Amio', 'Amnon', 'Amon', 'Amós',
              'Ampelo', 'Amulio', 'Anacario', 'Anacleto', 'Ananias',
              'Anastasio', 'Andrés', 'Androcles', 'Andronico', 'Anfiloco',
              'Anfion', 'Ángel', 'Aniceto', 'Anio', 'Anquises', 'Anselmo',
              'Antenor', 'Anteo', 'Antigono', 'Antiloco', 'Antinoo', 'Antioco',
              'Antipas', 'Antipater', 'Antistenes', 'Antolín', 'Antón']

female_names = ['Anita', 'Alejandra', 'Karen']

surnames = ['Sánchez', 'Martinez', 'Cebeda']

mayan_surnames = ['Ac', 'Baas', 'Bacab', 'Bak', 'Balam', 'Batún', 'Cab',
                  'Camal', 'Can', 'Canché', 'Canek', 'Canul', 'Catzim',
                  'Cauich', 'Ceh', 'Cen', 'Cetz', 'Cex', 'Cimé', 'Cob', 'Cocom',
                  'Coh', 'Cool', 'Couoh', 'Cupul', 'Cutz', 'Chablé', 'Chac',
                  'Chalé', 'Chan', 'Chay', 'Chí', 'Chim', 'Chú', 'Chuc',
                  'Chhel', 'Dzab', 'Dzal', 'Dzib', 'Dzul', 'Ek', 'Euan', 'Hau',
                  'Huchím', 'Iz', 'Kantún', 'Keb', 'Ku', 'Kutz', 'Kuyoc',
                  'Matú', 'May', 'Maz', 'Maaz', 'Mex', 'Miis', 'Moh', 'Mucuy',
                  'Na', 'Nabté', 'Nah', 'Nayal', 'Noh', 'Nuch', 'Och', 'Pacab',
                  'Pat', 'Peech', 'Pech', 'Pol', 'Pot', 'Puc', 'Puch', 'Tah',
                  'Tamay', 'Tun', 'Tuz', 'Tzab', 'Tzamá', 'Tzek', 'Uc', 'Ucán',
                  'Uicab', 'Uitz', 'Uxul', 'Xiu', 'Xol', 'Xul', 'Yah', 'Yoc']

nahuatl_surnames = ['Amixtián', 'Apahuita', 'Apango', 'Arnozoqueño', 'Atlixco',
                    'Atzin', 'Axotla', 'Cacama', 'Caleti', 'Chamilpa',
                    'Chapuli', 'Cihuacóatl', 'Cipactli', 'Cóatl', 'Coyohua',
                    'Coyotecatl', 'Coyotl', 'Cuate', 'Cuauhtémoc', 'Milpero',
                    'Mixcóatl', 'Moloya', 'Pancóal', 'Quecholli', 'Quimichi',
                    'Tecpan', 'Texcucano', 'Tezcoco', 'Tezcucano', 'Tlacomulco',
                    'Tlamilpa', 'Tlaxcala', 'Tlaxcalli', 'Tocatli', 'Tochi',
                    'Toxqui', 'Toxtle', 'Toza', 'Xalpeño', 'Xochicale',
                    'Xochihua', 'Xochimanahua', 'Xochime', 'Xochímitl',
                    'Xochiquiquixque', 'Xochitémol', 'Xóchitl', 'Xochitótol',
                    'Xotémol', 'Zacatenco', 'Zalpeño', 'Zepactle', 'Zepahua',
                    'Zepahuitse']

yaqui_surnames = ['Anguamea', 'Bacasehua', 'Buitimea', 'Choki', 'Cochemea',
                  'Cosmea', 'Huiqui', 'Jusacamea', 'Misibea', 'Moroyoqui',
                  'Pamea', 'Sibamea', 'Tequida', 'Yeomans']


class GenNames:
    """Names class"""
    @staticmethod
    def create_first_name(arg=None):
        """Return a male name"""
        if arg is 'male' or arg is 'Male' or args is 'M':
            first_name = random.choice(male_names)
        elif arg is 'female' or arg is 'Female' or args is 'F':
            first_name = random.choice(female_names)
        else:
            first_name = random.choice(male_names + female_names)
        return first_name

    @staticmethod
    def create_surname(arg=None):
        """Return a complete random surname"""
        if arg is 'common':
            surname = random.choice(surnames)
        elif arg is 'mayan':
            surname = random.choice(mayan_surnames)
        elif arg is 'nahuatl':
            surname = random.choice(nahuatl_surnames)
        elif arg is 'yaqui':
            surname = random.choice(yaqui_surnames)
        else:
            surname = random.choice(surnames + mayan_surnames + nahuatl_surnames + yaqui_surnames)
        return surname
