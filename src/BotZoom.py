"""..."""
import logging as logger
from src.services.zoom_services.ZoomService import ZoomService


class BotZoom:
    """..."""

    def __init__(self) -> None:
        """..."""

        logger.basicConfig(
            level=logger.DEBUG,
            format='%(asctime)s:-:%(name)s:-'
                   ':%(levelname)s:-:%(lineno)s:-:%(message)s',
            handlers=[logger.FileHandler('logger.txt', 'a'),
                      logger.StreamHandler()]
        )

        self.zoom_service = ZoomService()

    def execute_bot(self, email: str, password: str) -> str:
        """..."""

        self.zoom_service.login(email, password)
        return ''
