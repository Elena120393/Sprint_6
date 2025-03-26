# Класс главной страницы

from pages.base_page import BasePage
from locators.faq_locators import FaqLocators
from locators.navigation_locators import NavigationLocators
from locators.order_locators import OrderLocators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class MainPage(BasePage):
    def __init__(self, driver):
        """
        Инициализация главной страницы.
        """
        super().__init__(driver)
        self.faq_locators = FaqLocators()
        self.navigation_locators = NavigationLocators()
        self.order_locators = OrderLocators()

    def scroll_to_faq_section(self):
        """
        Прокрутить страницу до раздела FAQ.
        """
        faq_section = self.find_element(self.faq_locators.FAQ_SECTION)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", faq_section)

    def click_question(self, question_text):
        """
        Нажать на вопрос в разделе FAQ.
        """
        # Формируем локатор с конкретным текстом вопроса
        question_locator = (
            self.faq_locators.QUESTION_BUTTON_TEMPLATE[0],
            self.faq_locators.QUESTION_BUTTON_TEMPLATE[1].format(question_text)
        )
        # Прокручиваем до раздела FAQ
        self.scroll_to_faq_section()
        # Кликаем по вопросу
        self.click_element(question_locator)

    def get_answer_text(self, question_text):
        """
        Получить текст ответа на вопрос.
        """
        # Формируем локатор с конкретным текстом вопроса
        answer_text_locator = (
            self.faq_locators.ANSWER_TEXT_TEMPLATE[0],
            self.faq_locators.ANSWER_TEXT_TEMPLATE[1].format(question_text)
        )
        # Ожидаем, пока ответ станет видимым
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(answer_text_locator)
        )
        # Возвращаем текст ответа
        return self.get_element_text(answer_text_locator)

    def is_answer_visible(self, question_text):
        """
        Проверить, видим ли ответ на вопрос.
        """
        # Формируем локатор с конкретным текстом вопроса
        answer_panel_locator = (
            self.faq_locators.ANSWER_PANEL_TEMPLATE[0],
            self.faq_locators.ANSWER_PANEL_TEMPLATE[1].format(question_text)
        )
        # Проверяем видимость ответа
        return self.is_element_visible(answer_panel_locator)

    def click_order_button_top(self):
        """
        Нажать на верхнюю кнопку "Заказать".
        """
        self.click_element(self.order_locators.ORDER_BUTTON_TOP)

    def scroll_to_bottom_order_button(self):
        """
        Прокрутить страницу к нижней кнопке "Заказать".
        """
        # Прокручиваем страницу вниз до конца
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Ждем, пока кнопка станет видимой
        try:
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.order_locators.ORDER_BUTTON_BOTTOM)
            )
        except:
            # Если кнопка не найдена, пробуем прокрутить еще немного
            self.driver.execute_script("window.scrollBy(0, 300);")
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.order_locators.ORDER_BUTTON_BOTTOM)
            )

    def click_order_button_bottom(self):
        """
        Нажать на нижнюю кнопку "Заказать".
        """
        # Прокручиваем до нижней кнопки
        bottom_button = self.find_element(self.order_locators.ORDER_BUTTON_BOTTOM)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", bottom_button)
        # Кликаем по кнопке
        self.click_element(self.order_locators.ORDER_BUTTON_BOTTOM)

    def click_scooter_logo(self):
        """
        Нажать на логотип Самоката.
        """
        self.click_element(self.navigation_locators.SCOOTER_LOGO)

    def click_yandex_logo(self):
        """
        Нажать на логотип Яндекса.
        """
        self.click_element(self.navigation_locators.YANDEX_LOGO)