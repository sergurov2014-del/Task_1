import pytest
import data_for_tests.data_burger as data

class TestBurgerSetBuns:  # тесты установки булочек

    @pytest.mark.unit  # тэг юнит тестов
    def test_set_buns_stores_bun(self, burger, some_bun):
        bun = some_bun
        burger.set_buns(bun)
        assert burger.bun == bun

    @pytest.mark.unit  # тэг юнит тестов
    def test_set_bun_and_overwrites_new_bun(self, burger, some_bun):
        first_bun, second_bun = ("test_bun", 1111), some_bun
        burger.set_buns(first_bun)
        burger.set_buns(second_bun)
        assert burger.bun is second_bun


class TestAddIngredient:  # тесты добавленния ингридиента

    @pytest.mark.unit  # тэг юнит тестов
    def test_add_ingredient_appends(self, burger, make_mock_ingredient):
        ingredient = make_mock_ingredient()
        burger.add_ingredient(ingredient)
        assert burger.ingredients == [ingredient]

    @pytest.mark.unit  # тэг юнит тестов
    def test_add_3_ingredients_(self, burger, make_mock_ingredient):
        ingr0, ingr1, ingr2 = (
            make_mock_ingredient(),
            make_mock_ingredient(),
            make_mock_ingredient(),
        )
        burger.add_ingredient(ingr0)
        burger.add_ingredient(ingr1)
        burger.add_ingredient(ingr2)

        assert burger.ingredients == [ingr0, ingr1, ingr2]


class TestRemoveIngredient:  # тесты удаления ингридиента

    @pytest.mark.unit  # тэг юнит тестов
    def test_remove_ingredient_removes_it(self, burger, make_mock_ingredient):
        burger.add_ingredient(make_mock_ingredient())
        burger.remove_ingredient(0)
        assert burger.ingredients == []

    @pytest.mark.unit  # тэг юнит тестов
    def test_remove_ingredient_keeps_others_in_order(
        self, burger, make_mock_ingredient
    ):
        ingr0, ingr1, ingr2 = (
            make_mock_ingredient(),
            make_mock_ingredient(),
            make_mock_ingredient(),
        )
        burger.add_ingredient(ingr0)
        burger.add_ingredient(ingr1)
        burger.add_ingredient(ingr2)
        burger.remove_ingredient(1)

        assert burger.ingredients == [ingr0, ingr2]


class TestMoveIngredient:  # тесты перемещения ингридиента

    @pytest.mark.unit  # тэг юнит тестов
    def test_move_ingredient_to_current_index_does_not_change_order(
        self, burger, make_mock_ingredient
    ):
        ingr0, ingr1 = make_mock_ingredient(), make_mock_ingredient()
        burger.add_ingredient(ingr0)
        burger.add_ingredient(ingr1)
        burger.move_ingredient(0, 0)

        assert burger.ingredients == [ingr0, ingr1]

    @pytest.mark.unit  # тэг юнит тестов
    def test_move_ingredient_backward(self, burger, make_mock_ingredient):
        ingr0, ingr1, ingr2 = (
            make_mock_ingredient,
            make_mock_ingredient,
            make_mock_ingredient,
        )
        burger.add_ingredient(ingr0)
        burger.add_ingredient(ingr1)
        burger.add_ingredient(ingr2)
        burger.move_ingredient(2, 0)

        assert burger.ingredients == [ingr1, ingr2, ingr0]

    @pytest.mark.unit  # тэг юнит тестов
    def test_move_ingredient_forward(self, burger, make_mock_ingredient):
        ingr0, ingr1, ingr2 = (
            make_mock_ingredient,
            make_mock_ingredient,
            make_mock_ingredient,
        )
        burger.add_ingredient(ingr0)
        burger.add_ingredient(ingr1)
        burger.add_ingredient(ingr2)
        burger.move_ingredient(0, 2)  # (*,n) вырезаем элемент n и вставляем в позицию *
        assert burger.ingredients == [ingr2, ingr0, ingr1]


class TestGetPrice:

    @pytest.mark.unit
    def test_get_price_bun_counts_twice(self, burger, mock_bun):
        burger.set_buns(mock_bun)
        assert burger.get_price() == 222.2

    @pytest.mark.unit
    def test_get_price_with_one_ingredient(
        self, burger, mock_bun, make_mock_ingredient
    ):
        burger.set_buns(mock_bun)
        ingredient = make_mock_ingredient()
        burger.add_ingredient(ingredient)
        assert burger.get_price() == 322.2

    @pytest.mark.unit
    def test_get_price_with_multiple_ingredients(
        self, burger, mock_bun, make_mock_ingredient
    ):
        ingr1 = make_mock_ingredient(price=10.0)
        ingr2 = make_mock_ingredient(price=20.0)
        ingr3 = make_mock_ingredient(price=30.0)
        burger.set_buns(mock_bun)
        burger.add_ingredient(ingr1)
        burger.add_ingredient(ingr2)
        burger.add_ingredient(ingr3)

        assert burger.get_price() == 282.2


class TestGetReceipt:

    @pytest.mark.unit
    def test_get_receipt_only_black_bun(self, burger, mock_bun):
        burger.set_buns(mock_bun)
        assert data.RECEIPT_EMPTY_BLACK_BUN == burger.get_receipt()

    @pytest.mark.unit
    @pytest.mark.parametrize(
        "ingredient_t, expected_receipt",
        [
            ("SAUCE", data.RECEIPT_BLACK_BUN_WITH_SAUCE),
            ("FILLING", data.RECEIPT_BLACK_BUN_WITH_FILLING),
        ],
    )
    def test_get_receipt_black_bun_with_one_ingredient(
        self, burger, mock_bun, make_mock_ingredient, ingredient_t, expected_receipt
    ):
        burger.set_buns(mock_bun)
        ingredient = make_mock_ingredient(ingredient_type=ingredient_t)
        burger.add_ingredient(ingredient)
        receipt = burger.get_receipt()
        assert receipt == expected_receipt

    def test_get_receipt_multiple_ingredients_in_order(
        self, burger, mock_bun, make_mock_ingredient
    ):
        burger.set_buns(mock_bun)
        burger.add_ingredient(make_mock_ingredient(ingredient_type="SAUCE", price=200.0))
        burger.add_ingredient(make_mock_ingredient(ingredient_type="FILLING", price=300))
        ingredients_position = burger.get_receipt().split("\n")
        assert ingredients_position[0] ==ingredients_position[3] == data.RECEIPT_POSITION_BLACK_BUN
        assert ingredients_position[1] == data.RECEIPT_POSITION_SAUCE
        assert ingredients_position[2] == data.RECEIPT_POSITION_FILLING
        assert ingredients_position[5] == data.RECEIPT_PRICE