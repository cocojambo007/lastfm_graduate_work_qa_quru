import allure
from selene import browser, by, be


class SearchPage:
    @allure.step('Нажатие на иконку исполнителя')
    def click_found_artist(self, band):
        browser.element(by.text(band)).click()
        assert browser.element(by.class_name('header-new-title')).should(be.visible)
        return self



