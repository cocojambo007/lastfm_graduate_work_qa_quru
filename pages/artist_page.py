import random
from selene import browser, by

song = random.randint(1, 10)


class ArtistPage:
    def like_song(self):
        browser.element(by.css(
            f'#top-tracks>div.buffer-standard>table>tbody>tr:nth-child({song})>td.chartlist-loved>div>form>button')).click()


artist_page = ArtistPage()