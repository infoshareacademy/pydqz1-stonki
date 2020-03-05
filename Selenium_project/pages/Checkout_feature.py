from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import random
import string
from generator_function import generate_nick
from generator_function import numbers_generator

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://www.saucedemo.com/inventory.html')
driver.find_element_by_css_selector('div.inventory_item:nth-child(1) > div:nth-child(3) > button:nth-child(2)').click()
time.sleep(1)
driver.find_element_by_css_selector('div.inventory_item:nth-child(3) > div:nth-child(3) > button:nth-child(2)').click()
time.sleep(1)
driver.find_element_by_css_selector('.svg-inline--fa > path:nth-child(1)').click()
time.sleep(1)


class Checkout:
    # clik to checkout
    time.sleep(1)
    driver.find_element_by_css_selector('.btn_action').click()

    time.sleep(1)

    # input name
    driver.find_element_by_css_selector('#first-name').send_keys(generate_nick(6,2))
    time.sleep(1)

    # input lastname
    driver.find_element_by_css_selector('#last-name').send_keys(generate_nick(8,4))
    time.sleep(1)

    # input zip
    driver.find_element_by_css_selector('#postal-code').send_keys(numbers_generator(6))
    time.sleep(1)

    # click continue
    driver.find_element_by_css_selector('.btn_primary').click()
    time.sleep(1)

    # delete first item
    driver.find_element_by_css_selector('#item_4_title_link > div:nth-child(1)').click()
    time.sleep(1)
    driver.find_element_by_css_selector('.btn_secondary').click()
    time.sleep(1)
    driver.find_element_by_css_selector('.inventory_details_back_button').click()
    time.sleep(1)

    # continue shopping
    driver.find_element_by_css_selector('a.btn_secondary').click()
    time.sleep(1)

    # added 2 and 3 items
    driver.find_element_by_css_selector('div.inventory_item:nth-child(5) > div:nth-child(3) > button:nth-child(2)').click()
    time.sleep(1)
    driver.find_element_by_css_selector('div.inventory_item:nth-child(6) > div:nth-child(3) > button:nth-child(2)').click()
    time.sleep(1)

    # go to cart
    driver.find_element_by_css_selector('.svg-inline--fa > path:nth-child(1)').click()
    time.sleep(1)

    # delete one item
    driver.find_element_by_css_selector('div.cart_item:nth-child(3) > div:nth-child(2) > div:nth-child(3) > button:nth-child(2)').click()
    time.sleep(1)

    # click checkout
    driver.find_element_by_css_selector('.btn_action').click()
    time.sleep(1)

    # input name
    driver.find_element_by_css_selector('#first-name').send_keys(generate_nick(6,2))
    time.sleep(1)

    # input lastname
    driver.find_element_by_css_selector('#last-name').send_keys(generate_nick(8,4))
    time.sleep(1)

    # input zip
    driver.find_element_by_css_selector('#postal-code').send_keys(numbers_generator(6))
    time.sleep(1)

    # click continue
    driver.find_element_by_css_selector('.btn_primary').click()
    time.sleep(1)

    # # click cancel
    # cancel()


    # finish
    driver.find_element_by_css_selector(".btn_action").click()
    time.sleep(2)
    driver.quit()
#
# def cancel():
#     driver.find_element_by_css_selector('.cart_cancel_link').click()


# time.sleep(2)
# driver.quit()
