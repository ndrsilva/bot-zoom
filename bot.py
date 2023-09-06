"""..."""
import os
from src.BotZoom import BotZoom


def main():
    """..."""

    bot = BotZoom()
    email = os.getenv('EMAIL_ZOOM')
    password = os.getenv('PASSWORD_ZOOM')

    bot.execute_bot(email, password)


if __name__ == '__main__':
    main()
