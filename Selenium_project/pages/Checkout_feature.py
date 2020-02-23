from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import random
import string

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://www.saucedemo.com/cart.html')

time.sleep(1)


class Checkout:
    # clik to checkout
    driver.find_element_by_css_selector('.btn_action').click()

    time.sleep(2)

    # input name

    def generate_name():
        return letters_generator() + numbers_generator()  # zrobić zmienną nie definicję

    def letters_generator(chars=string.ascii_uppercase):
        return ''.join(random.choice(chars) for y in range(6))  # zrobić zmienną  nie definicję

    def numbers_generator(chars=string.digits):
        return ''.join(random.choice(chars) for x in range(5))  # zrobić zmienną  nie definicję

    driver.find_element_by_css_selector('#first-name').send_keys(generate_name())

    time.sleep(1)
    # input lastname

    driver.find_element_by_css_selector('#last-name').send_keys(generate_name())

    time.sleep(1)
    # input zip
    driver.find_element_by_css_selector('#postal-code').send_keys(numbers_generator())

    time.sleep(1)
    # click continue
    driver.find_element_by_css_selector('.btn_primary').click()

    time.sleep(1)

    # # click cancel
    # cancel()

    #
    # # finish
    # driver.find_element_by_css_selector(".btn_action").click()
    # time.sleep(2)
    # driver.quit()
#
# def cancel():
#     driver.find_element_by_css_selector('.cart_cancel_link').click()


# time.sleep(2)
# driver.quit()
