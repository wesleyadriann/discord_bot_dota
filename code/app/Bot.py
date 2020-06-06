
# -*- coding: utf-8 -*-

from random import randrange

from discord import Client, Activity, ActivityType
import get_hero
from logger import create_logger


logger = create_logger(name = 'BOT_DOTA')
class CreateBot(Client):
    def __init__(self, heroes):
        super().__init__()
        self.heroes = heroes.split('\n')


    async def on_ready(self):
        logger.info(f'\n\nBot {self.user}is ready! \n\n')
        activity = Activity(
            name='$ajuda',
            type=ActivityType.listening,
            )
        await self.change_presence(activity=activity)

    async def on_message(self, message):
        if (
            (message.author == self.user) or
            (not message.content.startswith('$')) or
            (len(message.content) < 2)
            ):
            return

        logger.info(message.author.id)

        send_message = message.channel.send

        logger.info(f'\n\nmesssage: {message.content}')
        content = message.content.lower()[1:].split()
        command = content[0]

        if(command == 'herois'):
            text = self.command_heroes()
            logger.info(f'\n\nCommand: herois | response: {text}')
            await send_message(text)
        elif(command == 'counter'):
            await send_message('Ok, um momento.')
            text = self.command_counter(content)
            logger.info(f'\n\nCommand: counter | response: {text}')
            await send_message(text)
        elif(command == 'voudq' or command == 'voudeq'):
            text = ""
            if(message.author.id == 486367785975414794):
                text = "Com quem você se sentir mais confortavel, abraço."
            elif(message.author.id == 315499525701632002):
                text = "Com quem você se sentir mais confortavel, abraço."
            else:
                text = self.command_voudq()
            logger.info(f'\n\nCommand: voudq | response: {text}')
            await send_message(text)
        else:
            await send_message(f'{message.author} digitou: {message.content}')

    def command_heroes(self):
        text = ""
        heroes = []
        columns = 3
        line = ""
        for index, hero in enumerate(self.heroes):
            line += f'| **{hero}** '
            if(len(line.split('|')) > columns):
                line += "|"
                heroes.append(line)
                line = ""

        text = 'Herois do Dota:\n' + '\n'.join(heroes)
        return text

    def command_counter(self, content):
        text = ""
        try:
            hero = content[1:]
            if(len(hero) > 1):
                hero = ' '.join(hero)
            else:
                hero = hero[0]

            finded = False
            for local_hero in self.heroes:
                if(local_hero.lower().startswith(hero)):
                    hero = local_hero
                    finded = True
                    break

            if(finded):
                hero_info = get_hero.run(hero)
                logger.info(hero_info)
                text = f'Heroi selecionado **{hero}**\n {hero_info}'
            else:
                text = f'Heroi {hero} não foi encontrado, herois disponíveis **>herois**'

        except IndexError as error:
            text = 'Comando errado, formato correto: **>counter heroi**'

        return text

    def command_voudq(self):
        text = ""
        total_heroes = len(self.heroes)
        number = randrange(0, total_heroes)
        text = f'Herói: {self.heroes[number]}'
        return text
