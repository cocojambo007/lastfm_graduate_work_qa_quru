import os
import time
import allure

from selene import browser, be, by

page_login = 'https://www.last.fm/login'
login = os.getenv('LOGIN_LASTFM')
password = os.getenv('PASSWORD_LASTFM')

class LoginPage:
    @allure.step('Открытие страницы регистрации')
    def open_page(self):
        browser.open(page_login)
        time.sleep(15)

    @allure.step('Ввод логина')
    def input_username_or_email(self, username):
        browser.element(by.id('id_username_or_email')).should(be.blank).type(username)
        return self

    @allure.step('Ввод пароля')
    def input_password(self, password):
        browser.element(by.id('id_password')).should(be.blank).type(password)
        return self

    @allure.step('Нажатие кнопки "Let me in!"')
    def press_button_login(self):
        browser.element(by.text('Let me in!')).click()
        return self

    @allure.step('Согласие на обработку куки')
    def click_accept_all(self):
        browser.element(by.css('#onetrust-accept-btn-handler')).click()
        return self

    @allure.step('Авторизация')
    def authorization(self):
        LoginPage.open_page(self)
        LoginPage.click_accept_all(self)
        LoginPage.input_username_or_email(self, login)
        LoginPage.input_password(self, password)
        LoginPage.press_button_login(self)



