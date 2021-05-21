# bot.py
import os
import random
from typing import final
import discord
from discord import voice_client
from discord import user
from discord.channel import VoiceChannel
from dotenv import load_dotenv
from discord.ext import commands

import logging
logging.basicConfig(level=logging.INFO)

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix = '!', case_insensitive = True, intents = intents) # Creates instance of bot

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.command(name = 'flip', help = 'The coin knows all')
async def coinflip(ctx):
    coin_list = ['hEaDs!', 'tAiLs!']
    response = random.choice(coin_list)
    await ctx.send(response)

@bot.command(name = 'ryan', help = 'rYaN')
async def ryan(ctx):
    imgdirectory = 'pictures\\'
    await ctx.channel.send(file=discord.File(imgdirectory + 'lil bill.jpg'))

@bot.command(name = 'dummy', help = 'pepega')
async def dummy(ctx):
    imgdirectory = 'pictures\\'
    await ctx.channel.send(file=discord.File(imgdirectory + 'pepega.png'))

@bot.command(name = 'elton', help = 'eLtOn')
async def elton(ctx):
    imgdirectory = 'pictures\\'
    await ctx.channel.send(file=discord.File(imgdirectory + 'elton.png'))

@bot.command(name = 'rishi', help = 'rIsHi')
async def rishi(ctx):
    imgdirectory = 'pictures\\'
    await ctx.channel.send(file=discord.File(imgdirectory + 'kameleon.jpg'))

@bot.command(name = 'teams', help='')
async def teams(ctx):
    def createTeams(users):
        """Returns a string describing the teams for the bot to send"""
        ### NOTE: Will replace this with a rich embed message instead of just a string ###

        if not users:
            # If a team is attempted to be created with an empty list of users
            return "Voice channel is empty"
        
        random.shuffle(users) # Randomizes users passed in
        teamList = users[0:(len(users) // 2)] + users[(len(users) // 2):] # Creates the team given a list of users

        finalTeams = "Team 1:"
        for name in teamList[0:(len(teamList) // 2)]:
            finalTeams += " " + name
        
        finalTeams += "\nTeam 2:"
        for name in teamList[(len(teamList) // 2):]:
            finalTeams += " " + name

        return finalTeams

    inVoiceChannel = ctx.author.voice # Voice status of user who called the command
    memberList = [] # List of members
    userList = [] # List of strings of the member's nicknames in the voice channel
    
    if inVoiceChannel == None:
        # If member who called command is not in a voice channel
        await ctx.channel.send("Get in voice channel dummy")
    else:
        voiceChannel = ctx.author.voice.channel # Gets the voice channel the author is in
        memberList = voiceChannel.members # Gets members in voice channel of the author
        # Pulls strings of usernames/nicknames (if applicable)
        userList = [member.nick if (member.nick is not None) else member.name for member in memberList]
        await ctx.channel.send(createTeams(userList))

bot.run(TOKEN)