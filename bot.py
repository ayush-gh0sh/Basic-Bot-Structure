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

PREFIX = config["prefix"]
TOKEN = config["token"]
STATUS = config["status"]

# ==============================
# BOT SETUP
# ==============================
intents = discord.Intents.all()
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

            filepath = os.path.join(root, file).replace("\\", "/")

            # Remove "./"
            if filepath.startswith("./"):
                filepath = filepath[2:]

            module_path = filepath[:-3].replace("/", ".")

            try:
                # 🔍 Check if file has setup()
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
    print(f"⏭️ Skipped : {skipped}")
    print(f"❌ Failed  : {failed}")
    print("==============================\n")


# ==============================
# BOT EVENTS
# ==============================
@bot.event
async def on_ready():
    print(f"🤖 Logged in as {bot.user}")
    await bot.change_presence(activity=discord.Game(name=STATUS))

    # Sync slash commands
    try:
        synced = await bot.tree.sync()
        print(f"🌐 Synced {len(synced)} slash command(s)")
    except Exception as e:
        print(f"❌ Slash sync failed → {e}")


# ==============================
# MAIN START
# ==============================
async def main():
    async with bot:
        await load_cogs()
        await bot.start(TOKEN)

asyncio.run(main())
