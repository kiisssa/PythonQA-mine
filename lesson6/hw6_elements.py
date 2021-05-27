def test_main_page(browser, base_url):
    browser.implicitly_wait(5)
    browser.get(base_url)
    browser.find_element_by_id('hero')
    browser.find_element_by_class_name('container')
    browser.find_elements_by_tag_name('a')
    browser.find_element_by_css_selector("button[type='button']")
    browser.find_element_by_link_text('Marketplace')

def test_product_page(browser, base_url):
    browser.implicitly_wait(5)
    browser.get(base_url + '/index.php?route=common/home')
    browser.find_element_by_id('copyright')
    browser.find_elements_by_tag_name('h1')
    browser.find_element_by_class_name('input-group-btn')
    browser.find_element_by_css_selector("button[type='button']")
    browser.find_element_by_link_text('Features')

def test_item_page(browser, base_url_demo):
    browser.implicitly_wait(5)
    browser.get(base_url_demo + '/index.php?route=product/product&product_id=43')
    browser.find_element_by_id('product')
    browser.find_element_by_css_selector("button[type='button']")
    browser.find_element_by_tag_name('li')
    browser.find_element_by_link_text('Apple')
    browser.find_element_by_class_name('rating')

def test_admin_page(browser, base_url_demo):
    browser.implicitly_wait(5)
    browser.get(base_url_demo + '/admin')
    browser.find_element_by_tag_name('br')
    browser.find_element_by_class_name('panel-body')
    browser.find_element_by_css_selector('*')
    browser.find_element_by_id('content')

def test_login_page(browser, base_url):
    browser.implicitly_wait(5)
    browser.get(base_url + '/index.php?route=account/login')
    browser.find_element_by_id('account-login')
    browser.find_element_by_class_name('page-header')
    browser.find_element_by_link_text('Create an OpenCart account')
    browser.find_element_by_css_selector("input[type='hidden']")
    browser.find_element_by_tag_name('h3')

