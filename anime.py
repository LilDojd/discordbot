# !/usr/bin/env python
# -*- coding: utf-8 -*-

import random
import asyncio
import aiohttp
import discord
from discord.ext import commands
from discord.ext.commands import Bot

TOKEN = 'NDUyMTUyMDcxNDM3NjgwNjQy.DfMK-g.AVS6VjH3sKABi2qt1zWCph2H4wI'

client = Bot(command_prefix='$', description='Orewa gadaisuki nandayo')


@client.event
async def on_ready():
    print('Logged in as ' + client.user.name + ' (ID:' + client.user.id + ') | Connected to ' + str(
        len(client.servers)) + ' servers | Connected to ' + str(len(set(client.get_all_members()))) + ' users')
    print('--------')
    print('Use this link to invite {}:'.format(client.user.name))
    print('https://discordapp.com/oauth2/authorize?client_id={}&scope=bot&permissions=8'.format(client.user.id))
    print('--------')
    return await client.change_presence(game=discord.Game(name='Teleports behind you'))


@client.command()
async def square(number):
    squared_value = int(number) * int(number)
    await client.say(str(number) + " squared is " + str(squared_value))


@client.command(name='nippon',
                description="Превращает убогий текст в латинице или кириллице в богоподобный японский",
                brief="Answers from the beyond.",
                aliases=['anime'],
                pass_context=False)
async def nippon(text):
    text = text.lower()
    legend = {
        'а': '丹',
        'б': '石',
        'в': '归',
        'г': '广',
        'д': '亼',
        'е': '仨',
        'ё': '庄',
        'ж': '卌',
        'з': '弓',
        'и': '仈',
        'й': '订',
        'к': '长',
        'л': '几',
        'м': '从',
        'н': '廾',
        'о': '口',
        'п': '冂',
        'р': '尸',
        'с': '仁',
        'т': '丁',
        'у': '丫',
        'ф': '中',
        'х': '乂',
        'ц': '凵',
        'ч': '丩',
        'ш': '山',
        'щ': '山',
        'ы': '辷',
        'э': '当',
        'ю': '扣',
        'я': '兑',

        'a': '闩',
        'b': '归',
        'c': '匚',
        'd': '力',
        'e': '仨',
        'f': '彳',
        'g': '呂',
        'h': '廾',
        'i': '工',
        'j': '亅',
        'k': '片',
        'l': '心',
        'm': '从',
        'n': '卜',
        'o': '囗',
        'p': '户',
        'q': '贝',
        'r': '夬',
        's': '丂',
        't': '丁',
        'u': '凵',
        'v': 'V',
        'w': '山',
        'x': '乂',
        'y': '丫',
        'z': '乙',
    }

    def changeletter(letter, dic):
        for i, j in dic.items():
            letter = letter.replace(i, j)
        return letter

    final = ""
    final += changeletter(text, legend)

    await client.say(final)

client.run(TOKEN)
