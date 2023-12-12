import discord
import asyncio
import random
import os

from discord.utils import get


intents = discord.Intents.all()
client = discord.Client(intents=intents)


@client.event
async def on_ready():

    print(client.user.name)
    print('성공적으로 봇이 시작되었습니다')
    game = discord.Game('~하는중') # ~~ 하는중
    await client.change_presence(status=discord.Status.online, activity=game)
    
    
    
@client.event
async def on_message(message):
    if message.content == "안녕": # 내가 '안녕'이라고 말하면
        msg =  await message.channel.send (f"이봇은 파이썬 기반으로 만든 봇이에여 + 유캔이 만들었어요") # 봇이 '안녕하세요'라고 대답
        await asyncio.sleep(60) # 숫자는 몇초후를 의미함
        await msg.delete() # 메세지 삭제를 의미

        if message.content == "노맨션":
            await message.channel.send ("{여러분들} 안녕하세요".format(message.author))
            
        if message.content == "dm":
         dme = "테스트"  # DM으로 받고 싶은 메시지를 작성하세요
        if message.author.dm_channel:
         await message.author.dm_channel.send(dme)
        elif message.author.dm_channel is None:
            channel = await message.author.create_dm()
            await channel.send(dme)

@client.event
async def on_message(message):
    if message.content.startswith(",계산 "):
        dlf = message.content.replace(",계산 ", "1")
        dle = (dlf[1:]) 
        fef = eval(dle)
        await message.channel.send (f"{fef} 입니다")

@client.event
async def on_ready():

    print(client.user.name)
    print('성공적으로 봇이 시작되었습니다')
    game = discord.Game('망고야 도움말')
    await client.change_presence(status=discord.Status.online, activity=game)
    ch = client.get_channel(1182283526549278831)
    await ch.send (f"✅ **망고봇이 시작하였습니다**")
    
access_token = os.environ["BOT_TOKEN"]
client.run(MTE4MjYxOTc5MjIwMTQ5NDYwOA.GwxIZk.35wUlR8i1DybwAjuBLYQ1sdG5iFnTX4Hhchp8U) # 토큰 적는곳
