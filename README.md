# League Bot

src/
├── api/
├── clients/ 
│   └── bot_client.py
├── cogs/
│   └── greetings.py
├── echo.py
├── error_handler/
│   ├── api_error.py
│   └── command_err.py
└── run.py

### install dependencies
pip3 install -r requirements.txt

## Run app:
python3 run.py
or
docker build -t league_bot .
docker run league_bot or docker run -d league_bot in the background

## Additional Notes:
Add your own token in .env file
Docker hosting mongodb (NoSQL) instead of using a json file as storage sys

### Run mongodb on docker
go into /mongodb dir 
ls: sudo docker ps -a
init: sudo docker-compose up -d
run: sudo docker exec -it mongodb bash

#### inside docker
run mongodb to use it
