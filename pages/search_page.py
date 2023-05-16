from selene import browser, by
import allure

class SearchPage:
    @allure.step('Нажатие на иконку исполнителя')
    def click_found_artist(self, artist):
        browser.element(by.text(artist)).click()
        return self


search_page = SearchPage()
