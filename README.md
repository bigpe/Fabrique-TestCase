# Pools Test Case

Файлы с настройками находятся в .env
```shell
WEB_INTERFACE_PORT - порт на котором будет запущен сервис
```

Запуск через композ
```shell
docker-compose up
```

Тестовый стенд на Heroku (Swagger)
```
https://fabrique-test-case.herokuapp.com/api/v1/
```

Админка на Heroku (Grapelli)

Логин - test | Пароль - test
```
https://fabrique-test-case.herokuapp.com/api/admin/
```

Вся документация методов API находится в doc string нужных методов

Опросы можно создать только через панель администратора, API такой функционал не предусматривает
