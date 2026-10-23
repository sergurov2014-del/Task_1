import pytest
from praktikum.ingredient import Ingredient
import data_for_tests.data_ingridient as data


class TestIngredientValid:  # тесты с валидными данными

    @pytest.mark.unit  # тэг юнит тестов
    @pytest.mark.parametrize(
        "ingredient_type, name, price,",
        data.INGREDIENT_VALID,
    )  # проверяем геттер возвращающий имя
    def test_get_name_returns_name_str(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_name() == name
        assert isinstance(ingredient.get_name(), str)

    @pytest.mark.unit
    @pytest.mark.parametrize(
        "ingredient_type, name, price",
        data.INGREDIENT_VALID,
    )  # проверяем геттер возвращающий цену в виде натурального или числа с плавающей точкой
    def test_get_price_returns_price(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_price() == price
        assert isinstance(ingredient.get_price(), (int, float))

    @pytest.mark.unit
    @pytest.mark.parametrize(
        "ingredient_type, name, price",
        data.INGREDIENT_VALID,
    )  # проверяем геттер возвращающий тип ингридиента в строчном виде
    def test_get_type_returns_type_str(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_type() == ingredient_type
        assert isinstance(ingredient.get_type(), str)


class TestIngedientBoundarys:  # тесты граничных значений

    @pytest.mark.unit
    @pytest.mark.parametrize("ingredient_type", data.INGREDIENT_BOUNDARY_TYPES)
    def test_get_type_boundary_value_stores_correctly(
        self, ingredient_type
    ):  # граничное значение корректно сохраняется
        ingredient = Ingredient(ingredient_type, "test", 1)

        assert ingredient.get_type() == ingredient_type

    @pytest.mark.unit
    @pytest.mark.parametrize(
        "name", data.INGREDIENT_BOUNDARY_NAMES
    )  # граничное имя сохраняется без изменений
    def test_get_name_boundary_value_stores_correctly(self, name):
        ingredient = Ingredient("sauce", name, 1)
        assert ingredient.get_name() == name

        @pytest.mark.unit
        @pytest.mark.parametrize("price", data.INGREDIENT_BOUNDARY_PRICES)
        def test_get_price_boundary_value_stores_correctly(self, price):
            ingredient = Ingredient("sauce", "test", price)

            assert ingredient.get_price() == price
