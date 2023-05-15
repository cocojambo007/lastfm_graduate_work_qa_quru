from selene import browser
import allure
from pages.login_page import login_page
from pages.user_page import user_page
from pages.artist_page import artist_page
from pages.search_page import search_page
from pages.playlists_page import playlist_page
from pages.settings_page import settings_page
from pages.footer_page import footer_page

band = 'Electric Wizard'

@allure.step('Открыть главную страницу')
def test_login():
    browser.open('https://www.last.fm/login')
    login_page.input_username_or_email('cocojambo_qa')
    login_page.input_password('1@qwerty')
    login_page.press_button_login()

@allure.step('Открыть главную страницу')
def test_search_band():
    test_login()
    user_page.click_search_toggle()
    user_page.artist_input(band)
    user_page.click_search_submit()
    search_page.click_found_artist(band)  # лучше перенести в search_page

@allure.step('Открыть главную страницу')
def test_like_song():
    test_search_band()
    artist_page.like_song()

@allure.step('Открыть главную страницу')
def test_new_playlist():
    test_login()
    user_page.click_playlist()
    playlist_page.new_playlist_button()
    playlist_page.similar_tracks()
    playlist_page.search_for_tracks(band)
    playlist_page.search_submit_button()
    playlist_page.choice_track_for_playlist()

@allure.step('Открыть главную страницу')
def test_dislike_song():
    test_login()
    user_page.click_loved_track()
    user_page.dislike_song_from_loved_track()

@allure.step('Открыть главную страницу')
def test_upload_picture_profile():
    test_login()
    user_page.click_add_image()
    settings_page.upload_picture()
    settings_page.click_upload_picture_button()
    settings_page.click_delete_picture_button()
    settings_page.click_save_changes()

@allure.step('Открыть главную страницу')
def test_change_display_name():
    test_login()
    footer_page.footer_settings()
    settings_page.change_display_name('Pavel Fomin')
    settings_page.click_save_changes()

@allure.step('Открыть главную страницу')
def test_change_country():
    test_login()
    footer_page.footer_settings()
    settings_page.click_dropdown_country()
    settings_page.pick_country()
    settings_page.click_save_changes()

@allure.step('Открыть главную страницу')
def test_change_website():
    test_login()
    footer_page.footer_settings()
    settings_page.change_website()
    settings_page.click_save_changes()

@allure.step('Открыть главную страницу')
def test_change_about_you():
    test_login()
    footer_page.footer_settings()
    settings_page.change_about_you()
    settings_page.click_save_changes()
