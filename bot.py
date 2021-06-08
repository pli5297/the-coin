# bot.py
import os
import random
from typing import final
import discord
from discord import voice_client
from discord import user
from discord import team
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
    await ctx.channel.send()
    await ctx.channel.send(response)

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

@bot.command(name = 'teams', help='Generates random teams for a custom game')
async def teams(ctx):
    def createTeams(users):
        """Returns a list of randomized players or an empty list if there are no players"""
        if not users:
            # If a team is attempted to be created with an empty list of users
            return []
        
        random.shuffle(users) # Randomizes users passed in
        teamList = users[0:(len(users) // 2)] + users[(len(users) // 2):] # Creates the team given a list of users

        # finalTeams = "Team 1:"
        # for name in teamList[0:(len(teamList) // 2)]:
        #     finalTeams += " " + name
        
        # finalTeams += "\nTeam 2:"
        # for name in teamList[(len(teamList) // 2):]:
        #     finalTeams += " " + name

        return teamList
    
    def chooseCharacters(game, teamLen):
        '''Returns two strings containing each teams characters'''
        # Randomizes players' agents
        agentList = ["Reyna", "Omen", "Killjoy", "Brimstone", "Astra", "Sova", "Phoenix", "Jett", "Cypher", "Sage", "Raze", "Yoru", "Viper", "Skye", "Breach"]
        teamOneAgents = random.sample(agentList, teamLen)
        teamTwoAgents = random.sample(agentList, teamLen)
        teamOneAgents = [(agent + "\n") for agent in teamOneAgents]
        teamTwoAgents = [(agent + "\n") for agent in teamTwoAgents]
        teamOneAgents = "".join(teamOneAgents)
        teamTwoAgents = "".join(teamTwoAgents)

        return teamOneAgents, teamTwoAgents

    def createEmbed(game, teams):
        '''Returns a rich embed message for the custom teams'''
        if game == "Valorant":
            # Gets the map for the game
            mapsFile = "pictures\\valorant-maps.txt"
            file = open(mapsFile, "r")
            mapList = file.readlines()
            mapList = [map.split(",") for map in mapList]
            map = random.choice(mapList)
            file.close()

            # Divides out the randomized list of users into two strings containing each team
            if len(teams) <= 1:
                # Bounds checking
                return None
            teamOne = teams[0:(len(teams) // 2)]
            teamTwo = teams[(len(teams) // 2):]
            teamOne = [(user + "\n") for user in teamOne]
            teamTwo = [(user + "\n") for user in teamTwo]
            teamOneAgents, teamTwoAgents = chooseCharacters(game, len(teamOne))
            teamOne = "".join(teamOne)
            teamTwo = "".join(teamTwo)

            # Creates the embed
            embed = discord.Embed(title = map[0], type = "rich", color=0xff0000)
            # Map Image
            embed.set_thumbnail(url=map[1])
            # Attackers Column
            embed.add_field(name = "Attackers", value = teamOne, inline = True)
            # Attackers Agents
            embed.add_field(name = "Agents", value = teamOneAgents, inline = True)
            # Empty Line Seperator
            embed.add_field(name = "\u200B", value = "\u200B", inline = False)
            # Defenders Column
            embed.add_field(name = "Defenders", value = teamTwo, inline = True)
            # Defenders Agents
            embed.add_field(name = "Agents", value = teamTwoAgents, inline = True)

        return embed

    game = "Valorant"
    inVoiceChannel = ctx.author.voice # Voice status of user who called the command
    memberList = [] # List of members
    userList = [] # List of strings of the member's nicknames in the voice channel
    
    
    if inVoiceChannel == None:
        # If member who called command is not in a voice channel
        await ctx.channel.send("Get in voice channel dummy")
    else:
        voiceChannel = ctx.author.voice.channel # Gets the voice channel the author is in
        memberList = voiceChannel.members # Gets members in voice channel of the author
        memberList = [member for member in memberList if (not member.voice.self_mute)]

        # Pulls strings of usernames/nicknames (if applicable)
        userList = [member.nick if (member.nick is not None) else member.name for member in memberList]
        teamList = createTeams(userList)
        embed = createEmbed(game, teamList)
        if embed != None:
            await ctx.channel.send(embed = embed)
        else:
            await ctx.channel.send("Not enough players dumbass")

bot.run(TOKEN)