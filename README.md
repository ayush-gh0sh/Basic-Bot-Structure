<!-- BANNER --><p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=5865F2&height=200&section=header&text=Discord%20Bot%20Structure&fontSize=40&fontColor=ffffff&animation=fadeIn" />
</p><h1 align="center">🤖 Basic Discord Bot Structure</h1><p align="center">
  A clean, scalable & production-ready Discord bot template using discord.py
</p><p align="center">
  <img src="https://img.shields.io/github/stars/ayush-gh0sh/Basic-Bot-Structure?style=for-the-badge&color=yellow" />
  <img src="https://img.shields.io/github/forks/ayush-gh0sh/Basic-Bot-Structure?style=for-the-badge&color=blue" />
  <img src="https://img.shields.io/github/license/ayush-gh0sh/Basic-Bot-Structure?style=for-the-badge&color=green" />
</p>

---

✨ Why This Repo?

Most beginner bots are:

- ❌ Messy
- ❌ Hard to scale
- ❌ Poorly structured

This repo solves that with:

- 📂 Clean modular architecture
- ⚡ Fast setup
- 🔁 Auto-loading commands
- 🧠 Easy to extend
- 🚀 Production-ready base

---

🚀 Features

- ⚡ Plug & Play Setup
- 📦 Cog-based command system
- 🔄 Auto command loader
- 🧱 Scalable architecture
- 🔐 Secure config handling
- 📁 Organized folder structure

---

📁 Project Structure
```
Basic-Bot-Structure/
│
├── bot.py              # Main bot file
├── config.json         # Configuration
├── requirements.txt    # Dependencies
│
├── Users/               # Commands
│   ├── ping.py
└   └── help.py
```
---

⚙️ Installation

1️⃣ Clone the Repo
```
git clone https://github.com/ayush-gh0sh/Basic-Bot-Structure.git
cd Basic-Bot-Structure
```
2️⃣ Install Requirements
```
pip install -r requirements.txt
```
3️⃣ Configure Bot
Edit "config.json":
```
{
  "token": "YOUR_BOT_TOKEN",
  "prefix": ".",
  "status": "Code By Drunken.py"
}
```
---

▶️ Run the Bot
```
python bot.py
```
---

📸 Preview

<p align="center">
  <img src="https://raw.githubusercontent.com/github/explore/main/topics/discord/discord.png" width="600"/>
</p>

---

📖 Example Commands
| Command | Description |
|--------|------------|
| `.ping` | Check bot latency |
| `.help` | Show commands |

---

🧠 How It Works

- "bot.py" → core entry point
- "cogs/" → all commands live here
- Auto-loader loads every cog dynamically
- Easy to scale without touching core

---

🔧 Add Your Own Command
```
from discord.ext import commands

class Example(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def hello(self, ctx):
        await ctx.send("Hello World!")

async def setup(bot):
    await bot.add_cog(Example(bot))
```
---

🔐 Security

⚠️ Never expose your bot token publicly

For production:
```
import os
TOKEN = os.getenv("TOKEN")
```
---

📈 Future Upgrades

- 🔥 Slash Commands
- 🎫 Ticket System
- 🤖 Auto Moderation
- 💰 Crypto Features
- 🌐 Web Dashboard

---

🤝 Contributing

1. Fork the repository
2. Create your branch
3. Commit changes
4. Open Pull Request

---

⭐ Show Support

If this helped you:

- ⭐ Star the repo
- 🍴 Fork it
- 🚀 Use it in your projects

---

<p align="center">
  Made with ❤️ by Drunken 
</p><p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=5865F2&height=120&section=footer"/>
</p>
