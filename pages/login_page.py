import os
import allure

from selene import browser, be, by, have

page = os.getenv('SITE')
login = os.getenv('LOGIN_LASTFM')
password = os.getenv('PASSWORD_LASTFM')


class LoginPage:
    @allure.step('Открытие страницы регистрации')
    def open_login_page(self):
        browser.open(page + 'login')
        assert 'Login | Last.fm' in browser.title()

    @allure.step('Ввод логина')
    def input_username_or_email(self, username):
        browser.element(by.id('id_username_or_email')).should(be.blank).type(username)
        assert browser.element(by.id('id_username_or_email')).should(have.value(username))
        return self

    @allure.step('Ввод пароля')
    def input_password(self, password):
        browser.element(by.id('id_password')).should(be.blank).type(password)
        assert browser.element(by.id('id_password')).should(have.value(password))
        return self

    @allure.step('Нажатие кнопки "Let me in!"')
    def press_button_login(self):
        browser.element(by.text('Let me in!')).click()
        # time.sleep(5)
        assert f'{login}’s Music Profile | Last.fm' in browser.title()
        return self

    @allure.step('Согласие на обработку куки')
    def click_accept_all(self):
        browser.element(by.css('#onetrust-accept-btn-handler')).click()
        return self

    @allure.step('Авторизация')
    def authorization(self):
        self.open_login_page()
        self.input_username_or_email(login)
        self.input_password(password)
        self.click_accept_all()
        self.press_button_login()

    @allure.step('Открытие главной страницы')
    def open_main_page(self):
        browser.open(page)
        self.click_accept_all()
        assert 'Last.fm | Play music, find songs, and discover artists' in browser.title()
