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
faces = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
deck = [Card(value, color) for value in faces for color in colors]

filename = 'config.json'
with open(filename, 'r') as f:
    config_keys = json.loads(f.read())

# client = discord.Client()

bot = cmds.Bot(command_prefix='$')


@bot.command(name='kings-cup', help='Plays kings cup with all people mentioned')
async def kingscup(ctx, *args):
    await ctx.send('{} wants to play kings cup!'.format(ctx.author))
    kings_deck = deck.copy()
    await ctx.send('Playing with {}'.format(', '.join(args)))
    random.shuffle(kings_deck)
    done_deck = []
    while len(kings_deck) > 0:
        for player in args:
            await ctx.send('{} picked {} of {}!'.format(player, kings_deck[0].value, kings_deck[0].color))
            done_deck.insert(0, kings_deck.pop(kings_deck.index(kings_deck[0])))
            #msg = await ctx.
            if len(kings_deck) == 0:
                break


@bot.command(name='gilmoursdreamcar', help='gilmour dream car')
async def gilmoursdreamcar(ctx):
    await ctx.send(
        'https://en.wikipedia.org/wiki/Koenigsegg_Agera#:~:text=The%20Koenigsegg%20Agera%20is%20a,2010%20by%20Top%20Gear%20magazine')


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
