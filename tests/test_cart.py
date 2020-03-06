import pytest
import time


@pytest.mark.usefixtures('setup1')
class TestCart:

    def test_cart_quantity(self):
        for n in range(1, 7):
            self.inventory_page.click_on_element(n)
        assert self.inventory_page.get_cart_quantity() == '6'

    def test_remove_btn(self):
        self.inventory_page.click_on_element(1)
        assert self.inventory_page.button_text(1) == "REMOVE"

    def test_remove_from_cart(self):
        for n in range(1, 3):
            self.inventory_page.click_on_element(n)
        self.inventory_page.click_on_element(1)
        assert self.inventory_page.get_cart_quantity() == '1'

    def test_continue_shopping(self):
        self.inventory_page.click_on_element(1)
        assert self.inventory_page.get_cart_quantity() == '1'

        self.inventory_page.click_on_cart_icon()
        assert self.inventory_page.get_cart_header() == 'Your Cart'

        self.inventory_page.click_on_continue_shopping()
        assert self.inventory_page.get_products_header() == 'Products'

    def test_produscts_name_cart(self):
        for n in range(1, 7):
            self.inventory_page.click_on_element(n)
        self.inventory_page.click_on_cart_icon()
        assert self.inventory_page.get_cart_element_name(3) == 'Sauce Labs Backpack'

#  nad asercjami opis czego dotyczą, pod testem jaki jest oczekiwany rezultat - komentarze