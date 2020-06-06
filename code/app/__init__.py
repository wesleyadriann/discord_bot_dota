
# -*- coding: utf-8 -*-

from Bot import CreateBot
from logger import logger_discord
from spiders import get_hero, get_heroes
from configuration import Configuration
import runner

logger_discord()
config = Configuration()

def main():
    heroes = runner.run(get_heroes.Get_Heroes)
    bot = CreateBot(heroes)
    bot.run(config.DISCORD_BOT_KEY)

if __name__ == '__main__':
    main()
