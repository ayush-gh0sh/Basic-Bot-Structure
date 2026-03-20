import discord
from discord.ext import commands
import os
import json
import asyncio

# ==============================
# LOAD CONFIG
# ==============================

with open("config.json", "r", encoding="utf-8") as f:
    config = json.load(f)

PREFIX = config.get("prefix", ".")
TOKEN = os.getenv("BOT_TOKEN") or config.get("token")
STATUS = config.get("status", "Online")

if not TOKEN:
    raise ValueError("❌ No bot token found! Set BOT_TOKEN env var or add it to config.json")

# ==============================
# BOT SETUP
# ==============================

# FIX: Use Intents.default() + specific intents instead of Intents.all()
# Intents.all() enables everything including unstable future intents
intents = discord.Intents.default()
intents.members = True
intents.presences = True
intents.message_content = True

bot = commands.Bot(
    command_prefix=PREFIX,
    intents=intents,
    help_command=None
)

# ==============================
# SMART AUTO LOADER
# ==============================

async def load_cogs():
    loaded = 0
    skipped = 0
    failed = 0

    for root, dirs, files in os.walk("."):
        root = root.replace("\\", "/")

        # Skip cache folders
        if "__pycache__" in root:
            continue

        for file in files:
            if not file.endswith(".py"):
                continue

            if file in ("__init__.py", "bot.py"):
                continue

            # FIX: Skip test files to prevent accidental cog loading
            if file.startswith("test_"):
                skipped += 1
                continue

            filepath = os.path.join(root, file).replace("\\", "/")

            # Remove "./"
            if filepath.startswith("./"):
                filepath = filepath[2:]

            module_path = filepath[:-3].replace("/", ".")

            try:
                # Check if file has setup()
                with open(filepath, "r", encoding="utf-8") as f:
                    content = f.read()

                if "async def setup" not in content:
                    print(f"[SKIPPED] {module_path} (no setup)")
                    skipped += 1
                    continue

                await bot.load_extension(module_path)
                print(f"[LOADED] {module_path}")
                loaded += 1

            except Exception as e:
                print(f"[FAILED] {module_path} → {e}")
                failed += 1

    print("\n==============================")
    print("📊 LOAD SUMMARY")
    print(f"✅ Loaded  : {loaded}")
    print(f"⏭️  Skipped : {skipped}")
    print(f"❌ Failed  : {failed}")
    print("==============================\n")

# ==============================
# BOT EVENTS
# ==============================

@bot.event
async def on_ready():
    # FIX: Guard against on_ready firing multiple times on reconnects
    if not hasattr(bot, "_ready_fired"):
        bot._ready_fired = True
        print(f"🤖 Logged in as {bot.user}")
        await bot.change_presence(activity=discord.Game(name=STATUS))

        # Sync slash commands
        try:
            synced = await bot.tree.sync()
            print(f"🌐 Synced {len(synced)} slash command(s)")
        except Exception as e:
            print(f"❌ Slash sync failed → {e}")

# ==============================
# GLOBAL ERROR HANDLER
# ==============================

# FIX: Added global error handler — was completely missing before
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        return  # silently ignore unknown commands
    elif isinstance(error, commands.MissingPermissions):
        await ctx.send("❌ You don't have permission to use this command.")
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(f"❌ Missing argument: `{error.param.name}`")
    elif isinstance(error, commands.BadArgument):
        await ctx.send(f"❌ Invalid argument provided.")
    else:
        await ctx.send(f"❌ An error occurred: `{error}`")
        raise error  # still raise so it shows in console

# ==============================
# MAIN START
# ==============================

async def main():
    async with bot:
        await load_cogs()
        await bot.start(TOKEN)

asyncio.run(main())
