import allure
from allure_commons.types import Severity
from pages import app

band = 'Electric Wizard'
page_login = 'https://www.last.fm/login'


@allure.tag('ui')
@allure.severity(Severity.NORMAL)
@allure.label('owner', 'fominpa')
@allure.feature(f'Проверка регистрации пользователя')
@allure.link(page_login, name='login')
def test_login(setup_browser):
    app.login_page.open_page(page_login)
    app.login_page.input_username_or_email('cocojambo_qa')
    app.login_page.input_password('1@qwerty')
    app.login_page.click_accept_all()
    app.login_page.press_button_login()


@allure.tag('ui')
@allure.severity(Severity.NORMAL)
@allure.label('owner', 'fominpa')
@allure.feature('Проверка поиска исполнителя')
def test_search_band(setup_browser):
    app.login_page.authorization()
    app.user_page.click_search_toggle()
    app.user_page.artist_input(band)
    app.user_page.click_search_submit()
    app.search_page.click_found_artist(band)


@allure.tag('ui')
@allure.severity(Severity.NORMAL)
@allure.label('owner', 'fominpa')
@allure.feature('Проверка кнопки лайк')
def test_like_song(setup_browser):
    app.login_page.authorization()
    app.user_page.click_search_toggle()
    app.user_page.artist_input(band)
    app.user_page.click_search_submit()
    app.search_page.click_found_artist(band)
    app.artist_page.like_song()


@allure.tag('ui')
@allure.severity(Severity.NORMAL)
@allure.label('owner', 'fominpa')
@allure.feature('Проверка добавления днового плейлиста')
def test_new_playlist(setup_browser):
    app.login_page.authorization()
    app.user_page.click_playlist()
    app.playlist_page.new_playlist_button()
    app.playlist_page.similar_tracks()
    app.playlist_page.search_for_tracks(band)
    app.playlist_page.search_submit_button()
    app.playlist_page.choice_track_for_playlist()


@allure.tag('ui')
@allure.severity(Severity.NORMAL)
@allure.label('owner', 'fominpa')
@allure.feature('Проверка кнопки дизлайк')
def test_dislike_song(setup_browser):
    app.login_page.authorization()
    app.user_page.click_loved_track()
    app.user_page.dislike_song_from_loved_track()


@allure.tag('ui')
@allure.severity(Severity.NORMAL)
@allure.label('owner', 'fominpa')
@allure.feature('Проверка загрузки аватара')
def test_upload_picture_profile(setup_browser):
    app.login_page.authorization()
    app.footer_page.footer_settings()
    app.settings_page.upload_picture()
    app.settings_page.click_upload_picture_button()
    app.settings_page.click_delete_picture_button()
    app.settings_page.click_save_changes()


@allure.tag('ui')
@allure.severity(Severity.NORMAL)
@allure.label('owner', 'fominpa')
@allure.feature('Проверка смены имени профиля')
def test_change_display_name(setup_browser):
    app.login_page.authorization()
    app.footer_page.footer_settings()
    app.settings_page.change_display_name('Pavel Fomin')
    app.settings_page.click_save_changes()


@allure.tag('ui')
@allure.severity(Severity.NORMAL)
@allure.label('owner', 'fominpa')
@allure.feature('Проверка смены страны')
def test_change_country(setup_browser):
    app.login_page.authorization()
    app.footer_page.footer_settings()
    app.settings_page.click_dropdown_country()
    app.settings_page.pick_country()
    app.settings_page.click_save_changes()


@allure.tag('ui')
@allure.severity(Severity.NORMAL)
@allure.label('owner', 'fominpa')
@allure.feature('Проверка смены website')
def test_change_website(setup_browser):
    app.login_page.authorization()
    app.footer_page.footer_settings()
    app.settings_page.change_website()
    app.settings_page.click_save_changes()


@allure.tag('ui')
@allure.severity(Severity.NORMAL)
@allure.label('owner', 'fominpa')
@allure.feature('Проверка смены информации о себе')
def test_change_about_you(setup_browser):
    app.login_page.authorization()
    app.footer_page.footer_settings()
    app.settings_page.change_about_you()
    app.settings_page.click_save_changes()
