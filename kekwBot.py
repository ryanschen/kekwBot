# kekwBot.py
import os
import random
from discord.ext import commands, tasks
import asyncio

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

class CustomClient(discord.Client):
    async def on_ready(self):
        print(f'{self.user} has connected to discord!')
        self.loop.create_task(self.kekwPrinter())
    #@tasks.loop(seconds=10)
    async def kekwPrinter(self):
        while True:
            for guild in client.guilds:
                await client.wait_until_ready()
                print(f'{guild.name}(id: {guild.id})')
                embed = discord.Embed(title='kekw', description='kekw')
                myUrl = random.choice(['https://media1.tenor.com/images/7aa4c06eda86b4a652086af536f08820/tenor.gif?itemid=19278361','https://media1.tenor.com/images/b51320c2350b55452d54569f56fe6ed2/tenor.gif?itemid=15123134','https://media1.tenor.com/images/aab1a103aaef34e19d7bc81cd57b7b2f/tenor.gif?itemid=16598372','https://media1.tenor.com/images/a0b165e3bc241e06dee22eced66a298a/tenor.gif?itemid=19460649','https://media.tenor.com/images/c5d2069819a2cea9310eed19a8f9a1a2/tenor.gif','https://media.tenor.com/images/e96b4230b45b45a1ad96215784952b08/tenor.gif','https://media1.tenor.com/images/a20ddd95ed33c6937246c1f37232e519/tenor.gif?itemid=10111909','https://media1.tenor.com/images/aab1a103aaef34e19d7bc81cd57b7b2f/tenor.gif?itemid=16598372',
                'https://media1.tenor.com/images/9ea80c20487b8cde920259a8d2acada0/tenor.gif',
                'https://media1.tenor.com/images/acfd8e63c48d69f95ee5faf2a5a7ae09/tenor.gif',
                'https://media1.tenor.com/images/aff9b4a7c7aa872aa2744b107d56195a/tenor.gif?itemid=11927660',
                'https://media1.tenor.com/images/7860b5ae5f03d1cfc4c65b33b5145229/tenor.gif?itemid=4712025',
                'https://media1.tenor.com/images/61b9d33ed9fe45e5d567647c2e744459/tenor.gif?itemid=17876428',
                'https://media1.tenor.com/images/a6f5f616269ed0a5cd40d9b1e1c3d741/tenor.gif?itemid=18066997'])
                print(myUrl)
                embed.set_image(url=myUrl)
                await random.choice(guild.text_channels).send(embed=embed)
            await asyncio.sleep(random.randint(1800, 2000))
    #kekwPrinter.start()


client = CustomClient()


print(TOKEN)

client.run(TOKEN)
