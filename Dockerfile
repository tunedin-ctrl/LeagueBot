FROM python:3
FROM gorialis/discord.py

RUN apt-get update
RUN apt-get install -y --no-install-recommends build-essential gcc
RUN pip install --upgrade pip

# RUN useradd --disabled-login --disabled-password myuser
RUN useradd -ms /bin/bash myuser
USER myuser
WORKDIR /home/myuser

ENV PATH="/home/myuser/.local/bin:${PATH}"
COPY --chown=myuser:myuser requirements.txt requirements.txt
RUN pip install --user -r requirements.txt

COPY --chown=myuser:myuser . .

CMD [ "python3", "run.py" ]