from page_objects import MainPage, ProductPage, ForgottenPage

def test_admin1(browser):
    MainPage(browser)\
        .click_login_element()\
        .click_categories()\
        .click_products()
    assert browser.find_element_by_class_name('panel-body')

def test_admin2(browser):
    MainPage(browser)\
        .click_forgotten_element()
    assert browser.find_elements_by_class_name('container-fluid')