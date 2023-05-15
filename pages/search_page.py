from selene import browser, by


class SearchPage:
    def click_found_artist(self, band):
        browser.element(by.text(band)).click()
        return self


search_page = SearchPage()
