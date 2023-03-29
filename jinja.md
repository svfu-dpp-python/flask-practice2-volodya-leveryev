# Шаблоны Jinja

## Типы тегов

* `{#  #}` — комментарий
* `{{  }}` — выражение
* `{%  %}` — синтаксическая конструкция

Рассмотрим следующий шаблон:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <title>My Webpage</title>
</head>
<body>
    <h1>My Webpage</h1>
    {# комментарий #}
    <p>{{ message }}</p>
    <p>{{ number1 + number2 }}</p>
    {% if my_list %}
        {% for elem in my_list %}
            <p>{{ elem }}</p>
        {% endfor %}
    {% endif %}
</body>
</html>
```

Если при рендеринге данного шаблона передать функции render_template() переменные:

* `message = "Hello, World!"`
* `number1 = 3`
* `number2 = 2`
* `my_list = [1, 2, 3]`

то получится такая HTML-страница:

```HTML
<!DOCTYPE html>
<html lang="en">
<head>
    <title>My Webpage</title>
</head>
<body>
    <h1>My Webpage</h1>

    <p>Hello, World!</p>
    <p>5</p>

    <p>1</p>
    <p>2</p>
    <p>3</p>

</body>
</html>
```

## Условия

Условия позволяют 

## Циклы



## Встроенные переменные и функции

Встроенные во Flask переменные и функции:

* `config` — переменная для доступа к конфигурации приложения
* `request` — переменная для доступа к параметрам HTTP-запроса
* `session` — переменная для доступа к данным текущей сессии
* `g` — переменная для доступа к глобальным переменным приложения
* `url_for()` — функция для получения ссылок на страницы и статические файлы приложения
* `get_flashed_messages()` — функция для получения flash-сообщений

## Блоки и наследование шаблонов

## Источники

* Документация [Jinja](https://jinja.palletsprojects.com/en/3.1.x/templates/)
* Документация [Flask](https://flask.palletsprojects.com/en/2.2.x/templating/)
