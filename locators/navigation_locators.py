# Локаторы для элементов навигации

from selenium.webdriver.common.by import By


class NavigationLocators:
    # Логотип Самоката
    SCOOTER_LOGO = (By.CLASS_NAME, "Header_LogoScooter__3lsAR")

    # Логотип Яндекса
    YANDEX_LOGO = (By.CLASS_NAME, "Header_LogoYandex__3TSOI")