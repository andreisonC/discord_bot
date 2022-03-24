from email import message
from mailbox import linesep
import discord
import os
from tqdm import tqdm
import time
import datetime

with tqdm(total=100) as pbar:
    for i in range(4):
        time.sleep(0.5)
        pbar.update(25)


class MyClient(discord.Client):
    async def on_ready(self):
        print('Developed by @andrezin.py')
        print('intagram: https://www.instagram.com/andreison.py/ ')
        print('Funcionando como: {0}!'.format(self.user))

    async def on_message(self, message):
        print('Mensagem de {0.author}:{0.content}'.format(message))
        if message.content == '!regras':
            await message.channel.send(f'@{message.author.name} as regras do servidor são:{os.linesep}:point_right:1. Respeitar todos igualmente.{os.linesep}:point_right:3. Não gritar nas calls.{os.linesep}:point_right: 4. Não enviar pornográfia.{os.linesep}:point_right:5. Não enviar gore.{os.linesep}:point_right:6. Evitar off-topic.{os.linesep}:point_right:7. Usar bot de música somente nos canais de música.{os.linesep}')
        elif message.content == '!instagram':
            await message.author.send('Olha o insta do <@!424190619968339968>, https://www.instagram.com/andreison.py/ (ele que me fez :v)')
        elif message.content == '!Instagram':
            await message.author.send('Olha o insta do <@!424190619968339968>, https://www.instagram.com/andreison.py/ (ele que me fez :v)')
        elif message.content == '!recrut':
            await message.author.send(f'Olá{message.author.name}, aqui está o link: {os.linesep} https://docs.google.com/forms/d/e/1FAIpQLSe00bqxHPIDYlwcMmtt_iKsddci1EAqHf_UdK8K7NzQFBkFGQ/viewform?usp=sf_link {os.linesep}Qualquer duvida, digite **!ajudarecrut**')
            await message.channel.send(f'Salve {message.author.name}, Te mandei uma mensagem no privado, confere lá')
        elif message.content == '!Recrut':
            await message.author.send(f'Olá{message.author.name}, aqui está o link: {os.linesep} https://docs.google.com/forms/d/e/1FAIpQLSe00bqxHPIDYlwcMmtt_iKsddci1EAqHf_UdK8K7NzQFBkFGQ/viewform?usp=sf_link {os.linesep}Qualquer duvida, digite **!ajudarecrut**')
            await message.channel.send(f'Salve {message.author.name}, Te mandei uma mensagem no privado, confere lá')        
        elif message.content == '!ajudarecrut':
            await message.author.send(f'Fala com ele aqui: <@!424190619968339968> ou ele aqui: <@!417552142820311040>{os.linesep}Eles vão te ajudar <3  ')
        elif message.content == '!Ajudarecrut':
            await message.author.send(f'Fala com ele aqui: <@!424190619968339968> ou ele aqui: <@!417552142820311040>{os.linesep}Eles vão te ajudar <3  ')
        elif message.content == 'test':
            await message.channel.send(' ')
        elif message.content == '<@!870666144426627092>':
            await message.channel.send(f"Olá {message.author.name}, se liga na minha lista de comandos:{os.linesep}!regras {os.linesep}!instagram{os.linesep}{os.linesep}--> CLÂ <--{os.linesep}{os.linesep}        !recrut{os.linesep}     !ajudarecrut{os.linesep}{os.linesep} ")

    async def on_menber_join(self, member):
        guild = member.guild
        if guild.system_channel is not None:
            mensagem = f'{member.mention} acabou de entrar no {guild.name}, seja bem vindo(a)!{os.linesep} use *!regras* para regras do servidor, ou me marque para menu de comandos!'
            await guild.system_channel.send(message)


intents = discord.Intents.default()
intents.members = True
client = MyClient(intents=intents)
client.run('MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM')
