
# -*- coding: utf-8 -*-

from Bot import CreateBot
from logger import logger_discord
import get_hero, get_heroes, runner
from configuration import Configuration

logger_discord()
config = Configuration()

def main():
    heroes = get_heroes.run()
    bot = CreateBot(heroes)
    bot.run(config.DISCORD_BOT_KEY)

if __name__ == '__main__':
    main()
