# League Bot

```text
src/
├── __init__.py
├── apis/
│   ├── api_lol.py
│   ├── log_helper.py
│   └── mongodb/
│       ├── docker-compose.yml
│       ├── dockerfile
│       └── sudo
├── clients/
│   └── bot_client.py
├── cogs/
│   ├── greetings.py
│   ├── log.py
│   └── lol.py
├── echo.py
└── error_handler/
    ├── api_error.py
    └── command_err.py
```

### install dependencies
```code
pip3 install -r requirements.txt
```

## Run app:
```code

python3 run.py
or
docker build -t league_bot .
docker run league_bot or docker run -d league_bot in the background
```

## Additional Notes:
Add your own token in .env file
Docker hosting mongodb (NoSQL) instead of using a json file as storage sys

### Run mongodb on docker
go into /mongodb dir 
```code
ls: sudo docker ps -a
init: sudo docker-compose up -d
run: sudo docker exec -it mongodb bash
```
#### inside docker
run mongo to use db
