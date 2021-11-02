import discord
import os
import time
from discord.utils import get
from discord.ext import commands, tasks
from discord.ext.commands import has_permissions,  CheckFailure, check
import random
from random import randint
from dhooks import Webhook,Embed
import string
client = discord.Client()
client = commands.Bot(command_prefix = '-',case_insensitive=True)
client.remove_command('help')
@client.event
async def on_ready():
    channel = client.get_channel(903690747197390888)
    await channel.send('DNA Reship Bot is UP!')
    print("online")
##SILENT##    
@client.command()
async def dna_us1(ctx):
    def random_character(n):
      return ''.join(random.choice(string.ascii_uppercase) for x in range(n))
    def random_author(n):
      return ''.join(random.choice(ctx.author.display_name) for x in range(n))
    def threeletters():
      if random_author(3).isalpha() == True:
        return random_author(3).upper()
      else:
       return random_character(3)   
    hook = Webhook('https://discord.com/api/webhooks/890607746481782815/HHIIWq6PrYTmkfGX-buMS92CGXDfZoek-2JvyfU2kFywge5jW3OcblFar6qMjTNNhD6g')   
    embed = discord.Embed() 
    embed.title=':flag_us: DNA US NEW YORK RESHIPPER' 
    embed.colour = discord.Color.teal()   
    embed.description=f"""
    First Name: (your name)
    Last Name: Atillo
    Address: {threeletters()} 175 w 60th Street, Valet Apt.
    City: New York
    State: New York (NY)
    Postal: 10023

    **Notes:**
    *- You can use randomize US phone numbers if you're running for multiple raffles/pairs.
    Click here to get your own US Number: https://discord.com/channels/812034353780752425/829812077731643424/856232448114425886*
    
    **Thank you and Good luck!**"""           
    embed.set_footer(text=f'Requested by {ctx.author}',icon_url='https://media.discordapp.net/attachments/814869462188556339/862375736416403496/DNA_Logo.png')
    embed.set_thumbnail(url='https://cdn.britannica.com/79/4479-050-6EF87027/flag-Stars-and-Stripes-May-1-1795.jpg')
    embed.set_author(name='DNA RESHIP BOT')  
    await ctx.send(embed=embed)
    hook.send(embed=embed)

##GEEZLER##
@client.command()
async def dna_us2(ctx):
    def random_character(n):
      return ''.join(random.choice(string.ascii_uppercase) for x in range(n))
    def random_author(n):
      return ''.join(random.choice(ctx.author.display_name) for x in range(n))
    def threeletters():
      if random_author(3).isalpha() == True:
        return random_author(3).upper()
      else:
       return random_character(3)   
    hook = Webhook('https://discord.com/api/webhooks/890607746481782815/HHIIWq6PrYTmkfGX-buMS92CGXDfZoek-2JvyfU2kFywge5jW3OcblFar6qMjTNNhD6g')   
    embed = discord.Embed() 
    embed.title=':flag_us: DNA US CALIFORNIA RESHIPPER\n(STOCK X & GOAT SHIPMENTS ONLY)' 
    embed.colour = discord.Color.teal()   
    embed.description=f"""
    First Name: (your name)
    Last Name: Fevidal
    Address: {threeletters()} 4165 Amapola Way
    City: Sacramento (SAC)
    State: California (CA)
    Postal: 95823
    Postal 9-digit: 95823-5028

    **Notes:**
    *- You can use randomize US phone numbers if you're running for multiple raffles/pairs.
    Click here to get your own US Number: https://discord.com/channels/812034353780752425/829812077731643424/856232448114425886
    In case of emergency, you can use (916)317-1989*
    
    **Thank you and Good luck!**"""           
    embed.set_footer(text=f'Requested by {ctx.author}',icon_url='https://media.discordapp.net/attachments/814869462188556339/862375736416403496/DNA_Logo.png')
    embed.set_thumbnail(url='https://cdn.britannica.com/79/4479-050-6EF87027/flag-Stars-and-Stripes-May-1-1795.jpg')
    embed.set_author(name='DNA RESHIP BOT')  
    await ctx.send(embed=embed)
    hook.send(embed=embed)

##ROGUE##
@client.command()
async def dna_uk(ctx):
    def random_character(n):
      return ''.join(random.choice(string.ascii_uppercase) for x in range(n))
    def random_author(n):
      return ''.join(random.choice(ctx.author.display_name) for x in range(n))
    def threeletters():
      if random_author(3).isalpha() == True:
        return random_author(3).upper()
      else:
       return random_character(3)   
    hook = Webhook('https://discord.com/api/webhooks/890607746481782815/HHIIWq6PrYTmkfGX-buMS92CGXDfZoek-2JvyfU2kFywge5jW3OcblFar6qMjTNNhD6g')   
    embed = discord.Embed() 
    embed.title=':flag_gb: DNA UK RESHIPPER'  
    embed.colour = discord.Color.teal()  
    embed.description=f"""
    First Name: (your name)
    Last Name: Atkinson
    Address: {threeletters()} 15 Jedburgh Street
    Town: Middlesbrough
    County: North Yorkshire
    Postal: DN22 7EH
   
    **Notes:**
    *Please do note that you can use randomize UK phone numbers starting with 0115 and is 7 digits long if you're running for multiple raffles/pairs.*
    
    **Thank you and Good luck!**"""           
    embed.set_footer(text=f'Requested by {ctx.author}',icon_url='https://media.discordapp.net/attachments/814869462188556339/862375736416403496/DNA_Logo.png')
    embed.set_thumbnail(url='https://cdn.pixabay.com/photo/2015/11/06/13/29/union-jack-1027898__340.jpg')
    embed.set_author(name='DNA RESHIP BOT')  
    await ctx.send(embed=embed)
    hook.send(embed=embed)

##BULLYBOY##
@client.command()
async def dna_sg(ctx):
    def random_character(n):
      return ''.join(random.choice(string.ascii_uppercase) for x in range(n))
    def random_author(n):
      return ''.join(random.choice(ctx.author.display_name) for x in range(n))
    def threeletters():
      if random_author(3).isalpha() == True:
        return random_author(3).upper()
      else:
       return random_character(3)   
    hook = Webhook('https://discord.com/api/webhooks/890607746481782815/HHIIWq6PrYTmkfGX-buMS92CGXDfZoek-2JvyfU2kFywge5jW3OcblFar6qMjTNNhD6g')   
    embed = discord.Embed() 
    embed.title=':flag_sg: DNA SG RESHIPPER'
    embed.colour = discord.Color.teal()  
    embed.description=f"""
    Name: (your name)
    Address: {threeletters()} 83A Frankel Avenue
    City: Singapore
    State (If necessary): South East
    Postal: 458211
   
    **Notes:**
    *- Names can be random, Phone number can be any random 8 numbers
    - SG shipment typically cares only about Postal code or Address Line 1*
    
    **Thank you and Good luck!**"""           
    embed.set_footer(text=f'Requested by {ctx.author}',icon_url='https://media.discordapp.net/attachments/814869462188556339/862375736416403496/DNA_Logo.png')
    embed.set_thumbnail(url='https://wallpapercave.com/wp/wp4214707.jpg')
    embed.set_author(name='DNA RESHIP BOT')  
    await ctx.send(embed=embed)
    hook.send(embed=embed)
client.run("TOKEN") 