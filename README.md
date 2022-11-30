# PokeBot

This repository contains a simple Discord bot to get the EVs you obtain for fighting every pokemon. It has been updated until the newest Pokemon release (Scarlet/Violet).

## How to use it

To use this bot you will need Python 3.8 or higher. To create activate Discord developer tools follow the instructions on their official [documentation](https://discord.com/developers/docs/intro). This bot is based on the [discord.py](https://discordpy.readthedocs.io/en/stable/) library. I have collected all the necessary packages on the *requirements.txt* file, so no need to install discord.py alone. Use:

> `python3 -m pip install -r requirements.txt`

If you are using this on Windows use this instead:

> `py -3 -m pip install -r requirements.txt`

To run the bot in your local PC change the `"your token"` part on the code for your token value generated on the Discord Developer Window. I recommend adding a *.venv* on the folder containing all the necessary token values under different names, so you do not need to hard write it in your code. The read for this environment variable is already implemented with **dotenv**, in the following lines:

```
python3

load_dotenv(find_dotenv())
TOKEN = os.getenv('your token name')
```

To run the bot use the command:

> `python3 bot.py` or `py -3 .\bot.py`


Now you can start using the bot in your local PC. If you want to have the bot running continiously have a look at available internet servers to host Python code such as [Replit](https://replit.com/) or [Heroku](https://www.heroku.com/). [Here](https://medium.com/@linda0511ny/create-host-a-discord-bot-with-heroku-in-5-min-5cb0830d0ff2) you can find a nice tutorial for you to follow.


## Contents

The file *evs_poke.txt* contains all the information for evs of the pokemons. Right now this is the best way I have to handle this data. However, I will like to make a much more cleaner data structure on the future to share this data and for faster reading. If you are interested, every Pokemon's information is spread across 10 lines, so we use the *chunker* function to get these blocks. *utils.py* contains all this necessary functions to read and reformat the data to something more understandable for us.

## Logs

 * **(30/11/22)** First commit
 * **Coming soon**: New data format for the information, easier to read and handle
 * **Coming soon**: Connection with more information of the Pokemons (similar to [PokeAPI](https://pokeapi.co/))
 * **Coming soon**: Improved message format

