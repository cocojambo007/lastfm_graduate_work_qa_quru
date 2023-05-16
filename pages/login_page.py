from selene import browser, be, by


class LoginPage:

    def input_username_or_email(self, username):
        browser.element(by.id('id_username_or_email')).should(be.blank).type(username)
        return self

    def input_password(self, password):
        browser.element(by.id('id_password')).should(be.blank).type(password)
        return self

    def press_button_login(self):
        browser.element(by.text('Let me in!')).click()
        return self

    def click_accept_all(self):
        browser.element(by.css('#onetrust-accept-btn-handler')).click()


    def full_way_login(self):
        browser.open('https://www.last.fm/login')
        LoginPage.click_accept_all(self)
        LoginPage.input_username_or_email(self, 'cocojambo_qa')
        LoginPage.input_password(self, '1@qwerty')
        LoginPage.press_button_login(self)


login_page = LoginPage()
