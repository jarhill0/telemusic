# telemusic

A Telegram bot to stream music locally based on the suggestions of others. Must be run on the computer you wish to 
hear music from.

# Installation
```commandline
python3 -m pip install git+https://github.com/jarhill0/telemusic.git
```

# Usage

Create a new bot using [BotFather](telegram.me/botfather). Note the API key.

```commandline
telemusic set key 54321:whateveryourkeyis
telemusic run
```
Send `/id` to the bot, note your user ID, then send ctrl-C to stop the bot. For example, if your ID is 123456789:

```commandline
telemusic set id 123456789
```

Set your name with the bot, using one of the following:

```commandline
telemusic set name FirstName
telemusic set name "Full Name"
```

Optionally, set a channel the bot should broadcast to when the track is advanced:

```commandline
telemusic set channel 123456789
```

Finally, run the bot again:

```commandline
telemusic run
```

Anyone can add music to the queue by sending `/add [URL]`. You, as the owner, can play, pause, or skip tracks by 
sending `/play`, `/pause`, or `/skip`, respectively.