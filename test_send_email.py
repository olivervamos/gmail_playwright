import json
from playwright.sync_api import Page, expect
from pytest_bdd import scenarios, given, when, then

path_to_credentials = "./secrets.json"
with open(path_to_credentials, "r") as handler:
    info = json.load(handler)
password = info["password"]
account = info["account"]

path_to_contact = "./contact.json"
with open(path_to_contact, "r") as handler:
    info = json.load(handler)
contact = info["contact"]

scenarios('gmail_send_email.feature')

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

@when("I click on the Contacts icon")
def click_contacts_icon(page: Page):
    Contacts_visible = page.frame_locator("iframe[title=\"Contacts\"]").get_by_text("Contacts")
    if Contacts_visible:
        pass
    else:
        page.get_by_label("Contacts", exact=True).click()
    page.wait_for_timeout(3000)

@when("I click on the contact")
def click_contact(page: Page):
    page.frame_locator("iframe[title=\"Contacts\"]").get_by_role("button", name=contact).click()
    page.wait_for_timeout(1000)

@when("I click on the Send email icon")
def click_send_email_icon(page: Page):
    page.frame_locator("iframe[title=\"Contacts\"]").get_by_label("Send email").click()

@when("I fill subject")
def fill_subject(page: Page):
    page.get_by_label("Subject").fill("Test")

@when("I attach file")
def attach_file(page: Page):
    with page.expect_file_chooser() as fc_info:
        page.get_by_label("Attach files").click()
    file_chooser = fc_info.value
    file_chooser.set_files("file.txt")
    page.wait_for_timeout(3000)

@when("I click on the Send button")
def click_send_button(page: Page):
    page.get_by_label("Send ‪(Ctrl-Enter)‬").click()

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

@then("Message sent should be visible")
def verify_successful_send(page: Page):
    expect(page.get_by_text("Message sent")).to_be_visible()