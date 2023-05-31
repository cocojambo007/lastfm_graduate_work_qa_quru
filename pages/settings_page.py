import random, os, allure
from selene import browser, by, have, be

random = random.randint(1, 100)
FILE = 'Screenshot_1.jpg'


class SettingsPage:
    @allure.step('Загрузка картинки на аватар')
    def upload_picture(self):
        browser.element(by.id('id_avatar')).send_keys(os.getcwd() + f'/resources/{FILE}')
        return self

    @allure.step('Нажатие на кнопку "Upload picture"')
    def click_upload_picture_button(self):
        browser.element(by.xpath('//*[@id="update-picture"]/div/div[2]/form/div[2]/div/button')).click()
        assert browser.element(by.xpath('//*[@id="update-picture"]/div/div[2]/form/div[1]')).should(
            have.text('Your avatar was uploaded successfully.'))
        return self

    @allure.step('Нажатие на кнопку "Delete picture"')
    def click_delete_picture_button(self):
        browser.element(by.text('Delete picture')).click()
        assert browser.element(by.css('#update-picture>div>div.col-xs-4.col-sm-2>span>img')).should(
            have.attribute('src',
                           'https://lastfm.freetls.fastly.net/i/u/avatar170s/818148bf682d429dc215c1705eb27b98.png'))
        return self

    @allure.step('Ввод "Display name"')
    def change_display_name(self, name):
        browser.element(by.xpath('//*[@id="id_full_name"]')).clear().type(name)
        assert browser.element(by.xpath('//*[@id="id_full_name"]')).should(have.value(name))
        return self

    @allure.step('Раскрытие dropdown')
    def click_dropdown_country(self):
        browser.element(by.xpath('//*[@id="id_country"]')).click()
        return self

    @allure.step('Выбор страны')
    def pick_country(self):
        browser.element(by.css(f'#id_country > option:nth-child({random})')).click()
        self.click_save_changes()
        assert browser.element(by.xpath(f'//*[@id="id_country"]/option[{random}][@selected]')).should(be.visible)
        return self

    @allure.step('Ввод "Website"')
    def change_website(self):
        browser.element(by.xpath('//*[@id="id_homepage"]')).clear().type('https://qa.guru/')
        assert browser.element(by.xpath('//*[@id="id_homepage"]')).should(have.value('https://qa.guru/'))
        return self

    @allure.step('Ввод "About you"')
    def change_about_you(self):
        browser.element(by.xpath('//*[@id="id_about_me"]')).clear().type('This diploma project')
        assert browser.element(by.xpath('//*[@id="id_about_me"]')).should(have.value('This diploma project'))
        return self

    @allure.step('Нажатие на кнопку "Save_changes"')
    def click_save_changes(self):
        browser.element(
            by.css('#update-profile > form > div.form-group.form-group--submit > div > button > span')).click()
        assert browser.element(by.xpath('//*[@id="update-profile"]/form/div[1]')).should(
            have.text('You have successfully updated your profile.'))
        return self
