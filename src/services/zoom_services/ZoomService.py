"""..."""

import logging as logger
from src.services.zoom_services.TasksZoomService import TasksZoomService


class ZoomService:
    """..."""

    def __init__(self):
        """..."""

        logger.basicConfig(
            level=logger.DEBUG,
            format='%(asctime)s:-:%(name)s:-'
                   ':%(levelname)s:-:%(lineno)s:-:%(message)s',
            handlers=[logger.FileHandler('logger.txt', 'a'),
                      logger.StreamHandler()]
        )

        self.log = logger.getLogger(__name__)
        self.tasks_zoom_service = TasksZoomService()

    def login(self, email: str, password: str) -> None:
        """..."""

        self.tasks_zoom_service.start()
        dlg = self.tasks_zoom_service.connect()

        self.tasks_zoom_service.click_sign_in(dlg)
        self.tasks_zoom_service.insert_email(dlg, email)
        self.tasks_zoom_service.insert_password(dlg, password)
        self.tasks_zoom_service.click_sign_in(dlg)

        self.log.info('')  # TODO - Write the message.

    def is_logged_in(self) -> bool:
        """..."""
        pass
