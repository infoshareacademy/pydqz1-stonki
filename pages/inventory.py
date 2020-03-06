from selenium.webdriver.common.by import By


class InventoryPage:

    def __init__(self, driver):

        self.driver = driver
        self.cart_navbar_status = (By.XPATH, '/html/body/div/div[2]/div[1]/div[2]/a/span')
        self.cart_status = (By.XPATH, '/html/body/div/div[2]/div[1]/div[2]/a/span')
        self.continue_shopping_btn = (By.XPATH, '/html/body/div/div[2]/div[3]/div/div[2]/a[1]')
        self.your_cart = (By.XPATH, '/html/body/div/div[2]/div[2]')
        self.products = (By.XPATH, '/html/body/div/div[2]/div[2]/div/div[1]/div[3]/div')

    @classmethod
    def pick_element(cls, element):
        xpath = f"/html/body/div/div[2]/div[2]/div/div[2]/div/div[{element}]/div[3]/button"
        return By.XPATH, xpath

    @classmethod
    def pick_cart_element(cls, element):
        xpath = f"/html/body/div/div[2]/div[3]/div/div[1]/div[{element}]/div[2]/a/div"
        return By.XPATH, xpath

    def click_on_cart_icon(self):
        bucket = self.driver.find_element(*self.cart_status)
        return bucket.click()

    def click_on_element(self, element):
        button = self.driver.find_element(*self.pick_element(element))
        return button.click()

    def get_cart_quantity(self):
        quantity = self.driver.find_element(*self.cart_navbar_status)
        return quantity.text

    def click_on_continue_shopping(self):
        continue_shopping = self.driver.find_element(*self.continue_shopping_btn)
        return continue_shopping.click()

    def get_cart_header(self):
        cart_header = self.driver.find_element(*self.your_cart)
        return cart_header.text

    def get_products_header(self):
        products_text = self.driver.find_element(*self.products)
        return products_text.text

    def get_cart_element_name(self, element):
        element = self.driver.find_element(*self.pick_cart_element(element))
        return element.text

    def button_text(self, element):
        button = self.driver.find_element(*self.pick_element(element))
        return button.text




















