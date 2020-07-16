import youtube_dl
import discord
import json
import ffmpeg
import random
import discord.ext.commands as cmds
import threading


# Card stuff
class Card:
    def __init__(self, value, color):
        self.value = value
        self.color = color


colors = ['heart', 'diamonds', 'spades', 'clubs']
faces = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
kcrules = ['Waterfall', 'Give Drink', 'Take Drink', 'Floor', 'Guys', 'Chicks', 'Heaven', 'Mate', 'Rhyme', 'Categories',
           'Never have I ever', 'Question-master', 'New Rule']
deck = [Card(value, color) for value in faces for color in colors]

# json join to discord
filename = 'config.json'
with open(filename, 'r') as f:
    config_keys = json.loads(f.read())

# bot command prefix
bot = cmds.Bot(command_prefix='$')
client = discord.Client()

# global deck listening
kclistening = 0
currdeck = []
playerqueue = []


# client logged in
@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))


# kings cup initalizer
@bot.command(name='kingscup', help='Plays kings cup with all people mentioned')
async def kingscup(ctx, *args):
    global currdeck, playerqueue, kclistening
    await ctx.send('{} wants to play kings cup!'.format(ctx.author))
    currdeck = deck.copy()
    await ctx.send('Playing with {}'.format(', '.join(args)))
    random.shuffle(currdeck)
    for p in args:
        playerqueue.append(p)
    kclistening = 1


# kings cup next card
@bot.command(name='kcnext', help='pulls the next kings cup card')
async def kcnext(ctx):
    global currdeck, playerqueue, kclistening, kcrules, faces
    if kclistening == 0:
        await ctx.send('Kings Cup not Initialized')
        return
    else:
        curcard = currdeck.pop()
        await ctx.send(
            '{} got {} of {}! They must {}'.format(playerqueue[0], curcard.value, curcard.color,
                                                   kcrules[faces.index(curcard.value)]))
        undertab = int(52 - len(deck))
        random_value = int(random.choice(range(1, 30)))
        if random_value < undertab:
            await ctx.send('TAB POPPED! {}')
            kclistening = 0


# Quit the kings cup game
@bot.command(name='kcquit', help='quits playing kings cup')
async def kcquit(ctx):
    global kclistening
    if kclistening == 0:
        await ctx.send('Kings Cup not Initialized')
    else:
        await ctx.send('Closing Kings Cup')
        kclistening = 0
        return


# thunderstruck player
def timer_done(vc):
    print("timer is finished")
    vc.play(discord.FFmpegPCMAudio(executable="ffmpeg/bin/ffmpeg.exe",
                                   source="Sounds/thunderstruck.mp3"),
            after=lambda e: print('done playing', e))


@bot.command(name='thunderstruck', help='plays thunderstruck', pass_context=True)
async def thunderstruck(ctx):
    channel = ctx.message.author.voice.channel
    vc = await channel.connect()

    await ctx.send("Playing Thunderstruck in 10 seconds!")
    timer = threading.Timer(10.0, timer_done, args=[vc])
    start_time = timer.start()


# Opens url for gilmour's dream car
@bot.command(name='gilmoursdreamcar', help='gilmour dream car')
async def gilmoursdreamcar(ctx):
    await ctx.send(
        'https://en.wikipedia.org/wiki/Koenigsegg_Agera#:~:text=The%20Koenigsegg%20Agera%20is%20a,'
        '2010%20by%20Top%20Gear%20magazine')


# @roll.error
# async def roll_error(ctx, error):
#     if isinstance(error, cmds.MissingRequiredArgument):
#         await ctx.send('Usage: $roll_dice <number_of_dice> <number_of_sides>')
#     if isinstance(error, cmds.BadArgument):
#         await ctx.send('Bad Argument')


# kills the brewrobot instance for dev purposes
@bot.command(name='killbrew', help='Kills the brewrobot.')
async def killbrew(ctx):
    await ctx.send('Killing instance')
    await bot.close()


# sends a message to a user to join them for happy hour
@bot.command(name='happyhour', help='runs happy hour routine')
async def happyhour(ctx):
    recipient = ctx.message.content.split()[1]
    recipient_id = int(recipient[3: -1])
    discord_recipient = bot.get_user(recipient_id)
    if discord_recipient is None:
        await ctx.message.channel.send("Couldn't find {0}".format(recipient))
        return
    recipient_dm = discord_recipient.dm_channel
    if recipient_dm is None:
        await discord_recipient.create_dm()
        recipient_dm = discord_recipient.dm_channel
    sender_mention = ctx.message.author.mention
    await recipient_dm.send(
        'Cheers! {0} invites you to Happy Hour in {1}!'.format(sender_mention, ctx.message.channel.guild.name))


# runs the bot
bot.run(config_keys['config'])
