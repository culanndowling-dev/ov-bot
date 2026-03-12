# OpenVille Discord Bot

A beginner-friendly, modular Discord bot for a Greenville Roblox roleplay server.

## Features
- Moderation with warning tracking and automatic punishments
- Welcome system with configurable message and rules button
- Verification panel with verify button
- Vehicle registration and staff approval flow
- RP session start/end tools with session code logging
- Simple JSON economy
- Reports and suggestions
- Utility commands
- Logging for joins, leaves, moderation, reports, sessions, and vehicles

## Project Structure
```
openville-bot/
├── main.py
├── config.json
├── vehicles.json
├── economy.json
├── requirements.txt
├── .env.example
├── README.md
├── cogs/
├── utils/
└── data/
```

## 1. How to run the bot
1. Install Python 3.11+.
2. Create a bot application in the Discord Developer Portal.
3. Enable **Server Members Intent** and **Message Content Intent** for the bot.
4. Copy `.env.example` to `.env` and put your bot token inside.
5. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
6. Edit `config.json` with your channel IDs and role IDs.
7. Start the bot:
   ```bash
   python main.py
   ```

## 2. How to host it
You can host it on:
- a VPS
- a home PC
- Railway / Render / similar Python host

For simple hosting:
- upload the folder
- install requirements
- set the `DISCORD_TOKEN` environment variable
- run `python main.py`

## 3. How to edit settings
Everything important is in `config.json`:
- channels
- roles
- welcome text
- economy rewards
- session defaults
- logging channels

Update IDs, save the file, and restart the bot.

## 4. How to add vehicles to the database
You have two easy ways:
- edit `vehicles.json` manually under `approved_models`
- use `/add_vehicle_model`

Vehicle approvals for users are stored in:
- `vehicles.json -> user_registry`

Pending requests are stored in:
- `vehicles.json -> pending`

## 5. How to add new commands later
1. Add a new file inside `cogs/` or expand an existing cog.
2. Create a new slash command with `@app_commands.command(...)`.
3. Load the cog in `main.py` if it is a new file.
4. Restart the bot.

## Notes
- This project uses JSON for easy editing.
- For larger communities, migrate to SQLite or PostgreSQL later.
- You can expand this bot with tickets, leveling, reaction roles, or a web dashboard.
