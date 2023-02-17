import discord
import asyncio
from discord.ext import commands


token="MTA3NDg3OTgwOTU4ODU2Mzk4MQ.GkRYJx.vBK1KeMbV-V7iSopiO--JEgcds5hw-igPm-F24"
OWNER_IDS= [217354675454738433,246469891761111051,1049313229127557180]

bot = commands.AutoShardedBot(command_prefix="s!",intents=discord.Intents.all(),owner_ids=OWNER_IDS,allowed_mentions=discord.AllowedMentions(everyone=False, replied_user=False,roles=False),case_insensitive=True,strip_after_prefix=True,replied_user=False,shard_count=1, sync_commands_debug= True, sync_commands=True)
bot.remove_command("help")



async def load():
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            await bot.load_extension(f"cogs.{filename[:-3]}")
import os
os.system("pip install jishaku")




    
async def main () :
    await load()
    await bot.load_extension("jishaku")
    os.environ["JISHAKU_NO_DM_TRACEBACK"] = "True"
    os.environ["JISHAKU_HIDE"] = "True"
    os.environ["JISHAKU_NO_UNDERSCORE"] = "True"
    os.environ["JISHAKU_FORCE_PAGINATOR"] = "True"
    await bot.start(token)
  
async def on_ready(bot):
  await bot.change_presence(activity=discord.Activity(type=(discord.ActivityType.playing),name="Google Chrome", url='https://discord.gg/sputnik'))
  print('Your bot is randi')

asyncio.run(main())