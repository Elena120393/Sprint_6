# Локаторы для страницы заказа

from selenium.webdriver.common.by import By


class OrderLocators:
    # Кнопки заказа
    ORDER_BUTTON_TOP = (By.CLASS_NAME, "Button_Button__ra12g")
    ORDER_BUTTON_BOTTOM = (By.XPATH, "//div[contains(@class, 'Home_FinishButton__1_cWm')]/button")

    # Первая форма заказа (личная информация)
    NAME_INPUT = (By.XPATH, "//input[@placeholder='* Имя']")
    SURNAME_INPUT = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS_INPUT = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_STATION_INPUT = (By.XPATH, "//input[@placeholder='* Станция метро']")
    METRO_STATION_OPTION = (By.XPATH, "//div[contains(@class, 'select-search__select')]//li[contains(text(), '{}')]")
    PHONE_INPUT = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']")

    # Вторая форма заказа (детали аренды)
    DELIVERY_DATE_INPUT = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    RENTAL_PERIOD_DROPDOWN = (By.CLASS_NAME, "Dropdown-root")
    RENTAL_PERIOD_OPTION = (By.XPATH, "//div[contains(@class, 'Dropdown-option') and text()='{}']")
    COLOR_CHECKBOX_TEMPLATE = (By.XPATH, "//label[text()='{}']/preceding-sibling::input")
    COMMENT_INPUT = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    ORDER_SUBMIT_BUTTON = (By.XPATH, "//div[contains(@class, 'Order_Buttons__1xGrp')]/button[text()='Заказать']")

    # Подтверждение заказа
    CONFIRM_ORDER_BUTTON = (By.XPATH, "//button[text()='Да']")

    # Модальное окно успешного заказа
    ORDER_SUCCESS_MODAL = (By.CLASS_NAME, "Order_Modal__YZ-d3")
    ORDER_SUCCESS_HEADER = (By.XPATH, "//div[contains(@class, 'Order_ModalHeader__3FDaJ')]")
    ORDER_SUCCESS_TEXT = (By.XPATH, "//div[contains(@class, 'Order_Text__2broi')]")

    # Локаторы для выбора станции метро
    METRO_STATION_OPTION_EXACT = (By.XPATH, "//div[contains(@class, 'select-search__select')]//div[text()='{}']")
    METRO_STATION_OPTION_CONTAINS = (
    By.XPATH, "//div[contains(@class, 'select-search__select')]//div[contains(text(), '{}')]")
    METRO_STATION_OPTION_LI = (By.XPATH, "//div[contains(@class, 'select-search__select')]//li[contains(text(), '{}')]")
    METRO_STATION_FIRST_OPTION = (By.XPATH, "//div[contains(@class, 'select-search__select')]//div[1]")

    # Словарь соответствия названий цветов и их ID
    COLOR_MAPPING = {
        "чёрный жемчуг": "black",
        "серая безысходность": "grey"
    }
