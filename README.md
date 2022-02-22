Команда для запуска хранилища:

    docker-compose up

Демонстрация работы хранилища:

1. Добавление записей
    
    1. Передан допустимый json

       ![](.\images\post_valid.png)
    2. Запись с таким ключом уже существует

       ![](.\images\post_conflict.png)
    3. Передан не json или json с ошибкой

       ![](.\images\post_bad_request.png)
2. Обновление записей

    1. Передан допустимый json

        ![](.\images\put_valid.png)
    2. Передан не json или json с ошибкой

       ![](.\images\put_bad_request.png)
    3. Записи с данным ключом не существует

       ![](.\images\put_not_found.png)
3. Получение записи
    1. Запись с указанным ключом существует

        ![](.\images\get_ok.png)
    2. Записи с указанным ключом не существует

       ![](.\images\get_not_found.png)
4. Удаление записи
    1. Запись с указанным ключом существует

       ![](.\images\delete_ok.png)
    2. Записи с указанным ключом не существует

       ![](https://github.com/general0303/vk_tarantool/blob/master/images/delete_not_found.png)
    3. Логирование

        ![](pwd\images\logging.png)

К сожалению, в облачное хранилище выложить не получилось,
так единственное облачное хранилище, с которым я работал
(Heroku), не поддерживает много контейнерные приложения