import discord
import random
import os
from discord.ext import commands
# Переменная intents - хранит привилегии бота
intents = discord.Intents.default()
# Включаем привелегию на чтение сообщений
intents.message_content = True
# Создаем бота в переменной client и передаем все привелегии
bot = commands.Bot(command_prefix='$', intents=intents)

fact = ['Более 99% населения мира дышат воздухом, который превышает пределы допустимых стандартов ВОЗ.', 'Сильный шум может оказывать негативное влияние на здоровье человека, особенно на слух.', 'К 2050 году в океане будет больше пластика, чем рыбы по весу.']

help =  {
    "$hello": "Приветсвует пользователя",
    "$heh": "Присылает прикольную фразу",
    "$number": "Рандомное число от 0 до 10 ",
    "$long": "Состовляет логин длиной в 10 символов",
    '$emojis': "Рандомный смайлик",
    "$mem": "Рандомный мем про IT",
    '$facts': "Интересный факт про экологию"
}

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Привет! Я бот {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def number(ctx, a: int = 0, b: int = 10):
    await ctx.send(random.randint(a, b))

@bot.command()
async def long(ctx, count_long = 10):
    await ctx.send(random.choice("+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890") * count_long)
@bot.command()
async def emojis(ctx):
    await ctx.send(random.choice('☺ ☻ ☹ シ ツ ʕʘ‿ಠʔ ￣ヘ¯ ◔◡‿◡◔ ⊙_ರೃ (͡๏̯͡๏)'))
@bot.command()
async def mem(ctx):
    list_of_files = os.listdir('memes')
    with open('memes/' + random.choice(list_of_files),'rb') as f:
        pic = discord.File(f)

    await ctx.send('Вот такой мем', file=pic)

@bot.command()
async def facts(ctx):
    await ctx.send(random.choice(fact))

@bot.command()
async def helps(ctx):
    await ctx.send(help)

bot.run("-----")
