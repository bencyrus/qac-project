from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import NoSuchElementException


class BasePage:
    """
    BasePage is a class that contains all the common methods that are used in all the pages
    of the application. This class is inherited by all the page objects.
    """

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def _open_url(self, url: str) -> None:
        """
        Opens a URL in the browser.
        """
        self.driver.get(url)

    def _find(self, locator: tuple) -> WebElement:
        """
        Finds an element in the page.
        """
        return self.driver.find_element(*locator)

    def _wait_for_visible_element(self, locator: tuple, timeout: int = 10) -> None:
        """
        Waits for an element to be visible in the page.
        """
        WebDriverWait(self.driver, timeout).until(ec.visibility_of_element_located(locator))

    def _get_text(self, locator: tuple, timeout: int = 10) -> str:
        """
        Gets the text of an element.
        """
        self._wait_for_visible_element(locator, timeout)
        return self._find(locator).text

    def _type(self, locator: tuple, text: str, timeout: int = 10) -> None:
        """
        Types text in a text field.
        """
        self._wait_for_visible_element(locator, timeout)
        element = self._find(locator)
        element.clear()
        element.send_keys(text)

    def _click(self, locator: tuple, timeout: int = 10) -> None:
        """
        Clicks on a button.
        """
        self._wait_for_visible_element(locator, timeout)
        self._find(locator).click()

    def _is_displayed(self, locator: tuple, timeout: int = 10) -> bool:
        """
        Checks if an element is displayed in the page.
        """
        try:
            self._wait_for_visible_element(locator, timeout)
            return self._find(locator).is_displayed()
        except NoSuchElementException:
            return False