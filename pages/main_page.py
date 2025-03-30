
from selenium.common import TimeoutException
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
import allure

class MainPage(BasePage):
    @allure.step("Инициализация главной страницы")
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = MainPageLocators()

    @allure.step("Нажать на верхнюю кнопку 'Заказать'")
    def click_order_button_top(self):
        self.click_element(self.locators.ORDER_BUTTON_TOP)

    @allure.step("Нажать на нижнюю кнопку 'Заказать'")
    def click_order_button_bottom(self):
        self.scroll_to_element(self.locators.ORDER_BUTTON_BOTTOM)
        self.click_element(self.locators.ORDER_BUTTON_BOTTOM)

    @allure.step("Нажать на логотип Самоката")
    def click_scooter_logo(self):
        self.click_element(self.locators.SCOOTER_LOGO)

    @allure.step("Нажать кнопку Яндекса и получить итоговый URL")
    def click_yandex_and_get_final_url(self):
        self.click_element(self.locators.YANDEX_LOGO)
        self.switch_to_new_tab()
        return self.get_url_after_redirect()

    @allure.step("Прокрутить страницу к нижней кнопке 'Заказать'")
    def scroll_to_bottom_order_button(self):
        """
        Прокрутить страницу к нижней кнопке "Заказать".
        """
        # Прокручиваем страницу вниз до конца
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    @allure.step("Прокрутить к разделу FAQ")
    def scroll_to_faq_text(self):
        self.scroll_to_element(self.locators.FAQ_TEXT)

    @allure.step("Раскрыть вопрос FAQ")
    def expand_question(self, question_text):
        try:
            question_locator = (
                self.locators.FAQ_QUESTIONS[0],
                self.locators.FAQ_QUESTIONS[1].format(question_text)
            )
            self.scroll_to_element(question_locator)
            self.click_element(question_locator)
            return True
        except TimeoutException:
            available_questions = [q.text for q in self.find_elements(self.locators.FAQ_QUESTIONS)]
            raise ValueError(f"Вопрос '{question_text}' не найден. Доступные вопросы: {available_questions}")

    @allure.step("Получить текст ответа на вопрос")
    def get_answer_text(self, question_text):
        try:
            answer_locator = (
                self.locators.FAQ_ANSWER[0],
                self.locators.FAQ_ANSWER[1].format(question_text)
            )
            return self.get_element_text(answer_locator)
        except TimeoutException:
            raise ValueError(f"Ответ на вопрос '{question_text}' не найден или не отображается")