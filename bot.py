from __future__ import print_function
from discord.enums import DefaultAvatar
from oauth2client.service_account import ServiceAccountCredentials
import gspread
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
import discord


scope = ["https://www.googleapis.com/auth/spreadsheets","https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("disord-321102-b632371be009.json", scope)

client = gspread.authorize(creds)

inventory = client.open('Inventory Management System').sheet1

inventory.update_cell(2,3, "hello world")
command_prefix = '!'
class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def calender_message(self, message):
        print('Message from {0.author}: {0.content}'.format (message))
        if message.author.bot:
            return
        if message.content[0] != command_prefix:
            return
        if message.content == '!Calender' or '!calender':
            await message.channel.send('https://docs.google.com/spreadsheets/d/1oZBWfnFzhrlFXEu1aLFf3lT8pPIYYmgRB38-2u9ty-k/edit?usp=sharing')
    async def on_message(self, message):
        if message.author.bot:
            return
        if message.content[0] != command_prefix:
            return

        cmd_args_data = message.content.split(' ')
        cmd = cmd_args_data[0]
        args = list()
        data = list()
        if len(cmd_args_data) > 1:
            args = cmd_args_data[1]
            if len(cmd_args_data) > 2:
                data = cmd_args_data[2]

        if cmd == '!hello':
            await message.channel.send(args)
        elif cmd == '!ping':
            await message.channel.send('Pong')
        elif cmd == '!help':
            await message.channel.send('Commands: \n!ping' + '\n!inventory((arguments(RainbowKit, MoonKit, SucculentKit PlantHangerKit, etc.)')
        elif cmd == '!update':
            if args == 'RainbowKit':
                inventory.update_cell(2,3, data)
        elif cmd == '!inventory':
            if args == 'RainbowKit':
                cell = sheet.cell(3,2).value
            elif args == 'MoonKit':
                cell = sheet.cell(3,9).value
            elif args == 'SucculentKit':
                cell = sheet.cell(3,3).value
            elif args == 'KeychainKit':
                cell = sheet.cell(3,4).value
            elif args == 'PlantHangerKit':
                cell = sheet.cell(3,7).value
            elif args == 'BottleToteKit':
                cell = sheet.cell(3,5).value
            elif args == 'FeatherKit':
                cell = sheet.cell(3,8).value
            elif args == 'MacraweaveKit':
                cell = sheet.cell(3,10).value
            await message.channel.send(cell)

client = MyClient()
client.run('BOT_TOKEN')
