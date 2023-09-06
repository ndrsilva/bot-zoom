"""..."""
from pywinauto.keyboard import send_keys
import logging as logger


class KeyboardService:
    """..."""

    def __init__(self) -> None:
        """Write the message."""

        logger.basicConfig(
            level=logger.DEBUG,
            format='%(asctime)s:-:%(name)s:-'
                   ':%(levelname)s:-:%(lineno)s:-:%(message)s',
            handlers=[logger.FileHandler('logger.txt', 'a'),
                      logger.StreamHandler()]
        )

        self.log = logger.getLogger(__name__)

    @staticmethod
    def clear_field() -> None:
        """write the docstring."""

        send_keys('(^a)', pause=1)
        send_keys('{DEL}')

        return None

    @staticmethod
    def enter_the_text(text: str, pause: float = 0.15) -> None:
        """write the docstring."""

        send_keys(text, pause=pause)

        return None
