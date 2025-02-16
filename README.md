# Тестовое задание

## Установка зависимостей:

`pip install -r requirements.txt`

Тест покрывает основное меню страницы в двух режимах разрешения экрана

1920x1080

900x1080

## Структура проекта:
Папка locators содержит локаторы элементов на страницах

Папка pages содержит локаторы элементов на страницах

Папка tests содержит тесты страниц

## Параметры:

Браузер - Google Chrome

## Запуск тестов с формированием отчета в Allure-report:
`pytest  -v -s  --alluredir allure_results`

## Просмотр отчета:

`allure  serve  .\allure_results\`

## Запуск контейнера с копированием результата в allure-results:
`docker run --rm -v C:\path_to_folder\allure-results:/app/allure-results effective_mobile