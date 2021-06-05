from .BasePage import BasePage
from .ProductPage import ProductPage
from .ForgottenPage import ForgottenPage

class MainPage(BasePage):

    LOGIN_ELEMENT = {'css':"button[type='submit']"}
    FORGOTTEN_ELEMENT = {'link_text': 'Forgotten Password'}

    def click_login_element(self):
        self.submit_login()
        return ProductPage(self.driver)

    def click_forgotten_element(self):
        self.submit_password()
        return ForgottenPage(self.driver)
