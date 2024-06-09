# About
PokeMMO Roamer Info (PRI) is a simple but relatively feature rich roamer tracker
for PokeMMO in the form of a Discord bot. The commandline version used as a
submodule can be found [here](https://github.com/LucasLyn/pokemmo-roamer-info).

## Status
❌ - Currently **__NOT__** hosted.

## Installation
### Adding bot to a server
Click [this link](https://discord.com/oauth2/authorize?client_id=1249020828985594026)
to add the bot to a server.

Simply select the desired server in the dropdown menu and press continue.

#### Custom emoji support
The bot automatically checks the server's custom emojis (both animated and static),
and uses them next to the respective roamer, if the emoji name matches the
roamer name in lowercase (eg. the emoji `:suicune:` will work, while `:Suicune:`,
`:SUICUNE:` etc. will **not**).

### Setting up a local copy
1. Make an application on the
[Discord developer portal](https://discord.com/developers/applications)
and generate a token.
2. Create a `token.env` file, and add the following line to it

```
BOT_TOKEN=TOKEN
```

Where `TOKEN` is the token you generated in step 1.

3. Install the requirements by running


```
$ pip install -r requirements.txt
```

## Usage
### Discord
Run `/roamers` with or without any additional arguments:

    $ /roamers

Or with any of the optional arguments (can be combined):

    $ /roamers [OPT] [VAL]

Where

```
[OPT]               [VAL]       
month               1-12        What month to base data on.
show_next_roamers   True/False  Whether to also print the next month of roamers.
```

### Running the bot
Run the bot with `pri-bot.py`:

    $ py pri-bot.py

## Media
![Using the base command without any optional parameters](https://i.imgur.com/T8i5v5H.gif)
![Using the optional month parameter](https://i.imgur.com/fdNB7L4.gif)
![Using both of the optional parameters for month and use_next_roamers](https://i.imgur.com/Z0phukM.gif)
