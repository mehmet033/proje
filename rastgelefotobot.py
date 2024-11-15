import discord
from discord.ext import commands
import os, random

description = '''Mehmet'in Botu'''

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='$', description=description, intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def mem(ctx, category: str = None):
    base_path = "images"
    if category:
        category_path = os.path.join(base_path, category)
        if not os.path.exists(category_path):
            await ctx.send(f"Kategori bulunamadı: {category}")
            return
        files = os.listdir(category_path)
    else:
        files = []
        for dirpath, _, filenames in os.walk(base_path):
            files.extend([os.path.join(dirpath, f) for f in filenames])
    
    if not files:
        await ctx.send("Hiç mem bulunamadı!")
        return

    img_path = random.choice(files)
    with open(img_path, "rb") as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

bot.run("")

#klasörden rastgele foto gönderen bot
