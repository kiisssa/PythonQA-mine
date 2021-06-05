from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.actions = []

    def submit_login(self):
        self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    def submit_categories(self):
        self.driver.find_element(By.CSS_SELECTOR, 'a[href="#collapse1"]').click()

    def submit_products(self):
        self.driver.find_element(By.LINK_TEXT, 'Products').click()

    def submit_password(self):
        self.driver.find_element(By.LINK_TEXT, 'Forgotten Password').click()
