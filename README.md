# Discord Translator Bot

This bot is written in pure python and uses Microsoft's Translate API's to translate the messages provided to it.

Using this bot is pretty straight forward as you just have to react to the message which you want to translate with a suitable flag emoji to language of which you want to translate the message.

The list of languages currently supported by this bot is 

![Help function of bot](https://res.cloudinary.com/dtldj8hpa/image/upload/v1574605347/projects/bot-help.jpg)

This project has a few dependencies which are discord-py and requests which if changed might cause the project to malfunction.

This is a ready to run bot if you are planning to run it on your own on heroku. But if you are on any other Continous Deployment Platform then you might have to make changes accordingly.

This project is built upon python3.6 and tried and tested on it. If you are running on any other version then you might face problems be sure to report them to me if you find any. I will be more than happy to help you out.

If you are planning to create your own seperate bot from this code you might wanna create an App on Discord Developer Portal and add a bot to your application and then add the bot key in keys.json file in the root directory of the folder.

You will also need to add your Microsoft Azure Translation Cognitive Services key to the keys.json file.

The working of app is as follows

![Working gif of the project](https://res.cloudinary.com/dtldj8hpa/video/upload/v1574606694/projects/TranslateBot.gif)

Or you can directly add the bot which i have kept running on heroku by clicking on this link and add it to the required server!

https://discordapp.com/oauth2/authorize?client_id=645821077901148203&scope=bot&permissions=1074203744
