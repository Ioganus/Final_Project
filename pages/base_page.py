from urllib.parse import urlparse
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    """
    Родительский класс для всех страниц.
    Содержащий общие методы и утилиты для всех страниц.
    """

    def __init__(self, driver: WebDriver, url=''):
        self.driver = driver
        self.driver.get(url)

    def find(self, locator, time=10):
        """Метод поиска элемента на странице."""
        WebDriverWait(self.driver, time).until(
            EC.presence_of_element_located(locator), message=f"Не удалось найти элемент по локатору {locator}")
        return self.driver.find_element(*locator)

    def switch_window(self, num=-1):
        """Метод переключения на другое окно браузера."""
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[num])

    def click(self, locator):
        """Метод клика по элементу на странице."""
        self.find(locator).click()

    def set(self, locator, value):
        """Метод ввода значения в поле на странице."""
        self.find(locator).clear()
        self.find(locator).send_keys(value)

    def get_text(self, locator):
        """Метод получения текста элемента на странице."""
        return self.find(locator).text

    def get_link(self):
        """Метод получения текущего URL страницы."""
        return self.driver.current_url

    def get_relative_link(self):
        """Метод получения относительного пути URL страницы."""
        url = urlparse(self.driver.current_url)
        return url.path
