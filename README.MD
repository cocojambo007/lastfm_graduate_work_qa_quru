# Автотесты для сайтов

* UI - https://www.last.fm/
* API - https://reqres.in/api/

## Покрыт следующий функционал
* UI тесты
    * ✅ Проверка регистрации пользователя
    * ✅ Проверка поиска исполнителя
    * ✅ Проверка кнопки лайк
    * ✅ Проверка добавления нового плейлиста
    * ✅ Проверка дизлайка
    * ✅ Проверка загрузки аватара
    * ✅ Проверка смены имени профиля
    * ✅ Проверка смены страны
    * ✅ Проверка смены website
    * ✅ Проверка смены информации о себе


* API тесты
  * ✅ Регистрация нового пользователя
  * ✅ Получение информации об одном пользователе
  * ✅ Получение информации о нескольких пользователях
  * ✅ Обновление информации о пользователе
  * ✅ Удаление информации о пользователе


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

## <img width="6%" title="Jenkins" src="resources/logo/Jenkins.png"> Запуск тестов из [Jenkins](https://jenkins.autotests.cloud/job/lastfm_graduate_work_qa_quru/)

Для запуска тестов из Jenkins:
1. Нажмите кнопку "Собрать с параметрами"

<p><img src="resources/screenshots/chrome_Th3Y7ERHtN.png" alt="Jenkins"/></p>

2. Выберите параметр ui или api

<p><img src="resources/screenshots/chrome_dTHa0jnbT2.png" alt="Jenkins"/></p>

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

## Отчеты о прохождении тестов доступны в Allure

> При локальном запуске введите в командной строке: 
```bash
allure serve .\allure-results
```

### <img width="6%" title="Allure" src="resources/logo/allure.png"> Allure

#### Примеры отображения тестов

<img src="resources/screenshots/chrome_48S1YicMlI.png" alt="Allure"/>

<img src="resources/screenshots/chrome_3oyurhepqi.png" alt="Allure"/>

<img src="resources/screenshots/chrome_GvuwgLTI2S.png" alt="Allure"/>