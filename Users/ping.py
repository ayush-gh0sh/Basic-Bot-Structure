import discord
from discord.ext import commands
import time
import datetime

class Ping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.start_time = time.time()

    def get_status(self, latency):
        if latency < 100:
            return "🟢 Excellent"
        elif latency < 200:
            return "🟡 Good"
        else:
            return "🔴 Poor"

    def format_uptime(self):
        seconds = int(time.time() - self.start_time)
        return str(datetime.timedelta(seconds=seconds))

    @commands.command(name="ping", help="Check bot performance & latency")
    async def ping(self, ctx: commands.Context):
        start = time.perf_counter()

        msg = await ctx.reply("🏓 Calculating latency...", mention_author=False)

        end = time.perf_counter()

        # ⚡ Latencies
        roundtrip = (end - start) * 1000
        websocket = self.bot.latency * 1000

        status = self.get_status(websocket)
        now = int(time.time())

        embed = discord.Embed(
            title="🏓 Pong! • Bot Performance",
            description=(
                f"╭─ **📊 Live Status**\n"
                f"│ {status}\n"
                f"╰───────────────\n\n"
                f"🕒 **Checked:** <t:{now}:F>\n"
                f"⏳ **Relative:** <t:{now}:R>"
            ),
            color=0x5DEFF9
        )

        # ⚡ Latency
        embed.add_field(
            name="⚡ Latency",
            value=(
                f"**WebSocket:** `{websocket:.2f} ms`\n"
                f"**Roundtrip:** `{roundtrip:.2f} ms`"
            ),
            inline=True
        )

        # 🧠 Stats
        embed.add_field(
            name="🧠 Bot Stats",
            value=(
                f"**Servers:** `{len(self.bot.guilds)}`\n"
                f"**Users:** `{len(self.bot.users)}`"
            ),
            inline=True
        )

        # ⏱️ Uptime
        embed.add_field(
            name="⏱️ Uptime",
            value=f"`{self.format_uptime()}`",
            inline=False
        )

        # 👤 User
        embed.add_field(
            name="👤 Requested By",
            value=ctx.author.mention,
            inline=True
        )

        # 📍 Channel
        embed.add_field(
            name="📍 Channel",
            value=ctx.channel.mention,
            inline=True
        )

        # 🎨 Styling
        embed.set_thumbnail(url=ctx.author.display_avatar.url)
        embed.set_footer(
            text=f"{self.bot.user.name} • Real-time Monitoring",
            icon_url=self.bot.user.display_avatar.url
        )

        await msg.edit(content=None, embed=embed)


async def setup(bot):
    await bot.add_cog(Ping(bot))
