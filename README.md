# GestBot

## Prerequisite

Python version : *3.10.9*

You will need a bot and is token 
You can follow this documentation to do it 
https://docs.pycord.dev/en/stable/discord.html

## Install

``` Bash
python -m pip install -r requirements.txt
```
make a **.env** file with
``` Env
SQL_HOSTNAME = "localhost"
SQL_PORT = "3306"
SQL_USERNAME = ""
SQL_USER_PASSWORD = ""
SQL_DB_NAME = "GestBot"
BOT_TOKEN = ""
```

## Folder Structure

```
    GestBot
    |
    ├── cogs                    # Cogs files for commands
    ├── doc                     # Documentation files (alternatively `docs`)
    ├── lib                     # Library files for class
    ├── test                    # Automated tests (alternatively `spec` or `tests`)
    ├── data                    # Data file like img or font, ect...
    ├── main.py                 # Bot base file
    ├── requirements.txt
    ├── LICENSE
    └── README.md
```

## Test


## License

[GPLv3](https://choosealicense.com/licenses/gpl-3.0/)
