import pytest
from pytest_bdd import scenario, given, when, then
from selenium import webdriver


@pytest.fixture
def browser(request):
    br = webdriver.Chrome()

    yield br

    br.quit()


@scenario("step_login.feature", "Valid Login")
def test_valid_login(browser):
    assert browser.find_element_by_id('my-account')


@scenario("step_login.feature", "Invalid Login")
def test_invalid_login(browser):
    assert browser.find_element_by_css_selector('div[id=center_column] > div.alert').is_displayed()


@given("I visit the main page")
def visit_page(browser):
    browser.get("http://prestashop.qatestlab.com.ua/uk/")


@when("I login with valid credentials")
def login_valid(browser):
    browser.find_element_by_css_selector("a.login").click()
    browser.find_element_by_id("email").send_keys('testmail11223@gmail.com')
    browser.find_element_by_id("passwd").send_keys('123456')
    browser.find_element_by_id("SubmitLogin").click()


@when("I login with invalid credentials")
def login_invalid(browser):
    browser.find_element_by_css_selector("a.login").click()
    browser.find_element_by_id("email").send_keys('testmail11223@gmail.com')
    browser.find_element_by_id("passwd").send_keys('good_password')
    browser.find_element_by_id("SubmitLogin").click()


@then("I should be on the account page")
def on_account_page(browser):
    assert 'my-account' in browser.current_url


@then("I should see an error message")
def error_msg(browser):
    assert browser.find_element_by_css_selector('div[id=center_column] > div.alert').is_displayed()
