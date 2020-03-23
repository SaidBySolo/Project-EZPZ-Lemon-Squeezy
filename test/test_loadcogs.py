from Bot import main
import sys,os
os.path.abspath(os.path.join(os.path.dirname(__file__),os.pardir))

def test_load_cog():
    bot = main.initialize()
    failed_cogs = main.load_cogs(bot)
    assert(len(failed_cogs) == 0)
