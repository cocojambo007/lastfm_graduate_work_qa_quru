import random
from selene import browser, by
import allure

song = random.randint(1, 10)


class ArtistPage:
    @allure.step('Нажатие на сердечко')
    def like_song(self):
        browser.element(by.css(
            f'#top-tracks>div.buffer-standard>table>tbody>tr:nth-child({song})>td.chartlist-loved>div>form>button')).click()


artist_page = ArtistPage()
