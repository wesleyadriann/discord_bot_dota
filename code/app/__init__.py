
# -*- coding: utf-8 -*-

import os
import discord
from logger import logger, m_logger


class BotDota(discord.Client):
    async def on_ready(self):
        m_logger.info('Logged on as {0}!'.format(self.user))
        activity = discord.Activity(
            name=">ajuda",
            type=discord.ActivityType.listening,
            )
        await self.change_presence(activity=activity)

    async def on_message(self, message):
        if (
            (message.author == self.user) or 
            (not message.content.startswith('>')) or
            (len(message.content) < 2)
            ):
            return

        await message.channel.send(f'{message.author} digitou: {message.content}')


bot = BotDota()
bot.run(os.environ.get('DISCORD_BOT_KEY'))