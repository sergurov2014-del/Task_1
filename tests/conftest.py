import pytest
from random import choice
from unittest.mock import Mock
from praktikum.bun import Bun
from praktikum.burger import Burger
from praktikum.database import Database
from praktikum.ingredient import Ingredient
from data_for_tests.data_ingridient import INGREDIENT_VALID as INGEDIENT
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE as SAUCE
from data_for_tests.data_bun import BUN_VALID_DATA as bun_data


@pytest.fixture
def some_bun() -> Bun:
    return Bun(
        *choice(bun_data)
    )  # выбираем рандомный вариант булки из BUN_VALID_DATA data_for_tests.data_bun


@pytest.fixture
def burger() -> Burger:
    return Burger()


@pytest.fixture
def database() -> Database:
    return Database()


@pytest.fixture
def some_ingredient() -> Ingredient:
    return Ingredient(choice(INGEDIENT))


@pytest.fixture
def mock_bun() -> Mock:  # функция всегда возвращает объект типа Mock
    bun = Mock(spec=Bun)  # spec=Bun-мок, который строго копирует интерфейс класса Bun
    bun.get_name.return_value = "black bun"
    bun.get_price.return_value = 111.1
    return bun


@pytest.fixture
def make_mock_ingredient():
    def _make(
        ingredient_type: str = SAUCE,
        name: str = "something",
        price: float = 100.0,
    ) -> Mock:
        ingredient = Mock(spec=Ingredient)
        ingredient.get_type.return_value = ingredient_type
        ingredient.get_name.return_value = name
        ingredient.get_price.return_value = price
        return ingredient

    return _make
