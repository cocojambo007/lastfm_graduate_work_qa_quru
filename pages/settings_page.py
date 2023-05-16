import random, os
from selene import browser, be, by

song = random.randint(1, 10)
FILE = 'Screenshot_1.jpg'


class SettingsPage:
    def upload_picture(self):
        browser.element(by.id('id_avatar')).send_keys(os.getcwd() + f'/resources/{FILE}')
        return self

    def click_upload_picture_button(self):
        browser.element(by.text('Upload picture')).click()
        return self

    def click_delete_picture_button(self):
        browser.element(by.text('Delete picture')).click()
        return self

    def change_display_name(self, name):
        # if browser.element(by.id('id_full_name')).should(be.blank):
        browser.element(by.css('#id_full_name')).type(name)
        return self
        # else:
        #     browser.element(by.id('id_full_name')).clear()
        #     browser.element(by.id('id_full_name')).type(name)
        #     return self

    def click_dropdown_country(self):
        browser.element(by.css('#id_country')).click()
        return self

    def pick_country(self):
        browser.element(by.css(f'#id_country > option:nth-child({song})')).click()
        return self

    def change_website(self):
        browser.element(by.css('#id_homepage')).type('https://qa.guru/')
        return self

    def change_about_you(self):
        browser.element(by.css('#id_about_me')).type('This diploma project')
        return self

    def click_save_changes(self):
        browser.element(
            by.css('#update-profile > form > div.form-group.form-group--submit > div > button > span')).click()
        return self

settings_page = SettingsPage()
