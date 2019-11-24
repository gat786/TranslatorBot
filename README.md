# Discord Translator Bot

This bot is written in pure Python and uses Microsoft's Translate API's to translate the messages provided to it.

Using this bot is pretty straightforward. Simply react to the message that you would like to translate with a suitable flag emoji to represent the language into which you want to translate the message.

![Working gif of the project](https://res.cloudinary.com/dtldj8hpa/video/upload/v1574606694/projects/TranslateBot.gif)

The languages currently supported by this bot are: 

![Help function of bot](https://res.cloudinary.com/dtldj8hpa/image/upload/v1574605347/projects/bot-help.jpg)

This project has a few dependencies: discord-py, heroku and requests.

This is a ready to run bot, deployed using Heroku. If you are on any other Continous Deployment Platform then you may have to make changes accordingly.

This project is built upon Python3.6. If you are running on any other version then you may face problems so be sure to report them to me if you find any. I will be more than happy to help you out.

If you would like to develope a bot derived from this, you may want to create an App on Discord Developer Portal, add a bot to your application and add the bot key in the keys.json file in the applications root directory. You will also need to add your Microsoft Azure Translation Cognitive Services key to the keys.json file.

I have a copy of this bot deployed on Heroku. You can  add the bot to your server by clicking on this link:

https://discordapp.com/oauth2/authorize?client_id=645821077901148203&scope=bot&permissions=1074203744
