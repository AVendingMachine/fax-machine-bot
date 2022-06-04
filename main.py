
import discord
from discord.ext import commands
from pathlib import Path

TOKEN = Path('bottoken.txt').read_text()

bot = commands.Bot(command_prefix="/")

@bot.event
async def on_ready():
    try:
        await bot.change_presence(activity=discord.Game('/faxhelp'))
        print("Fax Machine Online")
    except:
        print("Fax Machine Failed to Start!")
@bot.command()
async def faxstatus(ctx):
	await ctx.channel.send("Online")

@bot.command()
async def fax(ctx, user:discord.User,*,message):
    try:
        await ctx.message.delete()
        await user.send(message)
        print("User Sent Message")
    except discord.Forbidden:
        print("Message Could Not Be Sent! (Blocked)")
        await ctx.send('Message Failed to Send! (Blocked)')

@bot.command()
async def faxhelp(ctx):
    await ctx.send('<Fax Help> \n -Command Structure: \n /fax [UserID] [Message] \n -How to get a UserID: \n Enable developer mode under advanced settings in user settings \n Then right click on someones name and click copy id \n -Example: \n /fax 431996025813729302 Hi \n -Version \n 0.4 Github Cleanup')
   


@fax.error
async def fax_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        print("Message Could Not Be Sent! (Missing Argument)")
        await ctx.send('Message Failed to Send! (Missing Argument)')
    elif isinstance(error, commands.UserNotFound):
        print("Message Could Not Be Sent! (User Not Found)")
        await ctx.send('Message Failed to Send! (User Not Found)')
    else: 
        print(error)

bot.run(TOKEN)

stopclose = input()
# :D
