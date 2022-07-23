import discord
import os
from PySimpleGUI import PySimpleGUI as sg



class MyClient(discord.Client):
    async def on_ready(self):                   
        print('Developed by @andrezin.py')
        print('intagram: https://www.instagram.com/andreison.py/ ')
        print('Funcionando como: {0}!'.format(self.user))
    async def on_message(self, message):
        print('Mensagem de {0.author}:{0.content}'.format(message))
        if message.content == '!regras':
            await message.channel.send(f'''@{message.author.name} as regras do servidor são:
            {os.linesep}:point_right:1. Respeitar todos igualmente.
            {os.linesep}:point_right:3. Não gritar nas calls.
            {os.linesep}:point_right: 4. Não enviar pornográfia.
            {os.linesep}:point_right:5. Não enviar gore.
            {os.linesep}:point_right:6. Evitar off-topic.
            {os.linesep}:point_right:7. Usar bot de música somente nos canais de música.
            {os.linesep}''')
        elif message.content == '!TikTok':
            await message.channel.send(f'''{message.author.name}TikTok oficial da SKY {os.linesep} https://www.tiktok.com/@oficial_teamsky {os.linesep} Passa lá :grin:''')
        
        
        elif message.content == '!tiktok':
             await message.channel.send(f'''{message.author.name}TikTok oficial da SKY {os.linesep} https://www.tiktok.com/@oficial_teamsky {os.linesep} Passa lá :grin:''')
        
        
        elif message.content == '!Rp':
            await message.author.send(f'''**COMANDO EM PROGRAMAÇÃO** Qualquer duvida, digite **!ajudaRp**''')
            await message.channel.send(f'''Salve {message.author.name}, Te mandei uma mensagem no privado, confere lá''')
        
        
        elif message.content == '!rp':
            await message.author.send(f'''**COMANDO EM PROGRAMAÇÃO** Qualquer duvida, digite **!ajudaRp**''')
            await message.channel.send(f'''Salve {message.author.name}, Te mandei uma mensagem no privado, confere lá''')        
        
        elif message.content == '!ajudarp':
            await message.author.send(f'''Fala com eles aqui: <@!251080522401447936>, <@!630931258498613258>, <@!381233152183500802>, <@!987420394732519434> {os.linesep}Eles vão te ajudar <3  ''')
        
        
        elif message.content == '!Ajudarp':
            await message.author.send(f'''Fala com eles aqui: <@!251080522401447936>, <@!630931258498613258>, <@!381233152183500802>, <@!987420394732519434> {os.linesep}Eles vão te ajudar <3  ''')
        
        elif message.content == '!test':
            await message.channel.send(f'va se foder {message.author.name} <#1000442830126325862> :D')

        
        elif message.content == '<@910236137631674479>':
             await message.channel.send(f'''```Olá {message.author.name}, CALMA!!! esse comando ainda está sendo programado :D```''')
        
        
        elif message.content == '!':
            await message.channel.send(f'''EPA!!! {message.author.name}, esse é meu prefixo''')

intents = discord.Intents.default()
intents.members = True
client = MyClient(intents=intents)
client.run('      TOKEN GOES HERE  :D          ')
