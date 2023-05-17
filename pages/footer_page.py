import random
import allure
from selene import browser, by

song = random.randint(1, 10)
FILE = 'Screenshot_1.jpg'


class Footer_page:
    @allure.step('Нажатие в footer "Settings"')
    def footer_settings(self):
        browser.element(by.css(
            '#content > div:nth-child(2) > footer > div.footer-top > div > div > div:nth-child(4) > ul > li:nth-child(2) > a')).click()
        return self



