import time

def test_admin1(browser, base_url_demo):
    browser.implicitly_wait(5)
    browser.get(base_url_demo + '/admin')
    login_element = browser.find_element_by_css_selector("button[type='submit']")
    login_element.click()
    assert browser.find_elements_by_id('container')
    time.sleep(5)
    categories = browser.find_element_by_css_selector('a[href="#collapse1"]')
    categories.click()
    browser.implicitly_wait(3)
    products = browser.find_element_by_link_text('Products')
    products.click()
    assert browser.find_element_by_class_name('panel-body')
    time.sleep(5)

def test_admin2(browser, base_url_demo):
    browser.implicitly_wait(5)
    browser.get(base_url_demo + '/admin')
    link = browser.find_element_by_link_text('Forgotten Password')
    link.click()
    assert browser.find_elements_by_class_name('container-fluid')
    time.sleep(5)



