import youtube_dl
import discord
import discord.ext.commands as cmds
import json
import ffmpeg

filename = 'config.json'
config_keys = {}
with open(filename, 'r') as f:
    config_keys = json.loads(f.read())

bot = cmds.Bot(command_prefix="$")
client = discord.Client
players = {}

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))

@bot.command(pass_context=True)
async def thunderstruck(ctx):
    channel = ctx.message.author.voice.channel
    vc = await channel.connect()
    vc.play(discord.FFmpegPCMAudio(executable="C:/ffmpeg/bin/ffmpeg.exe",
                                   source="Sounds/thunderstruck.mp3"),
            after=lambda e: print('done playing', e))

@bot.command(pass_context=True)
async def happyhour(ctx):
	recipient = ctx.message.content.split()[1]
	recipient_id = int(recipient[3: -1])
	discord_recipient = client.get_user(recipient_id)
		if discord_recipient == None:
			await ctx.message.channel.send("Could'nt find {0}".format(recipient))
			return
		recipient_dm = discord_recipient.dm_channel
		if recipient_dm == None:
			await discord_recipient.create_dm()
			recipient_dm = discord_recipient.dm_channel
		sender_mention = ctx.message.author.mention
		await recipient_dm.send('Cheers! {0} invites you to Happy Hour in {1}!'.format(sender_mention, message.channel.guild.name))

@bot.command(pass_context=True)
async def killgill(ctx):
	await ctx.message.channel.send('goodbye gil')
	await client.close()

bot.run(config_keys['config'])