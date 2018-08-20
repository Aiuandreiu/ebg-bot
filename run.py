#eBattlegrounds Bot by Aiuandreiu

import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio

bot = commands.Bot(command_prefix='!')
bot.remove_command('help')

@bot.event
async def on_ready():
    await bot.change_presence(game=discord.Game(name="Aiuandreiu", type=2))
    print ("Online")

@bot.event
async def on_message(message):
    if message.content.startswith("!userinfo"):
        try:
            user = message.mentions[0]
            userjoinedat = str(user.joined_at).split('.', 1)[0]
            usercreatedat = str(user.created_at).split('.', 1)[0]
 
            userembed = discord.Embed(
                title="Username:",
                description=user.mention,
                color=0xd100ff
            )
            userembed.set_author(
                name=user.name + "'s Info",
                icon_url=user.avatar_url
            )
            userembed.add_field(
                name="Joined the server at:",
                value=userjoinedat
            )
            userembed.add_field(
                name="User Created at:",
                value=usercreatedat
            )
            userembed.add_field(
                name="User ID:",
                value=user.id
            )
            userembed.add_field(
                name="Bot",
                value=user.bot
            )
            userembed.set_thumbnail(
                url=user.avatar_url
            )
 
            await bot.send_message(message.channel, embed=userembed)
        except IndexError:
            await bot.send_message(message.channel, "Error!")
        finally:
            pass
    await bot.process_commands(message)

@bot.command(pass_context=True)
async def help(ctx):
    author = ctx.message.author

    embed = discord.Embed(
        color=0xd100ff
    )

    embed.set_author(name="Commands")
    embed.add_field(name="!help", value="Displays this message.", inline=False)
    embed.add_field(name="!founder", value="Information about the founder of eBattlegrounds.", inline=False)
    embed.add_field(name="!creator", value="Information about the creator of this bot.", inline=False)
    embed.add_field(name="!userinfo", value="Information about a person from the server.", inline=False)
    embed.add_field(name="!serverinfo", value="Information about the server.", inline=False)
    embed.add_field(name="!XD", value="Displays a gif.", inline=False)+
    
    await bot.say(embed=embed)

@bot.command(pass_context=True)
async def XD(ctx):
    embed=discord.Embed(color=0xd100ff)
    embed.set_thumbnail(url="https://i.redd.it/4ajfe9xdjaf11.gif")
    await bot.say(embed=embed)

@bot.command(pass_context=True)
async def founder(ctx):
    embed = discord.Embed(title="George D is the Founder of eBattlegrounds.", color=0xd100ff)
    await bot.say(embed=embed)

@bot.command(pass_context=True)
async def creator(ctx):
    embed = discord.Embed(title="Aiuandreiu is my Creator.", color=0xd100ff)
    await bot.say(embed=embed)

@bot.command(pass_context=True)
async def serverinfo(ctx):
    embed = discord.Embed(title="Server info".format(ctx.message.server.name), description="Here's what I could find.", color=0xd100ff)
    embed.add_field(name="Name", value=ctx.message.server.name, inline=True)
    embed.add_field(name="ID", value=ctx.message.server.id, inline=True)
    embed.add_field(name="Roles", value=len(ctx.message.server.roles), inline=True)
    embed.add_field(name="Members", value=len(ctx.message.server.members))
    embed.add_field(name="Channels", value=len(ctx.message.server.channels))
    embed.set_thumbnail(url=ctx.message.server.icon_url)
    await bot.say(embed=embed)

bot.run("TOKEN")
