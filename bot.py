# bot.py
import os
import random
import discord
from dotenv import load_dotenv
from discord.ext import commands

import logging
logging.basicConfig(level=logging.INFO)

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.command(name = 'flip', help = 'The coin knows all')
async def coinflip(ctx):
    coin_list = ['hEaDs!', 'tAiLs!']
    response = random.choice(coin_list)
    await ctx.send(response)

@bot.command(name = 'nut', help = 'Elton nutting')
async def nut(ctx):
    response = """────▓▓▓▓▓▓▓▓
──▓▓▓▓▓▓▒▒▒▒▒▒▓▓──────────────███
─▓▓▓▓▒░░▒▒▓▓▒▒▓▓▓▓────────────█░░█
▓▓▓▓▒░░▓▓▓▒▄▓░▒▄▄▄▓─────────██░░░█
▓▓▓▓▒░░▒▀▀▀▀▒░▄░▄▒▓▓──────────█░█
▓▓▓▓▒░░▒▒▒▒▒▓▒▀▒▀▒▓▒▓────────██░█
▓▓▓▓▒▒░░░▒▒▒░░▄▀▀▀▄▓▒▓ ──────██░░█
▓▓▓▓▓▒▒░░░▒▒▓▀▄▄▄▄▓▒▒▒▓ ─────█░░░█
▓█▀▄▒▓▒▒░░░▒▒░░▀▀▀▒▒▒▒▓─ ───█░░░░█
─▓█▒▒▄▒▒▒▒▒▒▒░░▒▒▒▒▒▒▓─────█░░░░█
──▓▓▓▓▒▒▒▒▒▒▒▒░░░▒▒▒▓ ─────█░░░░█                                                                          ░░░
────▓▓▒░░▒▒▒▒▒▒▒▒▒▒▒▓─────█░░░░█                                                                       ░████░
▓────▓▒▒░░░░▒▒▒▒▒▒▒▓​─────█░░░░░█                                                                    ░█elton█░
░█───█░░░░░░░░░░░░░█───██░░░░░█                                                                    ░███ ██░
░░███░░░░░░░░░░░░░░░███░░░░░░█                                                                        ░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░██
░░░░░░░░░░░░░░░░░░░░░░░░░░█─────────────────────▄▄▀▀█
█░░░░░░░░░░░░░░░░░░░░░░░░█────────────────────▄█▒░░▄░█
─██░░░░░░░░░░░░░░░░░░░░░░█───────────────────▄▀▒▀▀▀▄▄▀
───█░░░░░░░░░░░░░░░░░░░░░░█─────────────────█▒░░░░░▄▀
────█░░░░░░░░░░░░░░░░░░░░░█──-───-──────────█▒░░░░░▄▀
────█░░░░░░░░░░░░░░░░░░░░░█───────────────█▒░░░░░▄▀
─────█░░░░░░░░░░░░░░░░░░░░░█─────────────█▒░░░░░▄▀
─────█░░░░░░░░░░░░░░░░░░░░░█────────────█▒░░░░░ ▄▀
──────█░░░░░░░░░░░░░░░░░░░░░█──────────█▒░░░░░▄ ▀
──────​​█░░░░░░░░░░░░░░░░░░░░░█─────────█▒░░░░░▄▀
──────██░░░░░░░░░░░░░░░░░░░░░▓█──────█▒░░░░░▄▀
───────█░░░░░░░░░░░░░░░░░░░░░▒░█────█▒░░░░░▄▀
───────█░░░░░░░░░░░░░░░░░░░░░░░░▀▄─█▒░░░░░▄▀
────────█░░░░░░░░░░░░░░░░░░░░░░░░░█▒░░░░░▄▀
─────────█░░░░░░░░░░░░▒▒▒▒▒▒░░░░▄▀▒░░░░░▄▀
─────────█░░░░░░░░░░░▒▒▓▓▓▓▓▓▒░█▒░░░░░░█▄
──────────█░░░░░░░░░▒▓▓▓█████▀▒░░░░░░░█▀▄
──────────█░░░░░░░░░░▒▓▓█████▒▒░░░░░▒█░▀▄
──────────█░░░░░░░░░░▒▓▓██▓▓▒▒▒▀▀▀█▒█░░░█
───────────█░░░░░░░░░░▒▓██▓▒▒▒▒▒▒▒▒▒█░░░░█
────────────█░░░░░░░░░▒▓▓█▓▒▒▒▒▒▒▓▒▒█░░░░░█
─────────────█░░░░░░░░░░▒▒▀▀▄▄▄▄█▄▄▀░░░░░░░█"""
    await ctx.send(response)

@bot.command(name = 'ryan', help = 'rYaN')
async def ryan(ctx):
    imgdirectory = 'pictures\\'
    await ctx.channel.send(file=discord.File(imgdirectory + 'lil bill.jpg'))

@bot.command(name = 'dummy', help = 'rYaN')
async def dummy(ctx):
    imgdirectory = 'pictures\\'
    await ctx.channel.send(file=discord.File(imgdirectory + 'pepega.png'))

@bot.command(name = 'elton', help = 'rYaN')
async def elton(ctx):
    imgdirectory = 'pictures\\'
    await ctx.channel.send(file=discord.File(imgdirectory + 'elton.png'))

@bot.command(name = 'rishi', help = 'rYaN')
async def rishi(ctx):
    imgdirectory = 'pictures\\'
    await ctx.channel.send(file=discord.File(imgdirectory + 'kameleon.jpg'))


bot.run(TOKEN)