import os
import time

import allure
from selene import browser, be, by, have


login = os.getenv('LOGIN_LASTFM')
css_dislike_song_from_loved_track = f'#user-loved-tracks-section>table>tbody>tr:nth-child(1)>td.chartlist-loved>div>form>button'


class UserPage:
    @allure.step('Раскрытие поля поиска')
    def click_search_toggle(self):
        browser.element(by.class_name('masthead-search-toggle')).click()
        assert browser.element(by.class_name('masthead-search-inner-wrap')).should(be.visible)
        return self

    @allure.step('Ввод исполнителя')
    def artist_input(self, band):
        browser.element(by.id('masthead-search-field')).should(be.blank).type(band)
        assert browser.element(by.id('masthead-search-field')).should(have.value(band))
        return self

    @allure.step('Нажатие на кнопку поиск')
    def click_search_submit(self, band):
        browser.element(by.class_name('masthead-search-submit')).click()
        assert browser.element(by.id('site-search')).should(have.value(band))
        return self

    @allure.step('Открытие страницы плейлист')
    def click_playlist(self):
        browser.element(by.text('Playlists')).click()
        # time.sleep(10)
        assert browser.element(by.text('New playlist')).should(be.visible)
        return self

    @allure.step('Открытие страницы "Loved track"')
    def click_loved_track(self):
        browser.element(by.text('Loved Tracks')).click()
        time.sleep(10)
        assert f"{login}'s loved tracks | Last.fm" in browser.title()
        return self

    @allure.step('Нажатие на сердечко')
    def dislike_song_from_loved_track(self):
        browser.element(by.css(css_dislike_song_from_loved_track)).click()
        assert browser.element(by.css(css_dislike_song_from_loved_track)).should(have.text('Love this track'))
        return self

    @allure.step('Открытие страницы регистрации')
    def click_add_image(self):
        browser.element(by.text('Add Image')).click()
        return self

# browser.element(by.class_name('masthead-search-toggle')).click()
# browser.element(by.id('masthead-search-field')).should(be.blank).type('Electric Wizard')
# browser.element(by.class_name('masthead-search-submit')).click()
# browser.element(by.text('Electric Wizard')).click()
