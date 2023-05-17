import allure
from selene import browser, by


class SearchPage:
    @allure.step('Нажатие на иконку исполнителя')
    def click_found_artist(self, artist):
        browser.element(by.text(artist)).click()
        return self



