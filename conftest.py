import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options


@pytest.fixture(scope="function")
def driver():
    """
    Фикстура для создания и закрытия драйвера Firefox.

    :return: Экземпляр WebDriver
    """
    # Настройка опций Firefox
    firefox_options = Options()
    # firefox_options.add_argument("--headless")  # Раскомментируйте для запуска в headless режиме

    # Создание драйвера
    driver = webdriver.Firefox(options=firefox_options)
    driver.maximize_window()

    # Возвращаем драйвер для использования в тестах
    yield driver

    # Закрываем драйвер после завершения теста
    driver.quit()

# Удалены проблемные хуки, которые использовали _metadata
