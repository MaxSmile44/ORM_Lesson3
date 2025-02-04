# Корректировка электронного дневника школы

Скрипт с функциями для корректировки базы данных электронного дневника школы.

[Электронного дневника школы](https://github.com/devmanorg/e-diary/tree/master) - это сайт - интерфейс для учеников школы. Здесь можно посмотреть оценки, расписание и прочую открытую информацию. Учителя заполняют базу данных через другой сайт. Ставят там оценки и т.д.

## Как установить

Скачать [репозиторий электронного дневника школы](https://github.com/devmanorg/e-diary/tree/master).
Обзавестить собственной базой данных.
Следуя инструкции из репозитория, установить сайт дневника.

## Как запустить

Терминале вводим `python manage.py shell`. Таким образом попадаем в консоль. Копируем все строки из файла `scripts.py` данного репозитория и вставляем их в консоль. Нажимаем дважды клавишу Enter на клавиатуре.
В файле `scripts.py` перечислены функции, которые корректируют базу данных. К каждой функции добавлено ее описание и необходимые ей параметры.
Вводим название функции и атрибуты к ней для корректировки базы данных.
Для выходы из консоли вводим `exit()` и нажимаем клавишу Enter на клавиатуре.
Для просмотра сайта и проверки обновленных данных вводим в терминал `python manage.py runserver`.

## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).
