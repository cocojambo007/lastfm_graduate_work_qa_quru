import random, os, allure
from selenium.common.exceptions import WebDriverException
from selene import browser, be, by

song = random.randint(1, 10)
FILE = 'Screenshot_1.jpg'


class SettingsPage:
    @allure.step('Загрузка картинки на аватар')
    def upload_picture(self):
        # time.sleep(60)
        try:
            browser.element(by.id('id_avatar')).send_keys(os.getcwd() + f'/resources/{FILE}')
        except WebDriverException as e:
            allure.attach(str(e), name="WebDriverException")
            raise e
        return self

    @allure.step('Нажатие на кнопку "Upload picture"')
    def click_upload_picture_button(self):
        browser.element(by.text('Upload picture')).click()
        return self

    @allure.step('Нажатие на кнопку "Delete picture"')
    def click_delete_picture_button(self):
        browser.element(by.text('Delete picture')).click()
        return self

    @allure.step('Ввод "Display name"')
    def change_display_name(self, name):
        try:
            browser.element(by.xpath('//*[@id="id_full_name"]')).type(name)
            # return self
        except WebDriverException as e:
            allure.attach(str(e), name="WebDriverException")
            raise e
        return self

        # if browser.element(by.id('id_full_name')).should(be.blank):
        # time.sleep(60)
        # else:
        #     browser.element(by.id('id_full_name')).clear()
        #     browser.element(by.id('id_full_name')).type(name)
        #     return self

    @allure.step('Раскрытие dropdown')
    def click_dropdown_country(self):
        # time.sleep(10)
        browser.element(by.xpath('//*[@id="id_country"]')).click()
        return self

    @allure.step('Выбор страны')
    def pick_country(self):
        browser.element(by.css(f'#id_country > option:nth-child({song})')).click()
        return self

    @allure.step('Ввод "Website"')
    def change_website(self):
        # time.sleep(10)
        browser.element(by.xpath('//*[@id="id_homepage"]')).type('https://qa.guru/')
        return self

    @allure.step('Ввод "About you"')
    def change_about_you(self):
        browser.element(by.xpath('//*[@id="id_about_me"]')).type('This diploma project')
        return self

    @allure.step('Нажатие на кнопку "Save_changes"')
    def click_save_changes(self):
        browser.element(
            by.css('#update-profile > form > div.form-group.form-group--submit > div > button > span')).click()
        return self


settings_page = SettingsPage()
