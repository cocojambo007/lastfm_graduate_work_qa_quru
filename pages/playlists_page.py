from selene import browser, by, be
import random

song = random.randint(1, 10)


class PlaylistPage:

    def new_playlist_button(self):
        browser.element(by.text('New playlist')).click()
        return self

    def similar_tracks(self):
        browser.element(by.class_name('playlisting-create-option')).click()
        return self

    def search_for_tracks(self, band):
        browser.element(by.id('track-search')).should(be.blank).type(band)
        return self

    def search_submit_button(self):
        browser.element(by.class_name('search-submit')).click()
        return self

    def choice_track_for_playlist(self):
        browser.element(by.xpath(
            f'//*[@id="mantle_skin"]/div[2]/div/div[2]/div[2]/div/div/div/table/tbody/tr[{song}]/td[6]/form/button')).click()
        return self


playlist_page = PlaylistPage()
