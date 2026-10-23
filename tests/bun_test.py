import pytest
from praktikum.bun import Bun
import data_for_tests.data_bun as data


class TestBunValid:  # тесты булочек с валидными данными

    @pytest.mark.unit
    @pytest.mark.parametrize("name, price", data.BUN_VALID_DATA)
    def test_bun_valid_data_create_and_stores_correctly(self, name, price):
        bun = Bun(name, price)
        assert bun.name == name
        assert bun.price == price

    @pytest.mark.unit
    @pytest.mark.parametrize("name, price", data.BUN_VALID_DATA)
    def test_get_name_returns_correct_name_str(self, name, price):
        bun = Bun(name, price)
        result = bun.get_name()
        assert result == name
        assert isinstance(result, str)  # проверяем тип

    @pytest.mark.unit
    @pytest.mark.parametrize("name, price", data.BUN_VALID_DATA)
    def test_get_price_returns_correct_number(self, name, price):
        bun = Bun(name, price)
        result = bun.get_price()
        assert result == price
        assert isinstance(result, (int, float))


class TestBunBoundary:  # тесты граничных значений

    @pytest.mark.unit
    @pytest.mark.parametrize("name", data.BUN_BOUNDARY_NAMES)
    def test_get_name_boundary_value_stores_correctly(self, name):
        bun = Bun(name, 1.0)
        assert bun.get_name() == name

    @pytest.mark.unit
    @pytest.mark.parametrize("price", data.BUN_BOUNDARY_PRICES)
    def test_get_price_boundary_value_stores_correctly(self, price):
        bun = Bun("test", price)

        assert bun.get_price() == price
