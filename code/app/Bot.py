
# -*- coding: utf-8 -*-

from discord import Client, Activity, ActivityType

from logger import create_logger


logger = create_logger(name = 'BOT_DOTA')
class CreateBot(Client):
    def __init__(self, heroes):
        super().__init__()
        self.heroes = heroes.split('\n')


    async def on_ready(self):
        logger.info('\n\nBot is ready on as {0}! \n\n'.format(self.user))
        activity = Activity(
            name='>ajuda',
            type=ActivityType.listening,
            )
        await self.change_presence(activity=activity)

    async def on_message(self, message):
        if (
            (message.author == self.user) or
            (not message.content.startswith('>')) or
            (len(message.content) < 2)
            ):
            return

        send_message = message.channel.send

        logger.info(f'\n\nmesssage: {message.content}')
        content = message.content.lower()[1:].split()
        command = content[0]

        if(command == 'herois'):
            text = self.command_heroes()
            logger.info(f'\n\nCommand: herois | response: {text}')
            await send_message(text)
        elif(command == 'counter'):
            text = self.command_counter(content)
            logger.info(f'\n\nCommand: counter | response: {text}')
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
                text = f'Heroi selecionado {hero}'
            else:
                text = f'Heroi {hero} não foi encontrado, herois disponíveis **>herois**'

        except IndexError as error:
            text = 'Comando errado, formato correto: **>counter heroi**'

        return text
