
# -*- coding: utf-8 -*-

from random import randrange

from discord import Client, Activity, ActivityType
import spiders.get_hero as get_hero
from configuration.logger import create_logger


logger = create_logger(name = 'BOT_DOTA')

class CreateBot(Client):
    def __init__(self, heroes):
        super().__init__()
        self.heroes = heroes.split('\n')
        self.commands = {
            "ajuda": self.command_ajuda,
            "herois": self.command_heroes,
            "voudq": self.filter_command_voudq,
            "voudeq": self.filter_command_voudq,
            "counter": self.command_counter,
        }


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

        text = ""
        if(command in self.commands):
            text = self.commands[command](
                content=content,
                author=message.author,
                )
        else:
            text = f'{message.author}, o commando {message.content} não existe, utilize **$ajuda**'

        if(text):
            await send_message(text)

    def command_heroes(self, **kwargs):
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

    def command_counter(self, **kwargs):
        content = kwargs.get('content')
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
                text = f'Heroi {hero} não foi encontrado, herois disponíveis **$herois**'

        except IndexError as error:
            text = 'Comando errado, formato correto: **$counter heroi**'

        return text

    def filter_command_voudq(self, **kwargs):
        author = kwargs.get('author')
        text = ""
        if(author.id == 486367785975414794):
            options = ['Herói: Pugna', 'Herói: Dazzle', 'Com quem você se sentir mais confortavel, abraço.']
            text = options[randrange(0, 3)]
        elif(author.id == 315499525701632002):
            options = [lambda: "Com quem você se sentir mais confortavel, abraço.", self.command_heroes]
            text = options[randrange(0, 2)]()
        else:
            text = self.command_voudq()
        return text

    def command_voudq(self, **kwargs):
        text = ""
        total_heroes = len(self.heroes)
        number = randrange(0, total_heroes)
        text = f'Herói: {self.heroes[number]}'
        return text

    def command_ajuda(self, **kwargs):
        return {"x": 1, "y": 3}
