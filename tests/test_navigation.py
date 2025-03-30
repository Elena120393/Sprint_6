import time
import pytest
import allure
from pages.main_page import MainPage
from urls import BASE_URL, DZEN_URL


@allure.feature('Навигация')
@allure.story('Проверка навигации по логотипам')
class TestNavigation:

    @allure.title('Проверка перехода на главную страницу при клике на логотип Самоката')
    def test_scooter_logo_navigation(self, driver):
        """
        Тест перехода на главную страницу Самоката при клике на логотип Самоката.
        """
        # Открываем главную страницу
        with allure.step("Открываем главную страницу"):
            main_page = MainPage(driver)
            main_page.open(BASE_URL)

        # Переходим на страницу заказа (чтобы потом проверить возврат на главную)
        with allure.step("Переходим на страницу заказа"):
            main_page.click_order_button_top()

        # Проверяем, что мы не на главной странице (URL изменился)
        with allure.step("Проверяем, что URL изменился после перехода на страницу заказа"):
            assert driver.current_url != BASE_URL, "URL не изменился после перехода на страницу заказа"

        # Кликаем на логотип Самоката
        with allure.step("Кликаем на логотип Самоката"):
            main_page.click_scooter_logo()

        # Ждем, пока URL станет равным BASE_URL
        with allure.step(f"Ждем, пока URL станет равным {BASE_URL}"):
            main_page.wait_for_url_to_be(BASE_URL)

        # Проверяем, что мы вернулись на главную страницу
        with allure.step("Проверяем, что мы вернулись на главную страницу"):
            assert driver.current_url == BASE_URL, f"Ожидался URL {BASE_URL}, получен {driver.current_url}"


    @allure.title("Проверка на переход по новой вкладке")
    def test_yandex_button(self, driver):
        driver.get(BASE_URL)

        main_page = MainPage(driver)

        final_url = main_page.click_yandex_and_get_final_url()
        main_page.close_current_tab()

        assert "dzen.ru" in final_url, f"Финальный URL: {final_url}"