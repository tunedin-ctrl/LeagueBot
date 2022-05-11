FROM python:3
FROM gorialis/discord.py

RUN mkdir -p /LeagueBot/src/bot
WORKDIR /LeagueBot/src/bot

COPY . .

CMD [ "python3", "discord_bot.py" ]