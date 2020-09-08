import self as self
from selenium import webdriver


class LoginPage:

    #Landing Page
    textbox_email_name="email"
    textbox_password_name="password"
    link_forgotpwd_xpath="//*[@id='mat-hint-1']/a"
    button_signin_xpath="//span[@class='mat-button-wrapper']"
    link_register_id = "reg"

    def __init__(self, driver):
        self.driver=driver

    # Landing Page
    def setEmail(self, email):
        self.driver.find_element_by_name(self.textbox_email_name).clear()
        self.driver.find_element_by_name(self.textbox_email_name).send_keys(email)

    def setPassword(self, password):
        self.driver.find_element_by_name(self.textbox_password_name).clear()
        self.driver.find_element_by_name(self.textbox_password_name).send_keys(password)

    def clickForgotPwd(self):
        self.driver.find_element_by_xpath(self.link_forgotpwd_xpath).click()

    def clickSignIn(self):
        self.driver.find_element_by_xpath(self.button_signin_xpath).click()

    def clickRegister(self):
        self.driver.find_element_by_id(self.link_register_id).click()
