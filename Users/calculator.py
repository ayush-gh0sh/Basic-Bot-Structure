import discord
from discord.ext import commands
import math
import traceback

class Calculator(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        self.safe_dict = {
            "sqrt": math.sqrt,
            "pow": pow,
            "abs": abs,
            "round": round,
            "ceil": math.ceil,
            "floor": math.floor,
            "pi": math.pi,
            "e": math.e
        }

    def safe_eval(self, expr: str):
        expr = expr.replace("^", "**")

        allowed = "0123456789+-*/(). ,"
        for char in expr:
            if char not in allowed and not char.isalpha():
                raise ValueError("Invalid input")

        return eval(expr, {"__builtins__": None}, self.safe_dict)

    @commands.command(name="calc", help="Calculate expressions")
    async def calc(self, ctx: commands.Context, *, expression: str):
        try:
            result = self.safe_eval(expression)

        except Exception as e:
            # ❌ Terminal Error (Full Debug)
            print("\n[CALC ERROR]")
            print(f"Expression: {expression}")
            traceback.print_exc()
            print("-" * 40)

            # 👤 Clean user message
            return await ctx.reply(
                "❌ Invalid calculation",
                mention_author=False
            )

        embed = discord.Embed(
            title="🧮 Calculator",
            description=(
                f"```ansi\nCalculation Complete\n```\n"
                f"**➤ Input**\n`{expression}`\n\n"
                f"**➤ Output**\n`{result}`"
            ),
            color=0x5DEFF9
        )

        embed.set_thumbnail(url=ctx.author.display_avatar.url)

        if ctx.guild:
            embed.set_footer(
                text=ctx.guild.name,
                icon_url=ctx.guild.icon.url if ctx.guild.icon else None
            )
        else:
            embed.set_footer(text="Direct Messages")

        await ctx.reply(embed=embed, mention_author=False)


async def setup(bot):
    await bot.add_cog(Calculator(bot))
