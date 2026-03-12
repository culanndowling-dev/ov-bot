from __future__ import annotations

import asyncio
import logging
import os
from pathlib import Path

import discord
from discord.ext import commands
from dotenv import load_dotenv

from utils.json_store import load_json

BASE_DIR = Path(__file__).parent
COGS = [
    'cogs.moderation',
    'cogs.welcome',
    'cogs.verification',
    'cogs.vehicles',
    'cogs.sessions',
    'cogs.economy',
    'cogs.reports',
    'cogs.suggestions',
    'cogs.utility',
    'cogs.logging_cog',
]


class OpenVilleBot(commands.Bot):
    def __init__(self) -> None:
        intents = discord.Intents.default()
        intents.message_content = True
        intents.members = True
        intents.guilds = True
        intents.messages = True

        super().__init__(command_prefix='!', intents=intents)
        self.base_dir = BASE_DIR
        self.config = load_json(BASE_DIR / 'config.json', {})

    async def setup_hook(self) -> None:
        for extension in COGS:
            await self.load_extension(extension)

        guild_id = self.config.get('guild_id')
        if guild_id:
            guild = discord.Object(id=guild_id)
            self.tree.copy_global_to(guild=guild)
            await self.tree.sync(guild=guild)
        else:
            await self.tree.sync()

    async def on_ready(self) -> None:
        activity = discord.CustomActivity(name=self.config.get('bot_status', 'OpenVille RP'))
        await self.change_presence(activity=activity)
        print(f'Logged in as {self.user} (ID: {self.user.id})')


async def main() -> None:
    logging.basicConfig(level=logging.INFO)
    load_dotenv()
    token = os.getenv('DISCORD_TOKEN')
    if not token:
        raise RuntimeError('DISCORD_TOKEN is missing. Put it in your .env file.')

    bot = OpenVilleBot()
    async with bot:
        await bot.start(token)


if __name__ == '__main__':
    asyncio.run(main())
