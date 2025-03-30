from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import allure
from selenium.webdriver.common.keys import Keys


class OrderPage(BasePage):
    @allure.step("Инициализация страницы заказа")
    def __init__(self, driver):
        super().__init__(driver)
        from locators.order_page_locators import OrderPageLocators
        self.locators = OrderPageLocators()

    @allure.step("Заполнить личные данные")
    def fill_personal_info(self, name, surname, address, metro_station, phone):
        """
        Заполнить форму с личными данными заказчика
        """
        self.send_keys(self.locators.NAME_INPUT, name)
        self.send_keys(self.locators.SURNAME_INPUT, surname)
        self.send_keys(self.locators.ADDRESS_INPUT, address)
        self._select_metro_station(metro_station)
        self.send_keys(self.locators.PHONE_INPUT, phone)

    @allure.step("Выбрать станцию метро: {station_name}")
    def _select_metro_station(self, station_name):
        """
        Выбрать станцию метро из выпадающего списка
        """
        self.click_element(self.locators.METRO_STATION_INPUT)
        self.send_keys(self.locators.METRO_STATION_INPUT, station_name)
        self.click_element(self.locators.METRO_STATION_OPTION)

    @allure.step("Нажать кнопку 'Далее'")
    def click_next_button(self):
        """
        Нажать кнопку "Далее" для перехода к следующему шагу заказа
        """
        self.click_element(self.locators.NEXT_BUTTON)

    @allure.step("Заполнить детали аренды")
    def fill_rental_info(self, delivery_date, rental_period, color, comment=None):
        """
        Заполнить форму с деталями аренды самоката
        """
        self._set_delivery_date(delivery_date)
        self._select_rental_period(rental_period)
        self._select_scooter_color(color)
        if comment:
            self.send_keys(self.locators.COMMENT_INPUT, comment)

    @allure.step("Установить дату доставки: {date}")
    def _set_delivery_date(self, date):
        """
        Установить дату доставки самоката
        """
        date_field = self.find_element(self.locators.DELIVERY_DATE_INPUT)
        date_field.send_keys(Keys.CONTROL + "a")
        date_field.send_keys(date)
        date_field.send_keys(Keys.ENTER)

    @allure.step("Выбрать срок аренды: {period}")
    def _select_rental_period(self, period):
        """
        Выбрать срок аренды самоката из выпадающего списка
        """
        self.click_element(self.locators.RENTAL_PERIOD_DROPDOWN)
        period_locator = (
            self.locators.RENTAL_PERIOD_OPTION[0],
            self.locators.RENTAL_PERIOD_OPTION[1].format(period)
        )
        self.click_element(period_locator)

    @allure.step("Выбрать цвет самоката: {color}")
    def _select_scooter_color(self, color):
        """
        Выбрать цвет самоката, используя словарь соответствия цветов
        """
        color_id = self.locators.COLOR_MAPPING.get(color.lower())
        if not color_id:
            raise ValueError(f"Неизвестный цвет: {color}")

        color_locator = (By.ID, color_id)
        self.click_element(color_locator)

    @allure.step("Нажать кнопку 'Заказать'")
    def click_order_button(self):
        """
        Нажать кнопку "Заказать" после заполнения формы
        """
        self.click_element(self.locators.ORDER_BUTTON )

    @allure.step("Нажать кнопку 'Заказать' (центральная)")
    def click_order_button_center(self):
        """
        Нажать кнопку "Заказать" после заполнения формы (центральная кнопка)
        """
        self.click_element(self.locators.ORDER_BUTTON )

    @allure.step("Подтвердить заказ")
    def confirm_order(self):
        """
        Подтвердить заказ в модальном окне
        """
        # Ожидаем появления модального окна
        self.wait_for_element_visible(self.locators.CONFIRM_ORDER_BUTTON)
        self.click_element(self.locators.CONFIRM_ORDER_BUTTON)

    @allure.step("Нажать кнопку подтверждения заказа")
    def click_confirm_order_button(self):
        """
        Нажать кнопку подтверждения заказа в модальном окне
        """
        self.wait_for_element_visible(self.locators.CONFIRM_ORDER_BUTTON)
        self.click_element(self.locators.CONFIRM_ORDER_BUTTON)

    @allure.step("Проверить видимость модального окна успешного заказа")
    def is_order_success_modal_visible(self, timeout=5):
        """
        Проверяет, отображается ли модальное окно успешного заказа
        :param timeout: время ожидания в секундах
        :return: True если окно видимо, False если не видимо
        """
        return self.is_element_visible(self.locators.ORDER_SUCCESS_MODAL, timeout=timeout)

    @allure.step("Получить текст успешного заказа")
    def get_order_success_text(self):
        """
        Получить текст сообщения об успешном заказе
        """
        return self.get_element_text(self.locators.ORDER_SUCCESS_TEXT)

    @allure.step("Получить номер заказа")
    def get_order_number(self):
        """
        Извлечь номер заказа из текста успешного заказа
        """
        success_text = self.get_order_success_text()
        if "Номер заказа:" in success_text:
            return success_text.split("Номер заказа:")[1].strip()
        return None