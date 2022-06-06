# evrika_test

API запросы

http://127.0.0.1:8000/api/register/ - Добавление нового сотрудника компании
http://127.0.0.1:8000/api/user/<int:pk> - Получение информации о сотруднике
http://127.0.0.1:8000/api/status/user/<int:pk> - Изменение статуса сотрудника(Активный, Неактивный)
http://127.0.0.1:8000/api/leader/user/<int:pk> - Создание/изменение руководителя сотрудника
http://127.0.0.1:8000/api/token/ - Авторизация через jwt

1. Первым делом клонируем проект

  <code>git clone https://github.com/djars500/evrika_test.git</code>

2. Устанавливаем Docker и собираем проект

 2.1 Запустите команду сборку
  <code>docker-compose build</code>
  <br/>
 2.2 Запуск команды проекта
  <code>docker-compose up</code>
    <br/>
 2.3 Создайте пользователя открыв второй терминал
  <code> docker-compose exec web python manage.py createsuperuser </code>
    <br/>


  Пример заполнения полей для пользователя
    <br/>

  email - admin@gmail.com
    <br/>

  username - Дияр
    <br/>

  is_staff(статус руководителя) - True или False
    <br/>

  password - 123


3. Postman
 Ниже предоставлена ссылка с примерами для работы с API
   <br/>
  <code>https://www.postman.com/spacecraft-geologist-5341972/workspace/evrika-test/collection/19235221-4acbd506-1115-4ff3-8711-8c4afbc57a3e?action=share&creator=19235221</code>
  
  Для прикрепления токена авторизации используйте переменную {{access_token}}


Отредактируйте значение переменной на свой токен
<img width="1429" alt="Снимок экрана 2022-06-06 в 11 21 56" src="https://user-images.githubusercontent.com/67388370/172099803-287d16f0-f115-46b3-af28-150686a8ed7f.png">


  
