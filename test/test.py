from ..Bot import bot

def test_load_cog():
    bot = bot.initialize()
    failed_cogs = bot.load_cogs(bot)
    assert(len(failed_cogs) == 0)