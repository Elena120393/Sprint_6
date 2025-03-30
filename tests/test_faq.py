
# Тесты для раздела FAQ (вопросы о важном)

from data.faq_data import FAQ_DATA
from urls import BASE_URL
from pages.main_page import MainPage
import pytest
import allure

class TestQuestions:
    @allure.title("Проверка ответов в разделе FAQ")
    @pytest.mark.parametrize("faq_item", FAQ_DATA)
    def test_faq_answer(self, driver, faq_item):
        main_page = MainPage(driver)
        driver.get(BASE_URL)

        main_page.scroll_to_faq_text() # Прокрутка к FAQ
        main_page.expand_question(faq_item["question"]) # Раскрываем вопрос и получаем ответ
        actual_answer = main_page.get_answer_text(faq_item["question"])

        assert actual_answer == faq_item["answer"], \
            (f"Для вопроса '{faq_item['question']}'\n"
            f"Ожидался ответ: '{faq_item['answer']}'\n"  # Проверка ответа
            f"Получен ответ: '{actual_answer}'")