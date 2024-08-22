from os import mkdir, path

from tgbot import tgbot

if __name__ == "__main__":
    if not path.exists("cache"):
        mkdir("cache")
    tgbot().run()
    print("Bot has been started")
