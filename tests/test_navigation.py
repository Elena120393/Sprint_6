# Тесты для навигации (логотипы)

import pytest
from pages.main_page import MainPage
from urls import BASE_URL, DZEN_URL


class TestNavigation:

    def test_scooter_logo_navigation(self, driver):
        """
        Тест перехода на главную страницу Самоката при клике на логотип Самоката.
        """
        # Открываем главную страницу
        main_page = MainPage(driver)
        main_page.open(BASE_URL)

        # Переходим на страницу заказа (чтобы потом проверить возврат на главную)
        main_page.click_order_button_top()

        # Проверяем, что мы не на главной странице (URL изменился)
        assert driver.current_url != BASE_URL, "URL не изменился после перехода на страницу заказа"

        # Кликаем на логотип Самоката
        main_page.click_scooter_logo()

        # Ждем, пока URL станет равным BASE_URL
        main_page.wait_for_url_to_be(BASE_URL)

        # Проверяем, что мы вернулись на главную страницу
        assert driver.current_url == BASE_URL, f"Ожидался URL {BASE_URL}, получен {driver.current_url}"

    def test_yandex_logo_navigation(self, driver):
        """
        Тест перехода на страницу Яндекса при клике на логотип Яндекса.
        """
        # Открываем главную страницу
        main_page = MainPage(driver)
        main_page.open(BASE_URL)

        # Кликаем на логотип Яндекса
        main_page.click_yandex_logo()

        # Переключаемся на новую вкладку
        main_page.switch_to_new_window()

        # Ждем загрузки страницы
        main_page.wait_for_page_load()

        # Ждем, пока URL будет содержать один из доменов Яндекса
        yandex_domains = ["ya.ru", "yandex.ru", "dzen.ru"]
        main_page.wait_for_url_contains_any_domain(yandex_domains, timeout=30)

        # Проверяем, что URL содержит домен Яндекса
        current_url = driver.current_url
        assert any(domain in current_url for domain in yandex_domains), \
            f"Ожидался URL, содержащий один из доменов {yandex_domains}, получен {current_url}"
