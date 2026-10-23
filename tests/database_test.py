import pytest
import data_for_tests.data_database as data
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_FILLING,INGREDIENT_TYPE_SAUCE
class TestDbAvailableBuns:

    @pytest.mark.unit
    def test_available_buns_returns_list(self, database):
        result = database.available_buns()
        assert isinstance(result, list)

    @pytest.mark.unit
    def test_available_buns_returns_buns_count(self, database):
        result = database.available_buns()
        assert len(result) == data.BUNS_COUNT

    @pytest.mark.unit
    def test_available_buns_returns_bun_instances(self,database):
        for bun in database.available_buns():
            assert isinstance(bun, Bun)    

    @pytest.mark.unit
    def test_available_buns_returns_same_object_as_attribute(self, database):
        result = database.available_buns()

        assert result is database.buns


class TestDbAvailableIngredients:

    @pytest.mark.unit
    def test_available_ingredients_returns_list(self, database):
        result = database.available_ingredients()     
        assert isinstance(result, list)

    @pytest.mark.unit
    def test_available_ingredientsreturns_six_ingredients(self, database):
        result = database.available_ingredients()
        assert len(result) == data.INGREDIENTS_COUNT

    @pytest.mark.unit
    def test_available_ingredientsreturns_returns_same_object_as_attribute(self, database):
        result = database.available_ingredients()
        assert result is database.ingredients

    @pytest.mark.unit
    def test_available_ingredients_returns_ingredient_instances(self, database):
        result = database.available_ingredients()        
        for ingredient in result:
            assert isinstance(ingredient, Ingredient)


    @pytest.mark.unit
    def test_three_sauces_and_three_fillings(self, database):
        types = [ing.get_type() for ing in database.available_ingredients()]
        assert types.count(INGREDIENT_TYPE_SAUCE) == data.SAUCES_COUNT
        assert types.count(INGREDIENT_TYPE_FILLING) == data.FILLINGS_COUNT
