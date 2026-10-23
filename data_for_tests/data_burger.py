from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

# Данные для юнит тестов класса Burger

SAMPLE_BUN = Bun("some bun", 10)

SAMPLE_INGREDIENTS = [
    Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", 100),
    Ingredient(INGREDIENT_TYPE_SAUCE, "chili cream", 300),
    Ingredient(INGREDIENT_TYPE_FILLING, "cutlet", 100),
    Ingredient(INGREDIENT_TYPE_FILLING, "sausage", 300),
]

BURGER_PRICE_DATA = [
    # (bun_price, ingredient_prices, expected_total)
    (100, [], 200),
    (100, [100], 300),
    (100, [100, 200], 500),
    (200, [100, 200, 300], 900),
]



RECEIPT_EMPTY_BLACK_BUN = "(==== black bun ====)\n(==== black bun ====)\n\nPrice: 222.2"
RECEIPT_BLACK_BUN_WITH_SAUCE = (
    "(==== black bun ====)\n= sauce something =\n(==== black bun ====)\n\nPrice: 322.2"
)
RECEIPT_BLACK_BUN_WITH_FILLING = (
    "(==== black bun ====)\n= filling something =\n(==== black bun ====)\n\nPrice: 322.2"
)

RECEIPT_POSITION_BLACK_BUN = "(==== black bun ====)"
RECEIPT_POSITION_SAUCE = "= sauce something ="
RECEIPT_POSITION_FILLING = "= filling something ="
RECEIPT_PRICE = "Price: 722.2"