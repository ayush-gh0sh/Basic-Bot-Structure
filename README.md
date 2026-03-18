🤖 Basic Discord Bot Structure (Python)

<p align="center">
  <img src="https://img.shields.io/badge/discord.py-2.3+-5865F2?style=for-the-badge&logo=discord" />
  <img src="https://img.shields.io/badge/python-3.10+-yellow?style=for-the-badge&logo=python" />
  <img src="https://img.shields.io/github/stars/ayush-gh0sh/Basic-Bot-Structure?style=for-the-badge" />
</p><p align="center">
  <b>Clean, role-based Discord bot with modular command loading + UI system.</b>
</p>

---

✨ Overview

This repository is built with a minimal but scalable architecture:

- 📂 Commands organized by folders (currently "users/")
- ⚙️ Automatic cog loader (no manual imports)
- 🧩 UI system separated (buttons, views, modals)
- 🚀 Easy to scale into large bots

---

📂 Current Structure

bot/
│
├── users/              # ✅ All user commands (auto-loaded)
│   ├── ping.py
│   └── calc.py
│
├── bot.py              # Main bot (loader system)
├── config.json
├── requirements.txt
└── README.md

---

🧠 Core System Explanation

📌 Command System ("users/")

- All files inside "users/" are loaded automatically
- Each file must:
  - be a Cog
  - contain a "setup()" function

async def setup(bot):
    await bot.add_cog(YourCog(bot))

---

📌 UI System ("ui/") ⚠️ IMPORTANT

This is where most people mess up — read carefully.

❌ These files are NOT loaded automatically:

- buttons
- views
- modals

👉 Because they do not contain "setup()"

---

🧩 How UI Actually Works

UI files are manually imported inside command files.

---

🔹 Example Flow

users/panel.py → ui/views.py → ui/buttons.py

---

🔹 Example Button Usage

"ui/buttons.py"

import discord

class MyButton(discord.ui.Button):
    def __init__(self):
        super().__init__(label="Click Me", style=discord.ButtonStyle.primary)

    async def callback(self, interaction: discord.Interaction):
        await interaction.response.send_message("Button clicked!", ephemeral=True)

---

"ui/views.py"

import discord
from ui.buttons import MyButton

class MyView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        self.add_item(MyButton())

---

"users/panel.py"

from discord.ext import commands
from ui.views import MyView

class Panel(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def panel(self, ctx):
        await ctx.send("Click below:", view=MyView())

async def setup(bot):
    await bot.add_cog(Panel(bot))

---

⚠️ VERY IMPORTANT RULES

✔️ Commands Folder ("users/")

- Must contain "setup()"
- Automatically loaded by bot

---

❌ UI Folder ("ui/")

- Must NOT contain "setup()"
- Never auto-loaded
- Only imported manually

---

❗ Why This Separation?

- Keeps bot structure clean
- Prevents loader errors
- Avoids ""no setup function"" issues
- Matches real production bots

---

🚀 Scaling Your Structure

🔹 Option 1 (Role-Based — Recommended)

bot/
├── users/
├── moderator/
├── admin/
├── ui/

---

🔹 Option 2 (Advanced Structure)

bot/
├── commands/
│   ├── users/
│   ├── moderator/
│   └── admin/
├── ui/

---

⚙️ Installation

git clone https://github.com/ayush-gh0sh/Basic-Bot-Structure.git
cd Basic-Bot-Structure
pip install -r requirements.txt

---

🔑 Configuration

{
  "token": "YOUR_BOT_TOKEN",
  "prefix": ".",
  "status": "Code By drunken.py"
}

---

▶️ Run

python bot.py

---

🎯 Design Philosophy

«Simple → Clean → Scalable»

This repo avoids:

- ❌ Over-complicated structure
- ❌ Unnecessary folders
- ❌ Confusing loaders

---

🔥 Why This Is Good

- ✅ Beginner friendly
- ✅ Clean GitHub structure
- ✅ Easy to extend
- ✅ No loader errors
- ✅ Proper UI separation

---

🚀 Future Upgrades

- Add role-based folders ("moderator/", "admin/")
- Add "events/" system
- Add database ("JSON / MongoDB")
- Add advanced UI (ticket system)

---

📜 License

MIT License

---

<p align="center">
  Built with ❤️ by Drunken
</p>
