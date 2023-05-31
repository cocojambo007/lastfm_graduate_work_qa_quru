import random
import allure
from selene import browser, by, be, have

song = random.randint(1, 10)
xpath_choice_track_for_playlist = f'//*[@id="mantle_skin"]/div[2]/div/div[2]/div[2]/div/div/div/table/tbody/tr[{song}]/td[6]/form/button'

class PlaylistPage:
    @allure.step('Нажатие на кнопку новый плейлист')
    def new_playlist_button(self):
        browser.element(by.text('New playlist')).click()
        assert browser.element(by.css('#mantle_skin>div.container.page-content>div:nth-child(2)>form>button')).should(be.visible)
        return self

    @allure.step('Нажатие на кнопку "Similar Tracks"')
    def similar_tracks(self):
        browser.element(by.class_name('playlisting-create-option')).click()
        assert browser.element(by.class_name('content-top-header')).should(have.text('New similar tracks playlist'))
        return self

    @allure.step('Ввод исполнителя')
    def search_for_tracks(self, band):
        browser.element(by.id('track-search')).should(be.blank).type(band)
        assert browser.element(by.id('track-search')).should(have.value(band))
        return self

    @allure.step('Нажатие на кнопку поиск')
    def search_submit_button(self):
        browser.element(by.class_name('search-submit')).click()
        assert browser.element(by.xpath('//*[@id="mantle_skin"]/div[2]/div/div[2]/div[2]/div/div/div/table/tbody/tr[1]')).should(be.visible)
        return self

    @allure.step('Нажатие на кнопку добавления в плейлист')
    def choice_track_for_playlist(self):
        browser.element(by.xpath(xpath_choice_track_for_playlist)).click()
        assert browser.element(by.xpath('//*[@id="mantle_skin"]/div[5]/div/div[1]/div/button')).should(be.visible)
        return self
