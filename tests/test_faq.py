# Тесты для раздела FAQ (вопросы о важном)

import pytest
import allure
from pages.main_page import MainPage
from data.faq_data import FAQ_DATA
from urls import BASE_URL


@allure.feature('FAQ')
@allure.story('Проверка вопросов и ответов в разделе "Вопросы о важном"')
class TestFaq:

    @allure.title('Открытие главной страницы')
    def test_open_main_page(self, driver):
        """
        Тест открытия главной страницы.
        """
        main_page = MainPage(driver)
        main_page.open(BASE_URL)


        assert driver.current_url == BASE_URL, f"Ожидался URL {BASE_URL}, получен {driver.current_url}"

    @allure.title('Проверка видимости раздела FAQ')
    def test_faq_section_visible(self, driver):
        """
        Тест видимости раздела FAQ.
        """
        main_page = MainPage(driver)
        main_page.open(BASE_URL)
        main_page.scroll_to_faq_section()


        assert main_page.is_element_visible(main_page.faq_locators.FAQ_SECTION), "Раздел FAQ не виден на странице"

    @pytest.mark.parametrize("faq_item", FAQ_DATA)
    @allure.title('Проверка вопроса: {faq_item["question"]}')
    def test_faq_question_answer(self, driver, faq_item):
        """
        Тест проверки вопроса и ответа в разделе FAQ.
        """
        question = faq_item["question"]
        expected_answer = faq_item["answer"]

        main_page = MainPage(driver)
        main_page.open(BASE_URL)


        main_page.scroll_to_faq_section()


        assert not main_page.is_answer_visible(question), f"Ответ на вопрос '{question}' виден до клика"


        with allure.step(f"Нажимаем на вопрос: {question}"):
            main_page.click_question(question)


        with allure.step(f"Проверяем, что ответ виден"):
            assert main_page.is_answer_visible(question), f"Ответ на вопрос '{question}' не виден после клика"


        with allure.step(f"Проверяем текст ответа"):
            actual_answer = main_page.get_answer_text(question)
            assert actual_answer == expected_answer, f"Ожидался ответ '{expected_answer}', получен '{actual_answer}'"