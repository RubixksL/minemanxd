# mineman

import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import time
import random

bot = commands.Bot(command_prefix='!')
bot.remove_command("help")

@bot.event
async def on_ready():
    print ("MINE DIAMONDSSSSSS!")
    print ("My Username currently is: " + bot.user.name)
    print ("my current ID is: " + bot.user.id)
    await bot.change_presence(game=discord.Game(name='mineman | In Developement'), status=discord.Status('online')) 

#Moderation Commands

@bot.command(pass_context=True)
async def warn(ctx, member: discord.Member):
     if ctx.message.author.server_permissions.kick_members :
        embed=discord.Embed(title="User Warned", description=":white_check_mark: `{0}` has been issued a warning.".format(member, ctx.message.author), color=0x00ff00)
        await bot.say(embed=embed)
        await bot.send_message(member, '**You were warned in:** ' +ctx.message.server.name)
     else:
        embed=discord.Embed(title="Permission Denied.", description=":x: You do not have permission to use this command".format(member, ctx.message.author), color=0xffff00)
        await bot.say(embed=embed)

@bot.command(pass_context=True)
async def clearwarns(ctx, member: discord.Member):
     if ctx.message.author.server_permissions.manage_server :
        embed=discord.Embed(title="User Warns Cleared", description=":white_check_mark: The warns of `{0}` have been cleared.".format(member, ctx.message.author), color=0x00ff00)
        await bot.say(embed=embed)
        await bot.send_message(member, '**Your warns were cleared in:**' +ctx.message.server.name)
     else:
        embed=discord.Embed(title="Permission Denied.", description=":x: You do not have permission to use this command".format(member, ctx.message.author), color=0xffff00)
        await bot.say(embed=embed)

@bot.command(pass_context = True)
async def mute(ctx, member: discord.Member):
     if ctx.message.author.server_permissions.manage_roles :
        role = discord.utils.get(member.server.roles, name='Muted')
        await bot.add_roles(member, role)
        embed=discord.Embed(title="User Muted", description=":white_check_mark: `{0}` has been muted.".format(member, ctx.message.author), color=0x00ff00)
        await bot.say(embed=embed)
     else:
        embed=discord.Embed(title="Permission Denied.", description=":x: You do not have permission to use this command".format(member, ctx.message.author), color=0xffff00)
        await bot.say(embed=embed)

@bot.command(pass_context = True)
async def unmute(ctx, member: discord.Member):
     if ctx.message.author.server_permissions.manage_roles :
        role = discord.utils.get(member.server.roles, name='Muted')
        await bot.remove_roles(member, role)
        embed=discord.Embed(title="User Unmuted", description=":white_check_mark: `{0}` has been unmuted.".format(member, ctx.message.author), color=0x00ff00)
        await bot.say(embed=embed)
     else:
        embed=discord.Embed(title="Permission Denied.", description=":x: You do not have permission to use this command".format(member, ctx.message.author), color=0xffff00)
        await bot.say(embed=embed)

@bot.command(pass_context = True)
async def kick(ctx, member: discord.Member):
     if ctx.message.author.server_permissions.kick_members :
        await bot.kick(member)
        embed=discord.Embed(title="User Kicked", description=":white_check_mark: `{0}` has been kicked.".format(member, ctx.message.author), color=0x00ff00)
        await bot.say(embed=embed)
     else:
        embed=discord.Embed(title="Permission Denied.", description=":x: You do not have permission to use this command".format(member, ctx.message.author), color=0xffff00)
        await bot.say(embed=embed) 

@bot.command(pass_context = True)
async def ban(ctx, member: discord.Member):
     if ctx.message.author.server_permissions.ban_members :
        await bot.ban(member)
        embed=discord.Embed(title="User Banned", description=":white_check_mark: `{0}` has been banned.".format(member, ctx.message.author), color=0x00ff00)
        await bot.say(embed=embed)
     else:
        embed=discord.Embed(title="Permission Denied.", description=":x: You do not have permission to use this command".format(member, ctx.message.author), color=0xffff00)
        await bot.say(embed=embed)

# Fun Commands and Others


@bot.command(pass_context=True)
async def coinflip():
     await bot.say(random.choice(["Heads!", "Tails!"]))

@bot.command(pass_context = True)
async def say(ctx, *args):
    if ctx.message.author.server_permissions.manage_server :
       mesg = ' '.join(args)
       await bot.say(mesg)

@bot.command(pass_context=True)
async def ping(ctx):
    start = time.perf_counter()
    embed = discord.Embed(title= 'Pinging..', description='** **')
    message = await bot.say(embed=embed)
    end = time.perf_counter()
    duration = (end - start) * 1000
    embed = discord.Embed(title= 'Pong!', description=':stopwatch: {:.2f} ms!'.format(duration))
    await bot.edit_message(message, embed=embed)

@bot.command(pass_context=True)
async def serverinfo(ctx):
    embed = discord.Embed(name="{}'s info".format(ctx.message.server.name), description="This is the info I could find.", color=0x00ffff)
    embed.set_author(name="Server Info")
    embed.add_field(name="Name", value=ctx.message.server.name, inline=True)
    embed.add_field(name='Owner', value=ctx.message.server.owner, inline=False)
    embed.add_field(name="ID", value=ctx.message.server.id, inline=True)
    embed.add_field(name="Roles", value=len(ctx.message.server.roles), inline=True)
    embed.add_field(name="Members", value=len(ctx.message.server.members))
    embed.set_thumbnail(url=ctx.message.server.icon_url)
    await bot.say(embed=embed)

@bot.command(pass_context=True)
async def E8Ball():
     await bot.say(random.choice([":8ball: Maybe.", ":8ball: Certainly Not.", ":8ball: Yes.", ":8ball: My Sources Say No.", ":8ball: Outlook not so good.",":8ball: No. ",":8ball: Ask Me Later ",":8ball: I can't respond to that right now."]))

@bot.command(pass_context = True)
async def say(ctx, *args):
    if ctx.message.author.server_permissions.manage_server :
       mesg = ' '.join(args)
       await bot.delete_message(ctx.message)
       await bot.say(mesg)

bot.run("NTE0NjUyNTQ0NDg4ODMzMDM3.Dtb8iA.pRMFMRpD1BPQH_GsCdutHleTdYs")
