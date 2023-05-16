from selene import browser
import allure

from allure_commons.types import Severity
from pages.login_page import login_page
from pages.user_page import user_page
from pages.artist_page import artist_page
from pages.search_page import search_page
from pages.playlists_page import playlist_page
from pages.settings_page import settings_page
from pages.footer_page import footer_page

band = 'Electric Wizard'
page = 'https://www.last.fm/login'


@allure.tag('ui')
@allure.severity(Severity.NORMAL)
@allure.label('owner', 'fominpa')
@allure.feature(f'Проверка регистрации пользователя')
@allure.link(page, name='login')
def test_login(setup_browser):
    login_page.open_page(page)
    login_page.input_username_or_email('cocojambo_qa')
    login_page.input_password('1@qwerty')
    login_page.click_accept_all()
    login_page.press_button_login()


@allure.tag('ui')
@allure.severity(Severity.NORMAL)
@allure.label('owner', 'fominpa')
@allure.feature('Проверка поиска исполнителя')
def test_search_band(setup_browser):
    login_page.authorization()
    user_page.click_search_toggle()
    user_page.artist_input(band)
    user_page.click_search_submit()
    search_page.click_found_artist(band)


@allure.tag('ui')
@allure.severity(Severity.NORMAL)
@allure.label('owner', 'fominpa')
@allure.feature('Проверка кнопки лайк')
def test_like_song(setup_browser):
    login_page.authorization()
    user_page.click_search_toggle()
    user_page.artist_input(band)
    user_page.click_search_submit()
    search_page.click_found_artist(band)
    artist_page.like_song()


@allure.tag('ui')
@allure.severity(Severity.NORMAL)
@allure.label('owner', 'fominpa')
@allure.feature('Проверка добавления днового плейлиста')
def test_new_playlist(setup_browser):
    login_page.authorization()
    user_page.click_playlist()
    playlist_page.new_playlist_button()
    playlist_page.similar_tracks()
    playlist_page.search_for_tracks(band)
    playlist_page.search_submit_button()
    playlist_page.choice_track_for_playlist()


@allure.tag('ui')
@allure.severity(Severity.NORMAL)
@allure.label('owner', 'fominpa')
@allure.feature('Проверка кнопки дизлайк')
def test_dislike_song(setup_browser):
    login_page.authorization()
    user_page.click_loved_track()
    user_page.dislike_song_from_loved_track()


@allure.tag('ui')
@allure.severity(Severity.NORMAL)
@allure.label('owner', 'fominpa')
@allure.feature('Проверка загрузки аватара')
def test_upload_picture_profile(setup_browser):
    login_page.authorization()
    footer_page.footer_settings()
    # user_page.click_add_image()
    settings_page.upload_picture()
    settings_page.click_upload_picture_button()
    settings_page.click_delete_picture_button()
    settings_page.click_save_changes()


@allure.tag('ui')
@allure.severity(Severity.NORMAL)
@allure.label('owner', 'fominpa')
@allure.feature('Проверка смены имени профиля')
def test_change_display_name(setup_browser):
    login_page.authorization()
    footer_page.footer_settings()
    settings_page.change_display_name('Pavel Fomin')
    settings_page.click_save_changes()


@allure.tag('ui')
@allure.severity(Severity.NORMAL)
@allure.label('owner', 'fominpa')
@allure.feature('Проверка смены страны')
def test_change_country(setup_browser):
    login_page.authorization()
    footer_page.footer_settings()
    settings_page.click_dropdown_country()
    settings_page.pick_country()
    settings_page.click_save_changes()


@allure.tag('ui')
@allure.severity(Severity.NORMAL)
@allure.label('owner', 'fominpa')
@allure.feature('Проверка смены website')
def test_change_website(setup_browser):
    login_page.authorization()
    footer_page.footer_settings()
    settings_page.change_website()
    settings_page.click_save_changes()


@allure.tag('ui')
@allure.severity(Severity.NORMAL)
@allure.label('owner', 'fominpa')
@allure.feature('Проверка смены информации о себе')
def test_change_about_you(setup_browser):
    login_page.authorization()
    footer_page.footer_settings()
    settings_page.change_about_you()
    settings_page.click_save_changes()
