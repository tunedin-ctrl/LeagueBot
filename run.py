from src.clients.bot_client import BotClient
import os
from pathlib import Path
from dotenv import load_dotenv
from src.cogs.greetings import Greetings
from src.error_handler.command_err import CommandErrHandler
from src.cogs.lol import Lol
from src.cogs.log import Log

""" main code to execute my discord bot"""
def main():
    # Token contained in local environment
    dotenv_path = Path('.env')
    load_dotenv(dotenv_path=dotenv_path)
    token = os.getenv('TOKEN')

    # Event listeners will be implemented later
    # intents = discord.Intents.default()
    # intents.members = True
    # intents.typing = False

    # init obj instance
    bot = BotClient (
        command_prefix='$',
        # intents=intents
    )
    bot.add_cog(Greetings(bot))
    bot.add_cog(CommandErrHandler(bot))
    bot.add_cog(Lol(bot))
    bot.add_cog(Log(bot))

    bot.run(token)

if __name__ == '__main__':
    main()