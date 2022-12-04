# PokeBot

This repository contains a simple Discord bot to get the EVs you obtain for fighting every pokemon. It has been updated until the newest Pokemon release (Scarlet/Violet).

## How to use it

To use this bot you will need Python 3.8 or higher. To create activate Discord developer tools follow the instructions on their official [documentation](https://discord.com/developers/docs/intro). This bot is based on the [discord.py](https://discordpy.readthedocs.io/en/stable/) library. I have collected all the necessary packages on the *requirements.txt* file, so no need to install discord.py alone. Use:

> `python3 -m pip install -r requirements.txt`

If you are using this on Windows use this instead:

> `py -3 -m pip install -r requirements.txt`

To run the bot in your local PC change the `"your token"` part on the code for your token value generated on the Discord Developer Window. I recommend adding a *.venv* on the folder containing all the necessary token values under different names, so you do not need to hard write it in your code. The read for this environment variable is already implemented with **dotenv**, in the following lines:

```python3

load_dotenv(find_dotenv())
TOKEN = os.getenv('your token name')
```

To run the bot use the command:

> `python3 bot.py` or `py -3 .\bot.py`


Now you can start using the bot in your local PC. If you want to have the bot running continiously have a look at available internet servers to host Python code such as [Replit](https://replit.com/) or [Heroku](https://www.heroku.com/). [Here](https://medium.com/@linda0511ny/create-host-a-discord-bot-with-heroku-in-5-min-5cb0830d0ff2) you can find a nice tutorial for you to follow.


## Contents

All the data has been transfered to the Pokemon.csv inside the pokemonData folder. This new file contains more information about the stats and the evs. Included the Pokemons for the 9th Generation. The file takes as reference the csv files on the [pokemonData](https://github.com/lgreski/pokemonData) repository.

## Logs

 * **(30/11/22)** First commit
 * **(04/12/22)**: New data format for the information, easier to read and handle
 * **Coming soon**: Connection with more information of the Pokemons (similar to [PokeAPI](https://pokeapi.co/))
 * **Coming soon**: Improved message format

