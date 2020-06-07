
# -*- coding: utf-8 -*-

from Bot import CreateBot
from configuration.logger import logger_discord
import runner
import spiders.get_heroes as get_heroes
from configuration.configuration import Configuration

logger_discord()
config = Configuration()

def main():
    heroes = get_heroes.run()
    bot = CreateBot(heroes)
    bot.run(config.DISCORD_BOT_KEY)

if __name__ == '__main__':
    main()
