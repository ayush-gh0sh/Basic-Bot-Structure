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

    @commands.command(name="ping", help="Check bot latency")
    async def ping(self, ctx: commands.Context):
        start = time.perf_counter()

        msg = await ctx.reply("🏓 Pinging...", mention_author=False)

        end = time.perf_counter()

        websocket = self.bot.latency * 1000
        roundtrip = (end - start) * 1000

        status = self.get_status(websocket)
        now = int(time.time())

        embed = discord.Embed(
            title="🏓 Pong",
            description=(
                f"**{status}**\n\n"
                f"⚡ `{websocket:.0f} ms` • 🌐 `{roundtrip:.0f} ms`\n\n"
                f"⏱️ Uptime: `{self.format_uptime()}`\n"
                f"🕒 <t:{now}:R>"
            ),
            color=0x5DEFF9
        )

        # Minimal clean stats
        embed.set_footer(
            text=f"{ctx.guild.name if ctx.guild else 'Direct Messages'}",
            icon_url=ctx.guild.icon.url if ctx.guild and ctx.guild.icon else None
        )

        embed.set_thumbnail(url=self.bot.user.display_avatar.url)

        await msg.edit(content=None, embed=embed)


async def setup(bot):
    await bot.add_cog(Ping(bot))
