# id 541537048495128576
#token NTQxNTM3MDQ4NDk1MTI4NTc2.Dzg5tw.sRzkFH4OVWIwjYqWZSa-WXe0h1E
#8
#https://discordapp.com/oauth2/authorize?client_id=541537048495128576&scope=bot&permissions=8

import discord

client = discord.Client()

@client.event #event decorator/wrapper
async def on_ready():
	print(f"WE have logged in as {client.user}")

@client.event
async def on_message(message):
	print(f"{message.channel} : {message.author} : {message.author.name} : {message.content}")

	if "hi there" in message.content.lower():
		await message.channel.send("HI!")

	if "hi" in message.content.lower():
		await message.channel.send("Hello there " + f"{message.author.name}")

	if "how are you" in message.content.lower():
		await message.channel.send("I'm Fine... How are you doing today?")

	if "fuck" in message.content.lower():
		await message.delete()
		await message.channel.send("Sorry, that is a banned word. Please refrain from using it. " + "<@" + f"{message.author.id}" + ">")

	if "creeper" in message.content.lower():
		await message.delete()
		await message.channel.send("Sorry, Please refrain from using that Meme here. " + "<@" + f"{message.author.id}" + ">")

	if get.time() = "12:30":
		set message.channel = "chat"
		await message.channel.send("Hope you all are enjoying the server. Please make sure to follow the rules.")

	file = open ("logs.txt", "r")
	ign = get.message.content();
	while(a = file.readline(file) != 'EOF')
			b = file.readline()
			temp = b.split(:)
			if b[2].equals(ign):
				if temp[4] = red:
					team = red
				elif temp[4] = green:
					team = green
				elif temp[4] = blue:
					team = blue
	close(file);
	if temp.equals(red):
		rolered = get(message.server.roles, name='Red')
	        await client.add_roles(message.author, role)
	if temp.equals(green):
		rolegreen = get(message.server.roles, name='Green')
	        await client.add_roles(message.author, role)
	if temp.equals(blue):
		roleblue = get(message.server.roles, name='Blue')
	        await client.add_roles(message.author, role)


client.run("NTQxNTM3MDQ4NDk1MTI4NTc2.Dzg5tw.sRzkFH4OVWIwjYqWZSa-WXe0h1E")
