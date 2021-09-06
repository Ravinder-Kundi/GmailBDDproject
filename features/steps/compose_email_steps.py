from behave import *
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import time
from Utilities import XLutils


@then('click on compose link')
def step_impl(context):
    context.driver.find_element_by_xpath("//div[@class='T-I T-I-KE L3']").click()

@then('input data in subject')
def subject_in(context):
    context.driver.find_element_by_xpath("//input[@name='subjectbox']").send_keys(subject)


@then('input message in email')
def step_impl(context):
    context.driver.find_element_by_css_selector("[class='Am Al editable LW-avf tS-tW']").send_keys(message)
    time.sleep(3)
# Getting data from excel file
xl= ".//TestData/Book1.xlsx"
subject =XLutils.readData(xl,"composeSM",2,1)
message =XLutils.readData(xl,"composeSM",2,2)
print(subject)
print(message)