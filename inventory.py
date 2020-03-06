from selenium.webdriver.common.by import By


class InventoryPage:

    def __init__(self, driver):

        self.driver = driver
        self.cart_navbar_status = (By.XPATH, '/html/body/div/div[2]/div[1]/div[2]/a/span')
        self.cart_icon = '#shopping_cart_container > a > span'

        # self.add_to_cart_btns_list = driver.find_elements_by_css_selector('div#inventory_container div > div.pricebar > button')
        # self.inventory_names_list = driver.find_elements_by_css_selector('div.inventory_item_name')
        # self.inventory_price_list = driver.find_elements_by_css_selector('div.inventory_item_price')
        # self.cart_icon_navbar = '#shopping_cart_container > a > span'
        # self.continue_shopping_btn = 'div#cart_contents_container a.btn_secondary'
        # self.checkout_btn_css = 'div#cart_contents_container a.btn_action.checkout_button'

    @classmethod
    def pick_element(cls, element):
        xpath = f"/html/body/div/div[2]/div[2]/div/div[2]/div/div[{element}]/div[3]/button"
        return By.XPATH, xpath

    @classmethod
    def cart_element_title(cls, item):
        xpath = f"/html/body/div[1]/div[2]/div[3]/div/div[1]/div[{item}]/div[2]/a/div"
        return By.XPATH, xpath

    def click_on_element(self, element):
        button = self.driver.find_element(*self.pick_element(element))
        return button.click()

    def get_cart_quantity(self):
        quantity = self.driver.find_element(*self.cart_navbar_status)
        return quantity.text

    def button_text(self, element):
        button = self.driver.find_element(*self.pick_element(element))
        return button.text

    def cart_title_text(self, item):
        title = self.driver.find_element(*self.cart_element_title(item))
        return title.text

    def go_to_cart(self):
        cart_icon_btn = self.driver.find_element_by_css_selector(self.cart_icon)
        return cart_icon_btn.click()



    # def go_to_cart(self, item):
    #     cart_icon_btn = self.driver.find_element(*self.cart_element_title(item))
    #     return cart_icon_btn.click()

    # def inventory_title_text(self, item):
    #     title = self.driver.find_element(*self.inventory_element_title(item))
    #     return title.text

    # @classmethod
    # def inventory_element_title(cls, item):
    #     xpath = f"/html/body/div/div[2]/div[2]/div/div[2]/div/div[{item}]/div[2]/a/div"
    #     return By.XPATH, xpath



















