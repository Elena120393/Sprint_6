
import pytest
import allure
from pages.main_page import MainPage
from pages.order_page import OrderPage
from data.order_data import ORDER_DATA
from urls import BASE_URL

@allure.epic("Yandex Scooter")
@allure.feature("Order Process")
class TestOrder:

    @allure.story("Order from top button")
    @allure.title("Complete order using top button")
    @allure.description("Test checks the complete order flow using the top order button")
    @pytest.mark.parametrize("order_data", ORDER_DATA)
    def test_order_from_top_button(self, driver, order_data):
        """
        Test ordering a scooter using the top order button.

        :param driver: WebDriver instance
        :param order_data: Test data for the order
        """
        # Initialize pages
        main_page = MainPage(driver)
        order_page = OrderPage(driver)

        with allure.step("Open main page"):
            main_page.open(BASE_URL)

        with allure.step("Click on top order button"):
            main_page.click_order_button_top()

        # Fill in the first order form
        with allure.step("Fill in personal information"):
            order_page.fill_personal_info(
                name=order_data['name'],
                surname=order_data['surname'],
                address=order_data['address'],
                metro_station=order_data['metro_station'],
                phone=order_data['phone']
            )

        with allure.step("Click Next button"):
            order_page.click_next_button()

        # Fill in the second order form
        with allure.step("Fill in rental details"):
            order_page.fill_rental_info(
                delivery_date=order_data['delivery_date'],
                rental_period=order_data['rental_period'],
                color=order_data['color'],
                comment=order_data['comment']
            )

        with allure.step("Click Order button"):
            order_page.click_order_button()

        with allure.step("Confirm order"):
            order_page.confirm_order()

        # Verify the order was successful
        with allure.step("Verify order success modal is displayed"):
            # Take a screenshot of the result
            allure.attach(
                driver.get_screenshot_as_png(),
                name="order_result",
                attachment_type=allure.attachment_type.PNG
            )

            assert order_page.is_order_success_modal_visible(), "Order success modal is not displayed"

            # Verify the order number is present in the success text
            success_text = order_page.get_order_success_text()
            assert "Номер заказа:" in success_text, f"Order success text does not contain order number: {success_text}"

    @allure.story("Order from bottom button")
    @allure.title("Complete order using bottom button")
    @allure.description("Test checks the complete order flow using the bottom order button")
    @pytest.mark.parametrize("order_data", ORDER_DATA)
    def test_order_from_bottom_button(self, driver, order_data):
        """
        Test ordering a scooter using the bottom order button.

        :param driver: WebDriver instance
        :param order_data: Test data for the order
        """
        # Initialize pages
        main_page = MainPage(driver)
        order_page = OrderPage(driver)

        with allure.step("Open main page"):
            main_page.open(BASE_URL)

        with allure.step("Scroll to bottom order button"):
            main_page.scroll_to_bottom_order_button()

        with allure.step("Click on bottom order button"):
            main_page.click_order_button_bottom()

        # Fill in the first order form
        with allure.step("Fill in personal information"):
            order_page.fill_personal_info(
                name=order_data['name'],
                surname=order_data['surname'],
                address=order_data['address'],
                metro_station=order_data['metro_station'],
                phone=order_data['phone']
            )

        with allure.step("Click Next button"):
            order_page.click_next_button()

        # Fill in the second order form
        with allure.step("Fill in rental details"):
            order_page.fill_rental_info(
                delivery_date=order_data['delivery_date'],
                rental_period=order_data['rental_period'],
                color=order_data['color'],
                comment=order_data['comment']
            )

        with allure.step("Click Order button"):
            order_page.click_order_button()

        with allure.step("Confirm order"):
            order_page.confirm_order()

        # Verify the order was successful
        with allure.step("Verify order success modal is displayed"):
            # Take a screenshot of the result
            allure.attach(
                driver.get_screenshot_as_png(),
                name="order_result",
                attachment_type=allure.attachment_type.PNG
            )

            assert order_page.is_order_success_modal_visible(), "Order success modal is not displayed"

            # Verify the order number is present in the success text
            success_text = order_page.get_order_success_text()
            assert "Номер заказа:" in success_text, f"Order success text does not contain order number: {success_text}"
