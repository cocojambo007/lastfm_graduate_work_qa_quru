from selene import browser, be, by
import allure

page_login = 'https://www.last.fm/login'

class LoginPage:

    @allure.step('Открытие страницы регистрации')
    def open_page(self, page):
        browser.open(page)

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

    @allure.step('Авторизация')
    def authorization(self):
        LoginPage.open_page(self, page_login)
        LoginPage.click_accept_all(self)
        LoginPage.input_username_or_email(self, 'cocojambo_qa')
        LoginPage.input_password(self, '1@qwerty')
        LoginPage.press_button_login(self)


login_page = LoginPage()
