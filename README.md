# eliKAASbot
This is eliKAASbot, a multi-purpose bot

For the cleverbot responses I'm using a libary called [Cleverbot](https://pypi.python.org/pypi/cleverbot)

## Installation

#### cd into your home directory
``` bash
cd ~
```
#### clone the respository
``` bash
git clone https://github.com/elisaado/eliKAASbot.git
```
#### Install the dependencies
``` bash
pip3 install cleverbot
pip3 install python-telegram-bot --upgrade
```
#### cd Into the directory of eliKAASbot
``` bash
cd eliKAASbot
```
#### Now you need to edit the config file! Edit the ownerId, botName, etc. 
Of course you can edit it with whatever editor you want but I find nano the simplest.

``` bash
nano config.config
```

You can call the config file whatever you want but when you start the bot, give the config file as an argument like I will show you below

#### Now you can start the bot with
``` bash
python3 main.py "config.config" # that 'config.config' could be changed to everything but it must match the name you gave the config file
```

### The config file

| Property            | Line number |
|---------------------|-------------|
| Bot Token           | 2           |
| Name of the bot     | 4           |
| The ID of the Owner | 6           |
