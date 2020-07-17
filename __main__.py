import threading
import discord
import json
import time
import asyncio
import random
import discord.ext.commands as cmds

#PlayerQueue stuff
class PlayerQueue:
    def __init__(self):
        self.players = []
        self.numPlayers = 0

    def addPlayer2Queue(self, player):
        self.players.append(player)
        self.numPlayers += 1

    def removePlayerFromQueue(self, player):
        self.players.remove(player)
        self.numPlayers -= 1

    def getPlayerNames(self):
        result = []
        for player in self.players:
            result.append(player.name)
        return result

    def nextPlayer(self):
        return self.players.pop(0)

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

# global state machine listening
kclistening = False
thunderlistening = False

# current card deck and player queue
currdeck = []
playerqueue = PlayerQueue()


# state machine
def getCurrentState():
    if kclistening or thunderlistening:
        return True
    else:
        return False


# client logged in
@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))


# join the player queue
@bot.command(name='join', help='adds the joining player to the queue')
async def joinQueue(ctx):
    playerqueue.addPlayer2Queue(ctx.author)
    await ctx.send('{0} is now playing games!'.format(ctx.author.mention))


# leave the player queue
@bot.command(name='leave', help='removes the leaving player from the queue')
async def leaveQueue(ctx):
    playerqueue.removePlayerFromQueue(ctx.author)
    await ctx.send('{0} quit the game.'.format(ctx.author.mention))


# kings cup initializer
@bot.command(name='kingscup', help='Plays kings cup with all people mentioned')
async def kingscup(ctx):
    if getCurrentState():
        await ctx.send("Already playing a game")
        return
    global currdeck, playerqueue, kclistening
    kclistening = True
    await ctx.send('{} wants to play kings cup!'.format(ctx.author))
    currdeck = deck.copy()
    await ctx.send('Playing with {}'.format(', '.join(playerqueue.getPlayerNames())))
    random.shuffle(currdeck)
    kclistening = 1


# kings cup next card
@bot.command(name='kcnext', help='pulls the next kings cup card')
async def kcnext(ctx):
    global currdeck, playerqueue, kclistening, kcrules, faces
    if kclistening is False:
        await ctx.send('Kings Cup not Initialized')
        return
    else:
        curcard = currdeck.pop()
        currentPlayer = playerqueue.nextPlayer()
        await ctx.send(
            '{} got {} of {}! They must {}'.format(currentPlayer.mention, curcard.value, curcard.color,
                                                   kcrules[faces.index(curcard.value)]))
        playerqueue.addPlayer2Queue(currentPlayer)
        undertab = int(52 - len(deck))
        random_value = int(random.choice(range(1, 30)))
        if random_value < undertab:
            await ctx.send('TAB POPPED! {}')
            kclistening = 0


# Quit the kings cup game
@bot.command(name='kcquit', help='quits playing kings cup')
async def kcquit(ctx):
    global kclistening
    if kclistening is False:
        await ctx.send('Kings Cup not Initialized')
    else:
        await ctx.send('Closing Kings Cup')
        kclistening = 0
        return


