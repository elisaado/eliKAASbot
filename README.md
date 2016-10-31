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
nano config.json
```

#### Now you can start the bot with
``` bash
python3 main.py
```

### The config file
``` json
{
	"token" : "{your token here}",
	"botName" : "{botname here}",
	"ownerId" : "{Owner ID here}",
	"randomMessagesEnabled" : "{fill in, 'yes' or 'no'}",
	"randomMessages" : "{random messages should be formatted like this (TWO COMMA'S, witout spaces!): 'randomMessage1,,randomMessage2,,randomMessage3,,etc etc'}",
	"advertiseGroupLinkEnabled" : "{yes or no}",
	"groupLink" : "{Group link here, Only one is allowed}"
}
```
