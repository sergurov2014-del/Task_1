## Задание 1: Юнит-тесты

### Автотесты для проверки программы, которая помогает заказать бургер в Stellar Burgers

### Реализованные сценарии

Созданы юнит-тесты, покрывающие классы `Bun`, `Burger`, `Ingredient`, `Database`

Процент покрытия: 78%, модуль praktikum\praktikum.py по заданию не покрывается автотестами (отчет: `htmlcov/index.html`)

### Структура проекта

- `praktikum` - пакетс исходными файлами, содержащий код программы (`bun.py`, `burger.py`, `ingredient.py`, `ingredient_types.py`, `database.py`)
- `data_for_tests` - пакет, содержащий данные для тестов (`data_bun.py`, `data_burger.py`, `data_ingredient.py`, `data_database.py`) 
- `tests` - пакет, содержащий тесты, разделенные по классам (`bun_test.py`, `burger_test.py`, `ingredient_test.py`, `database_test.py`) 

### Запуск автотестов

**Установка зависимостей**

> `$ pip install -r requirements.txt`

**Запуск автотестов и создание HTML-отчета о покрытии**

>  `$python -m  pytest --cov=praktikum --cov-report=html`

запуск автотестов
python -m pytest -v ./tests/ingredient_test.py