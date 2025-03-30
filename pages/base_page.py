
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import allure


class BasePage:
    def __init__(self, driver):
        """
        Инициализация базовой страницы.
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self, url):
        """
        Открыть указанный URL.
        """
        self.driver.get(url)

    def find_element(self, locator):
        """
        Найти элемент с явным ожиданием.
        """
        return self.wait.until(
            EC.presence_of_element_located(locator),
            message=f"Элемент не найден: {locator}"
        )

    def find_elements(self, locator):
        """
        Найти элементы с явным ожиданием.
        """
        return self.wait.until(
            EC.presence_of_all_elements_located(locator),
            message=f"Элементы не найдены: {locator}"
        )

    def click_element(self, locator):
        """
        Кликнуть на элемент с явным ожиданием.
        """
        element = self.wait.until(
            EC.element_to_be_clickable(locator),
            message=f"Элемент не кликабелен: {locator}"
        )
        element.click()

    def send_keys(self, locator, text):
        """
        Ввести текст в элемент с явным ожиданием.
        """
        element = self.wait.until(
            EC.element_to_be_clickable(locator),
            message=f"Элемент не доступен для ввода: {locator}"
        )
        element.clear()
        element.send_keys(text)

    def is_element_visible(self, locator, timeout=10):
        """
        Пр��верить, видим ли элемент.
        :param locator: локатор элемента
        :param timeout: время ожидания в секундах
        :return: True если элемент видим, False если не видим
        """
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            return True
        except TimeoutException:
            return False

    def wait_for_element_visible(self, locator, timeout=10):
        """Wait for element to be visible and return it

        Args:
            locator: Locator tuple (By.XX, 'value')
            timeout: Maximum wait time in seconds

        Returns:
            WebElement: The visible element

        Raises:
            TimeoutException: If element doesn't become visible within timeout
        """
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator),
            message=f"Element not visible with locator: {locator}"
        )

    def get_element_text(self, locator):
        """
        Получить текст элемента с явным ожиданием.
        """
        element = self.wait.until(
            EC.visibility_of_element_located(locator),
            message=f"Элемент не видим: {locator}"
        )
        return element.text

    def wait_for_url_contains(self, url_part):
        """
        Ожидать, пока URL содержит указанную часть.
        """
        return self.wait.until(
            EC.url_contains(url_part),
            message=f"URL ��е содержит {url_part}"
        )

    def wait_for_url_to_be(self, url):
        """
        Ожидать, пока URL станет равным указанному.
        """
        return self.wait.until(
            EC.url_to_be(url),
            message=f"URL не равен {url}"
        )

    def wait_for_url_contains_any_domain(self, domains):
        """
        Ожидать, пока URL будет содержать один из указанных доменов.
        """
        def url_contains_any_domain(driver):
            current_url = driver.current_url
            return any(domain in current_url for domain in domains)

        return self.wait.until(
            url_contains_any_domain,
            message=f"URL не содержит ни один из доменов: {domains}"
        )

    def switch_to_new_tab(self):
        """
        Переключиться на новое окно/вкладку.
        """
        current_window = self.driver.current_window_handle
        for window in self.driver.window_handles:
            if window != current_window:
                self.driver.switch_to.window(window)
                break
        return self.driver.current_url

    def scroll_to_element(self, locator):
        """
        Прокрутить страницу до элемента.
        """
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        return element

    def get_url_after_redirect(self, timeout=100):
        WebDriverWait(self.driver, timeout).until(  # Получить URL
            lambda d: d.current_url != 'about:blank'
        )
        return self.driver.current_url

    def close_current_tab(self):
        """
        Закрыть текущую вкладку.
        """
        self.driver.close()
        if self.driver.window_handles:
            self.driver.switch_to.window(self.driver.window_handles[0])