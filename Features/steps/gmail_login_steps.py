from selenium import webdriver
from behave import *
from selenium import webdriver
import time
import allure
from allure_commons.types import AttachmentType

from Utilities import XLutils

@given('launch browser')
def open_browser(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.implicitly_wait(30)

@when('gmail homepage is open')
def gmail_homepage(context):
    context.driver.get("https://mail.google.com/mail")


@then(u'confirm Gmail title')
def gmail_logo(context):
    status = context.driver.title == "Gmail"
    assert status is True



@when('user email as email')
def step_impl(context):
    context.driver.find_element_by_xpath("//input[@type='email']").send_keys(email1)
    #email1 reading data from excel sheet


@when('user password as password')
def step_impl(context):
    context.driver.find_element_by_xpath("//input[@name='password']").send_keys(password1)
    # password1 reading data from excel sheet


@when('user email as "{email}"')
def email_input(context,email):
    context.driver.find_element_by_xpath("//input[@type='email']").send_keys(email)
    context.driver.implicitly_wait(10)
    print(email)


@when('click next button')
def click_next(context):
    context.driver.find_element_by_xpath("//span[@class ='VfPpkd-vQzf8d']").click()
    print("click")
    context.driver.implicitly_wait(10)

@when('user password as "{password}"')
def passwd_input(context,password):
    context.driver.find_element_by_xpath("//input[@name='password']").send_keys(password)
    context.driver.implicitly_wait(10)
    print(password)


@When('next button to login')
def next_button(context):
    context.driver.find_element_by_xpath("//div[@id='passwordNext'][1]").click()
    print("click")
    time.sleep(3)

@then('user must login')
def login_in(context):
    context.driver.implicitly_wait(20)
    try:
        text = context.driver.find_element_by_xpath("//title").text
        print(text)
        allure.attach(context.driver.get_screenshot_as_png(), name="Gmail Login",
                      attachment_type=AttachmentType.PNG)
        context.driver.save_screenshot(".\\Screenshots\\" + "gmail_login.png")

    except:
        context.driver.close()
        assert False, "Test Failed "
    if text == "Inbox (1) - aaaaabbb002@gmail.com - Gmail":
        assert True, "Test passed "



#getting data from excel file
xl= ".//TestData/Book1.xlsx"
# reading data from sheet
email1 = XLutils.readData(xl,"Login",2,1)
print(email1)
password1 = XLutils.readData(xl,"Login",2,2)
print(password1)