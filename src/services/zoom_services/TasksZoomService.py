from dotenv import load_dotenv
import logging as logger
from typing import Union

from pywinauto import Application
from pywinauto.application import WindowSpecification
from pywinauto import ElementNotFoundError
from pywinauto.timings import wait_until
from pywinauto.timings import TimeoutError

from src.services.KeyboardService import KeyboardService


class TasksZoomService:
    """..."""

    def __init__(self) -> None:
        """Write the message."""

        load_dotenv()
        logger.basicConfig(
            level=logger.DEBUG,
            format='%(asctime)s:-:%(name)s:-'
                   ':%(levelname)s:-:%(lineno)s:-:%(message)s',
            handlers=[logger.FileHandler('logger.txt', 'a'),
                      logger.StreamHandler()]
        )

        self.log = logger.getLogger(__name__)
        self._keyboard = KeyboardService()

    def start(self) -> None:
        """
        Start the zoom.

        Return:
        -------
            None

        Raises:
        -------
            ElementNotFoundError:
                The login window did not appear.

            TimeoutError:
                The login window did not appear within the time limit.

            Exception:
                Error starting 'Zoom'.
        """

        try:
            app = Application(backend="uia").start("Zoom", timeout=45)
            dlg = app.window(title="Zoom")

            wait_until(
                func=lambda: dlg.exists() and dlg.is_visible(),
                timeout=45,
                retry_interval=0.5
            )

            dlg.set_focus()

            self.log.info("Opening the Zoom.")

        except ElementNotFoundError:
            self.log.error(
                "The login window did not appear.")
            raise

        except TimeoutError:
            self.log.error(
                "The login window did not appear within the time limit.")
            raise

        except Exception as err:
            self.log.error(
                f"Error starting 'Zoom'.\n Err: {err}")
            raise

    def connect(self) -> Union[WindowSpecification, None]:
        """
        Connect with main zoom window.

        Return:
        -------
            dlg (Union[WindowSpecification, None]):
                Returns window connection if all goes well or none.

        Raises:
        -------
            ElementNotFoundError:
                The login window did not appear.

            TimeoutError:
                The login window did not appear within the time limit.

            Exception:
                Error connected to main window.
        """

        try:
            app = Application(backend="uia"). \
                connect(title='Zoom', timeout=45)
            dlg = app.window(title="Zoom")

            wait_until(
                func=lambda: dlg.exists() and dlg.is_visible(),
                timeout=45,
                retry_interval=0.5
            )

            dlg.set_focus()

            dlg.maximize()

            self.log.info(
                "Successfully connected to main window.")

            return dlg

        except ElementNotFoundError:
            self.log.error(
                "The main window did not appear."
            )
            raise

        except TimeoutError:
            self.log.error(
                "Main window did not appear within the time limit.")
            raise

        except Exception as err:
            self.log.error(
                f"Error connected to main window.\n Err: {err}")
            raise

    def click_sign_in(self, dlg: WindowSpecification) -> None:
        """
        Click on the button sign in.

        Parameter:
        -----------
            dlg (WindowSpecification):
                Login window.

        Return:
        -------
            None

        Raises
        -------
            ElementNotFoundError:
                The button 'Sign in' did not appear.

            TimeoutError:
                The button 'Sign in' did not appear within the time limit.

            Exception:
                Unexpected error on 'Sign in' button.
        """

        try:
            btn = dlg.child_window(
                title="Sign In",
                control_type="Button"
            )

            wait_until(
                func=lambda: btn.exists() and btn.is_visible(),
                timeout=30,
                retry_interval=0.5
            )

            btn.click_input()

            self.log.info("Click 'Sign in' button")
            return None

        except ElementNotFoundError:
            self.log.error("The button 'Sign in' did not appear.")
            raise

        except TimeoutError:
            self.log.error("The button 'Sign in' did not appear within the time limit.")
            raise

        except Exception as err:
            self.log.error(f"Unexpected error on 'Sign in' button.\n{err}")
            raise

    def insert_email(self, dlg: WindowSpecification, email: str) -> None:
        """
        Insert the e-mail.

        Paramenters:
        ------------
            dlg (WindowSpecification):
                Login Window.

            email (str):
                E-mail to access zoom account.

        Return:
        -------
            None
        """

        self._select_email_field(dlg)
        self._clear_field_email()
        self._enter_the_email(email)

        return None

    def _select_email_field(self, dlg: WindowSpecification) -> None:
        """Write the docstring."""

        try:
            field = dlg.child_window(
                title="Enter your email",
                control_type="Edit"
            )

            wait_until(
                func=lambda: field.exists() and field.is_visible(),
                timeout=30,
                retry_interval=0.5
            )

            field.click_input()

            self.log.info("")  # TODO - Write the message.
            return None

        except ElementNotFoundError:
            self.log.error("")  # TODO - Write the message.
            raise

        except TimeoutError:
            self.log.error("")  # TODO - Write the message.
            raise

        except Exception as err:
            self.log.error(err)  # TODO - Write the message.
            raise

    def _clear_field_email(self) -> None:
        """write the docstring."""

        self._keyboard.clear_field()

        self.log.info('')  # TODO - Write the message.
        return None

    def _enter_the_email(self, email: str) -> None:
        """write the docstring."""

        self._keyboard.enter_the_text(email)

        self.log.info('')  # TODO - Write the message.
        return None

    def insert_password(self, dlg: WindowSpecification, password: str) -> None:
        """write the docstring."""

        self._select_password_field(dlg)
        self._clear_field_password()
        self._enter_the_password(password)

        return None

    def _select_password_field(self, dlg: WindowSpecification) -> None:
        """Write the docstring."""

        try:
            field = dlg.child_window(
                title="Enter your password",
                control_type="Edit"
            )

            wait_until(
                func=lambda: field.exists() and field.is_visible(),
                timeout=30,
                retry_interval=0.5
            )

            field.click_input()

            self.log.info("")  # TODO - Write the message.
            return None

        except ElementNotFoundError:
            self.log.error("")  # TODO - Write the message.
            raise

        except TimeoutError:
            self.log.error("")  # TODO - Write the message.
            raise

        except Exception as err:
            self.log.error(err)  # TODO - Write the message.
            raise

    def _clear_field_password(self) -> None:
        """write the docstring."""

        self._keyboard.clear_field()

        self.log.info('')  # TODO - Write the message.
        return None

    def _enter_the_password(self, password: str) -> None:
        """Write the docstring."""

        self._keyboard.enter_the_text(password)

        self.log.info('')  # TODO - Write the message.
        return None

    @staticmethod
    def verify_login() -> bool:
        """Write the docstring."""

        # TODO
        return True
