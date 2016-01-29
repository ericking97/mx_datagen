# -*- coding: utf-8 -*-
"""This file contains functions that return a name with certain caracteristics"""
import random

male_names = ['Aarón', 'Ábaco', 'Abadón', 'Abdalá', 'Abdemelec', 'Abdénago',
              'Abdías', 'Abdón', 'Abdul', 'Abédnego', 'Abel', 'Abelardo',
              'Abelgario', 'Aberardo', 'Abner','Abraham', 'Absalon', 'Abudemio',
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
              'Amideo', 'Amílcar', 'Aminta', 'Amio', 'Amnon','Amon', 'Amós',
              'Ampelo', 'Amulio', 'Anacario', 'Anacleto', 'Ananias',
              'Anastasio', 'Andrés', 'Androcles', 'Andronico', 'Anfiloco',
              'Anfion', 'Ángel', 'Aniceto', 'Anio', 'Anquises', 'Anselmo',
              'Antenor', 'Anteo', 'Antigono', 'Antiloco', 'Antinoo', 'Antioco',
              'Antipas', 'Antipater', 'Antistenes', 'Antolín', 'Antón']

female_names = ['Anita', 'Alejandra', 'Karen']

surnames = ['Sánchez', 'Martinez', 'Cebeda']

class Names():
    """Names class"""
    def create_male_first_name(self):
        """Return a male name"""
        return random.choice(male_names)

    def create_female_first_name(self):
        """Return a female name"""
        return random.choice(female_names)

    def create_paternal_surname(self):
        """Return paternal surname"""

    def create_maternal_surname(self):
        """Return maternal surname"""
