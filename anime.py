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


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$mlady'):
        return await client.send_message(message.channel,
                                         ':flower_playing_cards: :forsen1337: *teleports behind you* :spy:')


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
    text = str(text).lower()
    legend = {
        'а': ('丹', '升', '闩'),
        'б': '石',
        'в': ('归', '乃'),
        'г': ('广', '厂'),
        'д': '亼',
        'е': ('仨', '巨', '乞'),
        'ё': '庄',
        'ж': ('卌', '水', '兴', '米'),
        'з': ('弓', '乡'),
        'и': '仈',
        'й': ('订', '计', '认'),
        'к': ('长', '片'),
        'л': ('几', '人', '穴', '入'),
        'м': ('从', '爪'),
        'н': '廾',
        'о': '口',
        'п': ('冂', '门', '刀'),
        'р': ('尸', '卩', '户'),
        'с': ('仁', '匚', '亡'),
        'т': ('丁', '丅'),
        'у': '丫',
        'ф': '中',
        'х': '乂',
        'ц': '凵',
        'ч': '丩',
        'ш': '山',
        'ь': '乙',
        'ъ': '乙',
        'щ': '山',
        'ы': '辷',
        'э': '当',
        'ю': '扣',
        'я': '兑',

        'a': ('丹', '升', '闩'),
        'b': ('归', '乃', '巧'),
        'c': ('仁', '匚', '亡'),
        'd': '力',
        'e': ('仨', '巨', '乞'),
        'f': ('彳', '下'),
        'g': ('呂', '马'),
        'h': '廾',
        'i': ('工', '丨'),
        'j': '亅',
        'k': ('长', '片'),
        'l': '心',
        'm': ('从', '爪'),
        'n': '卜丨',
        'o': '囗',
        'p': ('尸', '卩', '户'),
        'q': '贝',
        'r': '夬',
        's': ('丂', '与'),
        't': '丁',
        'u': '凵',
        'v': 'V',
        'w': ('山', '屮'),
        'x': '乂',
        'y': '丫',
        'z': '乙',
    }

    def changeletter(string, dic):
        start = ""
        for letter in string:
            if letter in dic:
                if letter == 'n':
                    start += '卜丨'
                else:
                    letter = random.choice(dic.get(letter))
                    start += letter
            else:
                if letter == "-":
                    start += " "
                else:
                    start += letter
        return start

    final = ""
    final += changeletter(text, legend)

    await client.say(final)


client.run(TOKEN)