# thunderstruck player
@bot.command(name='thunderstruck', help='plays thunderstruck', pass_context=True)
async def thunderstruck(ctx):
    if getCurrentState():
        await ctx.send("Already playing a game")
        return
    global thunderlistening
    thunderlistening = True
    channel = ctx.message.author.voice.channel
    vc = await channel.connect()
    await ctx.send("Playing Thunderstruck in 10 seconds!")
    await ctx.send('Playing with {}'.format(', '.join(playerqueue)))
    timer = threading.Timer(10.0, lambda: print("timer is finished")).start()
    time.sleep(10)
    vc.play(discord.FFmpegPCMAudio(executable="ffmpeg/bin/ffmpeg.exe",
                                   source="Sounds/thunderstruck.mp3"),
            after=lambda e: print('done playing', e))

    start_time = time.time()
    current_time = time.time() - start_time
    past_time = current_time

    while vc.is_playing():
        await asyncio.sleep(0.01)
        past_time = current_time
        current_time = round(time.time() - start_time, 1)

        # tells player to drink at each specific timestamps where 'thunder' is said
        if past_time != current_time:
            if current_time == 29.0:
                currentPlayer = playerqueue.pop(0)
                await ctx.send('{} DRINK!'.format(currentPlayer))
                playerqueue.append(currentPlayer)

            if current_time == 32.9:
                currentPlayer = playerqueue.pop(0)
                await ctx.send('{} DRINK!'.format(currentPlayer))
                playerqueue.append(currentPlayer)

            if current_time == 36.5:
                currentPlayer = playerqueue.pop(0)
                await ctx.send('{} DRINK!'.format(currentPlayer))
                playerqueue.append(currentPlayer)

            if current_time == 39.8:
                currentPlayer = playerqueue.pop(0)
                await ctx.send('{} DRINK!'.format(currentPlayer))
                playerqueue.append(currentPlayer)

            if current_time == 43.5:
                currentPlayer = playerqueue.pop(0)
                await ctx.send('{} DRINK!'.format(currentPlayer))
                playerqueue.append(currentPlayer)

            if current_time == 47.1:
                currentPlayer = playerqueue.pop(0)
                await ctx.send('{} DRINK!'.format(currentPlayer))
                playerqueue.append(currentPlayer)

            if current_time == 50.8:
                currentPlayer = playerqueue.pop(0)
                await ctx.send('{} DRINK!'.format(currentPlayer))
                playerqueue.append(currentPlayer)

            if current_time == 54.5:
                currentPlayer = playerqueue.pop(0)
                await ctx.send('{} DRINK!'.format(currentPlayer))
                playerqueue.append(currentPlayer)

            if current_time == 58.0:
                currentPlayer = playerqueue.pop(0)
                await ctx.send('{} DRINK!'.format(currentPlayer))
                playerqueue.append(currentPlayer)

            if current_time == 61.5:
                currentPlayer = playerqueue.pop(0)
                await ctx.send('{} DRINK!'.format(currentPlayer))
                playerqueue.append(currentPlayer)

            if current_time == 70.5:
                currentPlayer = playerqueue.pop(0)
                await ctx.send('{} DRINK!'.format(currentPlayer))
                playerqueue.append(currentPlayer)

            if current_time == 78.7:
                currentPlayer = playerqueue.pop(0)
                await ctx.send('{} DRINK!'.format(currentPlayer))
                playerqueue.append(currentPlayer)

            if current_time == 85.0:
                currentPlayer = playerqueue.pop(0)
                await ctx.send('{} DRINK!'.format(currentPlayer))
                playerqueue.append(currentPlayer)

            if current_time == 92.0:
                currentPlayer = playerqueue.pop(0)
                await ctx.send('{} DRINK!'.format(currentPlayer))
                playerqueue.append(currentPlayer)

            if current_time == 111.5:
                currentPlayer = playerqueue.pop(0)
                await ctx.send('{} DRINK!'.format(currentPlayer))
                playerqueue.append(currentPlayer)

            if current_time == 161.5:
                currentPlayer = playerqueue.pop(0)
                await ctx.send('{} DRINK!'.format(currentPlayer))
                playerqueue.append(currentPlayer)

            if current_time == 165.2:
                currentPlayer = playerqueue.pop(0)
                await ctx.send('{} DRINK!'.format(currentPlayer))
                playerqueue.append(currentPlayer)

            if current_time == 169.1:
                currentPlayer = playerqueue.pop(0)
                await ctx.send('{} DRINK!'.format(currentPlayer))
                playerqueue.append(currentPlayer)

            if current_time == 172.7:
                currentPlayer = playerqueue.pop(0)
                await ctx.send('{} DRINK!'.format(currentPlayer))
                playerqueue.append(currentPlayer)

            if current_time == 222.8:
                currentPlayer = playerqueue.pop(0)
                await ctx.send('{} DRINK!'.format(currentPlayer))
                playerqueue.append(currentPlayer)

            if current_time == 226.3:
                currentPlayer = playerqueue.pop(0)
                await ctx.send('{} DRINK!'.format(currentPlayer))
                playerqueue.append(currentPlayer)

            if current_time == 229.9:
                currentPlayer = playerqueue.pop(0)
                await ctx.send('{} DRINK!'.format(currentPlayer))
                playerqueue.append(currentPlayer)

            if current_time == 233.5:
                currentPlayer = playerqueue.pop(0)
                await ctx.send('{} DRINK!'.format(currentPlayer))
                playerqueue.append(currentPlayer)

            if current_time == 251.0:
                currentPlayer = playerqueue.pop(0)
                await ctx.send('{} DRINK!'.format(currentPlayer))
                playerqueue.append(currentPlayer)

            if current_time == 254.8:
                currentPlayer = playerqueue.pop(0)
                await ctx.send('{} DRINK!'.format(currentPlayer))
                playerqueue.append(currentPlayer)

            if current_time == 257.0:
                currentPlayer = playerqueue.pop(0)
                await ctx.send('{} DRINK!'.format(currentPlayer))
                playerqueue.append(currentPlayer)

            if current_time == 258.0:
                currentPlayer = playerqueue.pop(0)
                await ctx.send('{} DRINK!'.format(currentPlayer))
                playerqueue.append(currentPlayer)

            if current_time == 261.9:
                currentPlayer = playerqueue.pop(0)
                await ctx.send('{} DRINK!'.format(currentPlayer))
                playerqueue.append(currentPlayer)

            if current_time == 265.3:
                currentPlayer = playerqueue.pop(0)
                await ctx.send('{} DRINK!'.format(currentPlayer))
                playerqueue.append(currentPlayer)

            if current_time == 268.7:
                currentPlayer = playerqueue.pop(0)
                await ctx.send('{} DRINK!'.format(currentPlayer))
                playerqueue.append(currentPlayer)

            if current_time == 272.2:
                currentPlayer = playerqueue.pop(0)
                await ctx.send('{} DRINK!'.format(currentPlayer))
                playerqueue.append(currentPlayer)

            if current_time == 275.8:
                currentPlayer = playerqueue.pop(0)
                await ctx.send('{} DRINK!'.format(currentPlayer))
                playerqueue.append(currentPlayer)

            if current_time == 278.9:
                currentPlayer = playerqueue.pop(0)
                await ctx.send('{} DRINK!'.format(currentPlayer))
                playerqueue.append(currentPlayer)


# Opens url for gilmour's dream car
@bot.command(name='gilmoursdreamcar', help='gilmour dream car')
async def gilmoursdreamcar(ctx):
    await ctx.send(
        'https://en.wikipedia.org/wiki/Koenigsegg_Agera#:~:text=The%20Koenigsegg%20Agera%20is%20a,'
        '2010%20by%20Top%20Gear%20magazine')


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
