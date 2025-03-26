
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage
from locators.order_locators import OrderLocators


class OrderPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = OrderLocators()

    def fill_personal_info(self, name, surname, address, metro_station, phone):
        """
        Заполнить форму с персональными данными.
        """
        # Заполняем поле имени
        self.send_keys(self.locators.NAME_INPUT, name)

        # Заполняем поле фамилии
        self.send_keys(self.locators.SURNAME_INPUT, surname)

        # Заполняем поле адреса
        self.send_keys(self.locators.ADDRESS_INPUT, address)

        # Заполняем поле станции метро и выбираем из списка
        metro_input = self.find_element(self.locators.METRO_STATION_INPUT)
        metro_input.click()
        metro_input.send_keys(metro_station)

        # Ждем, пока появится выпадающий список с вариантами станций
        # Пробуем несколько вариантов локаторов для выбора станции метро
        metro_option_locators = [
            # Вариант 1: поиск по точному тексту
            (By.XPATH, self.locators.METRO_STATION_OPTION_EXACT[1].format(metro_station)),
            # Вариант 2: поиск по содержанию текста
            (By.XPATH, self.locators.METRO_STATION_OPTION_CONTAINS[1].format(metro_station)),
            # Вариант 3: поиск по li элементам
            (By.XPATH, self.locators.METRO_STATION_OPTION_LI[1].format(metro_station)),
            # Вариант 4: поиск первого элемента в выпадающем списке
            self.locators.METRO_STATION_FIRST_OPTION
        ]

        # Пробуем каждый локатор по очереди
        for locator in metro_option_locators:
            try:
                if self.is_element_visible(locator, timeout=2):
                    self.click_element(locator)
                    break
            except Exception:
                continue

        # Если не удалось выбрать станцию через клик, пробуем через Enter
        if not self.is_element_visible(self.locators.NEXT_BUTTON, timeout=1):
            metro_input.send_keys(Keys.ENTER)

        # Заполняем поле телефона
        self.send_keys(self.locators.PHONE_INPUT, phone)

    def click_next_button(self):
        """
        Нажать кнопку "Далее".
        """
        self.click_element(self.locators.NEXT_BUTTON)

    def fill_rental_info(self, delivery_date, rental_period, color, comment):
        """
        Заполнить форму с информацией об аренде.
        """
        # Заполняем поле даты доставки
        date_input = self.find_element(self.locators.DELIVERY_DATE_INPUT)
        date_input.click()
        date_input.send_keys(Keys.CONTROL + "a")  # Выделяем весь текст
        date_input.send_keys(delivery_date)  # Вводим новую дату
        date_input.send_keys(Keys.ENTER)  # Нажимаем Enter для подтверждения

        # Выбираем срок аренды
        self.click_element(self.locators.RENTAL_PERIOD_DROPDOWN)

        # Формируем локатор для конкретного периода аренды
        period_option_locator = (
            By.XPATH,
            self.locators.RENTAL_PERIOD_OPTION[1].format(rental_period)
        )

        # Ждем появления элемента и кликаем по нему
        self.wait_for_element_visible(period_option_locator)
        self.click_element(period_option_locator)

        # Выбираем цвет самоката на основе переданного значения
        color_id = self._get_color_id(color)
        # Исправлено: используем прямой XPath вместо COLOR_CHECKBOX
        color_checkbox_locator = (By.XPATH, f"//*[@id='{color_id}']")

        # Кликаем по чекбоксу цвета
        self.click_element(color_checkbox_locator)

        # Заполняем поле комментария
        if comment:
            self.send_keys(self.locators.COMMENT_INPUT, comment)

    def _get_color_id(self, color_name):
        """
        Получить ID чекбокса цвета на основе названия цвета.
        """
        # Используем словарь соответствия из локаторов
        return self.locators.COLOR_MAPPING.get(color_name, color_name)

    def click_order_button(self):
        """
        Нажать кнопку "Заказать" на форме заказа.
        """
        self.click_element(self.locators.ORDER_SUBMIT_BUTTON)

    def confirm_order(self):
        """
        Подтвердить заказ в модальном окне.
        """
        self.click_element(self.locators.CONFIRM_ORDER_BUTTON)

    def is_order_success_modal_visible(self):
        """
        Проверить, видно ли модальное окно успешного заказа.
        """
        return self.is_element_visible(self.locators.ORDER_SUCCESS_MODAL)

    def get_order_success_text(self):
        """
        Получить текст из модального окна успешного заказа.
        """
        return self.get_element_text(self.locators.ORDER_SUCCESS_TEXT)

    def wait_for_element_visible(self, locator, timeout=10):
        """
        Ожидать, пока элемент станет видимым.
        """
        from selenium.webdriver.support import expected_conditions as EC
        from selenium.webdriver.support.ui import WebDriverWait

        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator),
            message=f"Элемент не стал видимым с локатором: {locator}"
        )