
# -*- coding: utf-8 -*-

import logging

def logger_discord():
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger('discord')
    logger.setLevel(logging.DEBUG)
    handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
    handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
    logger.addHandler(handler)

def create_logger(name = 'logger_name'):
    m_logger = logging.getLogger(name)
    # handler = logging.StreamHandler()
    # handler.setFormatter(logging.Formatter('%(name)s - %(levelname)s :: %(message)s'))
    # m_logger.addHandler(handler)

    return m_logger
