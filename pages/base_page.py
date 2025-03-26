from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


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

    def find_element(self, locator, timeout=10):
        """
        Найти элемент с явным ожиданием.
        """
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator),
            message=f"Элемент не найден с локатором: {locator}"
        )

    def find_elements(self, locator, timeout=10):
        """
        Найти элементы с явным ожиданием.
        """
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_all_elements_located(locator),
            message=f"Элементы не найдены с локатором: {locator}"
        )

    def click_element(self, locator, timeout=10):
        """
        Кликнуть по элементу с явным ожиданием.
        """
        element = WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator),
            message=f"Элемент не кликабелен с локатором: {locator}"
        )
        element.click()

    def send_keys(self, locator, text, timeout=10):
        """
        Ввести текст в элемент с явным ожиданием.
        """
        element = WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator),
            message=f"Элемент не кликабелен с локатором: {locator}"
        )
        element.clear()
        element.send_keys(text)

    def is_element_visible(self, locator, timeout=10):
        """
        Проверить, видим ли элемент.
        """
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            return True
        except TimeoutException:
            return False

    def get_element_text(self, locator, timeout=10):
        """
        Получить текст элемента с явным ожиданием.
        """
        element = WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator),
            message=f"Элемент не видим с локатором: {locator}"
        )
        return element.text

    def wait_for_url_contains(self, url_part, timeout=10):
        """
        Ожидать, пока URL содержит указанную часть.
        """
        return WebDriverWait(self.driver, timeout).until(
            EC.url_contains(url_part),
            message=f"URL не содержит {url_part}"
        )

    def wait_for_url_to_be(self, url, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.url_to_be(url),
            message=f"URL не равен {url}"
        )

    def wait_for_url_contains_any_domain(self, domains, timeout=30):
        """
        Ожидать, пока URL будет содержать один из указанных доменов.
        """

        def url_contains_any_domain(driver):
            current_url = driver.current_url
            return any(domain in current_url for domain in domains)

        return WebDriverWait(self.driver, timeout).until(
            url_contains_any_domain,
            message=f"URL не содержит ни один из доменов: {domains}"
        )

    def switch_to_new_window(self):
        """
        Переключиться на новое окно/вкладку.
        """
        current_window = self.driver.current_window_handle
        all_windows = self.driver.window_handles
        for window in all_windows:
            if window != current_window:
                self.driver.switch_to.window(window)
                break

    def scroll_to_element(self, locator, timeout=10):
        """
        Прокрутить страницу до элемента.
        """
        element = self.find_element(locator, timeout)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        return element

    def wait_for_page_load(self, timeout=10):
        """
        Ожидать загрузки страницы.
        """
        WebDriverWait(self.driver, timeout).until(
            lambda d: d.execute_script("return document.readyState") == "complete",
            message="Страница не загрузилась полностью"
        )