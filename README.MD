# Автотесты для сайта

* https://www.last.fm/

## Покрыт следующий функционал
* UI тесты
    * ✅ Проверка входа пользователя
    * ✅ Проверка поиска исполнителя
    * ✅ Проверка кнопки лайк и дизлайк
    * ✅ Проверка добавления нового плейлиста
    * ✅ Проверка загрузки аватара
    * ✅ Проверка страницы settings
      * ✅ Проверка смены имени профиля
      * ✅ Проверка смены страны
      * ✅ Проверка смены website
      * ✅ Проверка смены информации о себе



## Технологический стек
<p  align="center">
  <code><img width="5%" title="Pycharm" src="resources/logo/pycharm.png"></code>
  <code><img width="5%" title="Python" src="resources/logo/python.png"></code>
  <code><img width="5%" title="Pytest" src="resources/logo/pytest.png"></code>
  <code><img width="5%" title="Selene" src="resources/logo/selene.png"></code>
  <code><img width="5%" title="Selenium" src="resources/logo/selenium.png"></code>
  <code><img width="5%" title="GitHub" src="resources/logo/Github.png"></code>
  <code><img width="5%" title="Jenkins" src="resources/logo/Jenkins.png"></code>
  <code><img width="5%" title="selenoid" src="resources/logo/selenoid.png"></code>
  <code><img width="5%" title="Allure Report" src="resources/logo/allure.png"></code>
<!--   <code><img width="5%" title="Jira" src="resources/logo/jira.png"></code> -->
  <code><img width="5%" title="Telegram" src="resources/logo/tg.png"></code>
</p>

## <img width="6%" title="Jenkins" src="resources/logo/Jenkins.png"> Запуск тестов из [Jenkins](https://jenkins.autotests.cloud/job/lastfm_graduate_work_qa_quru_ui/)

Для запуска тестов из Jenkins:
1. Нажмите кнопку "Собрать сейчас"

<p><img src="resources/screenshots/chrome_CGQDVLALYz.png" alt="Jenkins"/></p>


## Запуск тестов
### Локально
```
pytest .
```

### Удаленно
```bash
rm -rf allure-results/*
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest . --alluredir=allure-results
```

### <img width="6%" title="Allure" src="resources/logo/allure.png"> [Allure](https://jenkins.autotests.cloud/job/lastfm_graduate_work_qa_quru_ui/100/allure/)

#### Примеры отображения тестов

<img src="resources/screenshots/chrome_TLhUJ6pyoC.png" alt="Allure"/>

<img src="resources/screenshots/chrome_8exlyfTogV.png" alt="Allure"/>

### <img width="6%" title="Telegram" src="resources/logo/tg.png"> Telegram

#### Настроена отправка отчета в Telegram

<img src="resources/screenshots/Telegram_W88WWBlIPN.png" alt="Telegram"/>

## Пример видео тестового прогона

В отчетах Allure для каждого UI-теста прикреплен не только скриншот, но и видео прохождения теста

<p align="center">
  <img title="Video" src="resources/video/2a77907a7d05d490ef38790234474482.gif"/>
</p>