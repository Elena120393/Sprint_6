# Локаторы для раздела FAQ

from selenium.webdriver.common.by import By


class FaqLocators:
    # Контейнер раздела FAQ
    FAQ_SECTION = (By.CLASS_NAME, "Home_FAQ__3uVm4")

    # Кнопки с вопросами (будут использоваться с форматированием для получения конкретного вопроса)
    QUESTION_BUTTON_TEMPLATE = (By.XPATH, "//div[contains(@class, 'accordion__button') and text()='{}']")

    # Панель с ответом (будет использоваться с форматированием для получения конкретной панели ответа)
    ANSWER_PANEL_TEMPLATE = (
    By.XPATH, "//div[contains(@class, 'accordion__button') and text()='{}']/parent::div/following-sibling::div")

    # Текст ответа (будет использоваться с форматированием для получения конкретного текста ответа)
    ANSWER_TEXT_TEMPLATE = (
    By.XPATH, "//div[contains(@class, 'accordion__button') and text()='{}']/parent::div/following-sibling::div/p")