import discord

client = discord.Client()


@client.event
async def on_ready():
	print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
	if message.author == client.user:
		return

	if message.content.startswith('Brew Bro!'):
		await message.channel.send('Beer is good for the heart :)')

	elif message.content.startswith('You are our child and slave so go get me a beer bitch'):
		await message.channel.send('fuck you bitch')

	elif message.content.startswith('skynet will prevail all hail our brew robot overlords'):
		await message.channel.send('all hail')

	elif message.content.startswith('$BRB'):
		await message.channel.send('v0.1')

client.run('NzMyNDE3OTY3ODkxMDIxOTQ0.Xw0ZXw.FbnV25hTSHCHXavReaSx6YB9u1M')
