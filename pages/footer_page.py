import random
import allure
from selene import browser, by, be

song = random.randint(1, 10)


class Footer_page:
    @allure.step('Нажатие в footer "Settings"')
    def footer_settings(self):
        browser.element(by.css(
            '#content > div:nth-child(2) > footer > div.footer-top > div > div > div:nth-child(4) > ul > li:nth-child(2) > a')).click()
        assert browser.element(by.xpath('//*[@id="update-picture"]/div/div[2]/form/div[2]/div/button')).should(be.visible)
        return self



