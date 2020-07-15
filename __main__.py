import discord
import json
import random
import discord.ext.commands as cmds
import sys


class Card:
    def __init__(self, value, color):
        self.value = value
        self.color = color


colors = ['heart', 'diamonds', 'spades', 'clubs']
deck = [Card(value, color) for value in range(1, 14) for color in colors]

filename = 'config.json'
config_keys = {}
with open(filename, 'r') as f:
    config_keys = json.loads(f.read())

# client = discord.Client()

bot = cmds.Bot(command_prefix='$')


@bot.command(name='kings-cup', help='Plays kings cup with all people mentioned')
async def kingscup(ctx, *args):
    await ctx.send('Playing with {}'.format(', '.join(args)))
    


# @bot.command(name='roll_dice', help='Simulates rolling dice.')
# async def roll(ctx, number_of_dice: int, number_of_sides: int):
#     if int(number_of_sides) < 1 | int(number_of_dice) < 1:
#         print('invalid number')
#         await ctx.send('Usage: $roll_dice <number_of_dice>  <number_of_sides>\nParams:\nnumber_of_dice > '
#                        '0\nnumber_of_sides > 0')
#     dice = [
#         str(random.choice(range(1, number_of_sides + 1)))
#         for _ in range(number_of_dice)
#     ]
#     print('here')
#     print(number_of_dice)
#     print(number_of_sides)
#
#     await ctx.send(', '.join(dice))
#
#
# @bot.command(name='add', help='Add numbers.')
# async def add(ctx, num1: int, num2: int):
#     await ctx.send(num1 + num2)
#
#
# @bot.command(name='lessthan', help='lessthanfunc')
# async def lessthan(ctx, num1: int, num2: int):
#     if num1 < num2:
#         await ctx.send('{} is less than {}'.format(num1, num2))
#     elif num2 < num1:
#         await ctx.send('{} is greater than {}'.format(num1, num2))
#     elif num1 == num2:
#         await ctx.send('{} is equal to {}'.format(num1, num2))
#     else:
#         await ctx.send('bad numbers')
#
#
# @roll.error
# async def roll_error(ctx, error):
#     if isinstance(error, cmds.MissingRequiredArgument):
#         await ctx.send('Usage: $roll_dice <number_of_dice> <number_of_sides>')
#     if isinstance(error, cmds.BadArgument):
#         await ctx.send('Bad Argument')


@bot.command(name='killdawdy', help='Kills the brewrobot that Dawdy is working on.')
async def killbrew(ctx):
    await ctx.send('Killing Dawdy\'s instance')
    sys.exit()


bot.run(config_keys['config'])
