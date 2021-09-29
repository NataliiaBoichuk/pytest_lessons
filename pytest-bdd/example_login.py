import pytest
from pytest_bdd import scenario, given, when, then
from selenium import webdriver


@pytest.fixture
def browser(request):
    br = webdriver.Firefox()

    yield br

    br.quit()


@scenario("store_login.feature", "Valid Login")
def test_valid_login():
    pass


@scenario("store_login.feature", "Valid Login")
def test_invalid_login():
    pass


@given("I visit the login page")
def visit_page(browser):
    browser.get("https://my-store.ca")


@when("I login with valid credentials")
def login_valid(browser):
    browser.find_element_by_id("user-name").send_keys('valid_user')
    browser.find_element_by_id("password").send_keys('good_password')
    browser.find_element_by_class_name("btn_action").click()


@when("I login with invalid credentials")
def login_valid(browser):
    browser.find_element_by_id("user-name").send_keys('nope')
    browser.find_element_by_id("password").send_keys('still_nope')
    browser.find_element_by_class_name("btn_action").click()


@then("I should be on the inventory page")
def on_inventory_page(browser):
    assert 'inventory' in browser.current_url


@then("I should see an error message")
def on_inventory_page(browser):
    assert browser.find_element_by_class_name('error-button').present
