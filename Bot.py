import asyncio
from typing import Final
import os
from dotenv import load_dotenv
from discord.ext import commands
from discord import Intents, Interaction, Member

from ShantyCode.help_cog import help_cog
from ShantyCode.music_cog import music_cog
from GrandmasterAI.GmAI import gm_response

# loading token
load_dotenv()
TOKEN: Final[str] = os.getenv('DISCORD_TOKEN')

intents: Intents = Intents.all()
bot = commands.Bot(command_prefix='/', intents=intents)


@bot.event
async def on_ready():
    print(f'{bot.user.name} is online')

    await bot.tree.sync()


# ---------------------------------------------------------------------------------------- bot testing code
@bot.tree.command()
async def assassinate(interaction: Interaction, user: Member):
    await interaction.response.send_message(f"{user.mention} was assassinated")


# ---------------------------------------------------------------------------------------- bot testing code
@bot.tree.command()
async def grandmaster(interaction: Interaction, user_message: str):
    response: str = gm_response(user_message)
    await interaction.response.send_message(response)

# ---------------------------------------------------------------------------------------- shanty
bot.remove_command('help')


async def main():
    async with bot:
        await bot.add_cog(help_cog(bot))
        await bot.add_cog(music_cog(bot))
        await bot.start(TOKEN)


asyncio.run(main())
