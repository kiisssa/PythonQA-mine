from .BasePage import BasePage

class ProductPage(BasePage):

    CATEGORIES = {'css': 'a[href="#collapse1"]'}
    PRODUCTS = {'link_text': 'Products'}

    def click_categories(self):
        self.submit_categories()
        return self

    def click_products(self):
        self.submit_products()
        return self
