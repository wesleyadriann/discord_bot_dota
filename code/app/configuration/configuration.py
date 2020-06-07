
# -*- coding: utf-8 -*-

import os

class Configuration:
    def __init__(self):
        self.DOTA_BUFF_BASE_URL = 'https://pt.dotabuff.com'
        self.HEROES = f'{self.DOTA_BUFF_BASE_URL}/heroes'
        self.HERO_COUNTERS = '/counters'
        self.HERO_COUNTERS_FULL = f'{self.DOTA_BUFF_BASE_URL}/hero-name/{self.HERO_COUNTERS}'
        self.DISCORD_BOT_KEY = os.environ.get('DISCORD_BOT_KEY')

    def configure_hero_counters_full(self, hero):
        hero_name = '-'.join(hero.split()).lower()
        self.HERO_COUNTERS_FULL = f'{self.HEROES}/{hero_name}{self.HERO_COUNTERS}'
