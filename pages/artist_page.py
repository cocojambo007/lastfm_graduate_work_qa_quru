import time

import allure
import random
from selene import browser, by, have

song = random.randint(1, 10)
css_like_song = f'#top-tracks>div.buffer-standard>table>tbody>tr:nth-child({song})>td.chartlist-loved>div>form>button'


class ArtistPage:
    @allure.step('Нажатие на сердечко')
    def like_song(self):
        browser.element(by.css(css_like_song)).click()
        assert browser.element(by.css(css_like_song)).should(have.text('Unlove this track'))

    def unlike_song(self):
        time.sleep(3)
        browser.element(by.css(css_like_song)).click()
        assert browser.element(by.css(css_like_song)).should(have.text('Love this track'))

    # browser.element(by.css(css_like_song)).click()
    # assert browser.element(by.css(css_like_song)).should(have.text('Love this track'))
