import pytest
import time


@pytest.mark.usefixtures('setup1')
class TestCart:

    # def test_cart_quantity(self):
    #     for n in range(1, 7):
    #         self.inventory_page.click_on_element(n)
    #         time.sleep(1)
    #     assert self.inventory_page.get_cart_quantity() == '6'
    #
    # def test_remove_btn(self):
    #     for n in range(1, 2):
    #         self.inventory_page.click_on_element(n)
    #     time.sleep(1)
    #     assert self.inventory_page.button_text(n) == "REMOVE"
    #
    # def test_title_text(self):  # NIE DZIAŁA
    #     for n in range(1, 2):
    #         self.inventory_page.click_on_element(n)
    #         time.sleep(1)
    #         self.inventory_page.go_to_cart()
    #         time.sleep(1)
    #         assert self.inventory_page.cart_title_text(n) == "Sauce Labs Backpack"
    #
    # def test_remove_from_cart(self):
    #     for n in range(1, 3):
    #         self.inventory_page.click_on_element(n)
    #         time.sleep(1)
    #     for n in range(1, 2):
    #         self.inventory_page.click_on_element(n)
    #     assert self.inventory_page.get_cart_quantity() == '1'

    @pytest.mark.usefixtures('setup2')
    class TestCart1:

        def test_continue_shopping(self):
            self.cart_page.continue_shopping()
            assert self.driver.find_element_by_css_selector('div#inventory_filter_container > div') is True
