import random
import allure
from selene import browser, be, by

song = random.randint(1, 10)
FILE = 'Screenshot_1.jpg'


class UserPage:
    @allure.step('Раскрытие поля поиска')
    def click_search_toggle(self):
        browser.element(by.class_name('masthead-search-toggle')).click()
        return self

    @allure.step('Ввод исполнителя')
    def artist_input(self, artist):
        browser.element(by.id('masthead-search-field')).should(be.blank).type(artist)
        return self

    @allure.step('Нажатие на кнопку поиск')
    def click_search_submit(self):
        browser.element(by.class_name('masthead-search-submit')).click()
        return self

    @allure.step('Открытие страницы плейлист')
    def click_playlist(self):
        browser.element(by.text('Playlists')).click()
        return self

    @allure.step('Открытие страницы "Loved track"')
    def click_loved_track(self):
        browser.element(by.text('Loved Tracks')).click()
        return self

    @allure.step('Нажатие на сердечко')
    def dislike_song_from_loved_track(self):
        browser.element(by.css(
            f'#user-loved-tracks-section > table > tbody > tr:nth-child(1) > td.chartlist-loved > div > form > button')).click()
        return self

    @allure.step('Открытие страницы регистрации')
    def click_add_image(self):
        browser.element(by.text('Add Image')).click()
        return self




# browser.element(by.class_name('masthead-search-toggle')).click()
# browser.element(by.id('masthead-search-field')).should(be.blank).type('Electric Wizard')
# browser.element(by.class_name('masthead-search-submit')).click()
# browser.element(by.text('Electric Wizard')).click()
