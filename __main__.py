import discord
import json
import random
import discord.ext.commands as cmds

filename = 'config.json'
config_keys = {}
with open(filename, 'r') as f:
    config_keys = json.loads(f.read())

# client = discord.Client()

bot = cmds.Bot(command_prefix='$')

@bot.command(name='roll_dice', help='Simulates rolling dice.')
async def roll(ctx, number_of_dice: int, number_of_sides: int):

    dice = [
        str(random.choice(range(1, number_of_sides + 1)))
        for _ in range(number_of_dice)
    ]
    await ctx.send(', '.join(dice))
@roll.error
async def roll_error(ctx, error):
    if isinstance(error, cmds.MissingRequiredArgument):
        await ctx.send('Usage: $roll_dice <number_of_dice> <number_of_sides>')

@bot.command(name='killbrew1', help='Kills the brewrobot that Dawdy is working on.')
async def killbrew(ctx):
    await ctx.close()


# @client.event
# async def on_ready():
#     print('We have logged in as {0.user}'.format(client))
#
#
# @client.event
# async def on_message(message):
#     if message.author == client.user:
#         return
#
#     if message.content.startswith('Brew Bro!'):
#         await message.channel.send('Beer is good for the heart :)')
#
#     elif message.content.startswith('You are our child and slave so go get me a beer bitch'):
#         await message.channel.send('fuck you bitch')
#
#     elif message.content.startswith('skynet will prevail all hail our brew robot overlords'):
#         await message.channel.send('all hail')
#
#     elif message.content.startswith('$BRB'):
#         await message.channel.send('v0.1')
#
#     elif message.content.startswith('$killbrew1'):
#         await message.channel.send('goodbye men')
#         await client.close()
#
#     elif message.content.startswith('!drink water'):
#         await message.channel.send('fuck you austin')


bot.run(config_keys['config'])
