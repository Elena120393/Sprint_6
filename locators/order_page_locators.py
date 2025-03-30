from selenium.webdriver.common.by import By


class OrderPageLocators:
    # Личные данные
    NAME_INPUT = (By.XPATH, "//input[@placeholder='* Имя']")
    SURNAME_INPUT = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS_INPUT = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_STATION_INPUT = (By.XPATH, "//input[@placeholder='* Станция метро']")
    METRO_STATION_OPTION = (By.XPATH, "//div[contains(@class, 'select-search__select')]//div[1]")
    PHONE_INPUT = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']")

    # Детали аренды
    DELIVERY_DATE_INPUT = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    RENTAL_PERIOD_DROPDOWN = (By.CLASS_NAME, "Dropdown-root")
    RENTAL_PERIOD_OPTION = (By.XPATH, "//div[contains(@class, 'Dropdown-option') and text()='{}']")
    COMMENT_INPUT = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")

    # Кнопка заказа (исправлено)
    ORDER_BUTTON = (By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM']")
    CONFIRM_ORDER_BUTTON = (By.XPATH, "//button[text()='Да']")

    # Успешный заказ
    ORDER_SUCCESS_MODAL = (By.CLASS_NAME, "Order_Modal__YZ-d3")
    ORDER_SUCCESS_TEXT = (By.XPATH, "//div[contains(@class, 'Order_ModalHeader__3FDaJ')]")

    # Маппинг цветов
    COLOR_MAPPING = {
        "чёрный жемчуг": "black",
        "серая безысходность": "grey"
    }