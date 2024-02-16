import json
from playwright.sync_api import Page, expect
from pytest_bdd import scenario, given, when, then

path_to_credentials = "./secrets.json"
with open(path_to_credentials, "r") as handler:
    info = json.load(handler)
password = info["password"]
account = info["account"]

@scenario('gmail_login_logout.feature', 'Successful login and logout')
def test_successful_login_and_logout():
    pass

@given("I am on the Gmail login page")
def navigate_to_gmail_login_page(page: Page):
    page.goto("https://mail.google.com/")
    return page

@when("I enter valid username and password")
def enter_valid_credentials(page: Page):
    page.get_by_label("Email or phone").fill(account)
    page.click("#identifierNext")
    page.get_by_label("Enter your password").fill(password)
    page.click("#passwordNext")

@when("I click on the profile icon")
def click_profile_icon(page: Page):
    page.get_by_role("button", name="Google Account").click()

@when("I click on the Sign out button")
def click_sign_out_button(page: Page):
    page.frame_locator("iframe[name=\"account\"]").get_by_text("Sign out").click()
    
@then("I should be logged in successfully")
def verify_successful_login(page: Page):
    expect(page.get_by_role("button", name="Inbox")).to_be_visible()

@then("I should be logged out successfully")
def verify_successful_logout(page: Page):
    expect(page.get_by_role("button", name="Inbox")).not_to_be_visible()