FROM python:3
FROM gorialis/discord.py

RUN mkdir -p /home/disbot/LeagueBot/src/bot
WORKDIR /home/disbot/LeagueBot/src/bot

COPY . .

CMD [ "python3", "discord_bot.py" ]