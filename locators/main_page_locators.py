
from selenium.webdriver.common.by import By


class MainPageLocators:
    # Кнопки заказа
    ORDER_BUTTON_TOP = (By.XPATH, "//button[contains(@class, 'Button_Button__ra12g') and text()='Заказать']")
    ORDER_BUTTON_BOTTOM = (By.XPATH, "//div[contains(@class, 'Home_FinishButton__1_cWm')]/button")

    # Логотипы
    SCOOTER_LOGO = (By.CLASS_NAME, "Header_LogoScooter__3lsAR")
    YANDEX_LOGO = (By.CLASS_NAME, "Header_LogoYandex__3TSOI")

    # FAQ

    FAQ_TEXT = (By.XPATH, "//div[text()='Вопросы о важном']")
    FAQ_QUESTIONS = (By.XPATH, "//div[contains(@class, 'accordion__button') and text()='{}']")
    FAQ_ANSWER = (
    By.XPATH, "//div[contains(@class, 'accordion__button') and text()='{}']/parent::div/following-sibling::div/p")