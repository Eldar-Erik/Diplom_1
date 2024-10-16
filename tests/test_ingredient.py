import pytest
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


@pytest.mark.parametrize("type, name, price, expected", [
    (INGREDIENT_TYPE_SAUCE, "hot sauce", 100, 100),
    (INGREDIENT_TYPE_SAUCE, "sour cream", 200, 200),
    (INGREDIENT_TYPE_SAUCE, "chili sauce", 300, 300),
    (INGREDIENT_TYPE_FILLING, "cutlet", 100, 100),
    (INGREDIENT_TYPE_FILLING, "dinosaur", 200, 200),
    (INGREDIENT_TYPE_FILLING, "sausage", 300, 300)
])
def test_get_price_success(type, name, price, expected):
    ingredient = Ingredient(type, name, price)
    assert ingredient.get_price() == expected

@pytest.mark.parametrize("type, name, price, expected", [
    (INGREDIENT_TYPE_SAUCE, "hot sauce", 100, "hot sauce"),
    (INGREDIENT_TYPE_SAUCE, "sour cream", 200, "sour cream"),
    (INGREDIENT_TYPE_SAUCE, "chili sauce", 300, "chili sauce"),
    (INGREDIENT_TYPE_FILLING, "cutlet", 100, "cutlet"),
    (INGREDIENT_TYPE_FILLING, "dinosaur", 200, "dinosaur"),
    (INGREDIENT_TYPE_FILLING, "sausage", 300, "sausage")
])
def test_get_name_success(type, name, price, expected):
    ingredient = Ingredient(type, name, price)
    assert ingredient.get_name() == expected

@pytest.mark.parametrize("type, name, price, expected", [
    (INGREDIENT_TYPE_SAUCE, "hot sauce", 100, INGREDIENT_TYPE_SAUCE),
    (INGREDIENT_TYPE_SAUCE, "sour cream", 200, INGREDIENT_TYPE_SAUCE),
    (INGREDIENT_TYPE_SAUCE, "chili sauce", 300, INGREDIENT_TYPE_SAUCE),
    (INGREDIENT_TYPE_FILLING, "cutlet", 100, INGREDIENT_TYPE_FILLING),
    (INGREDIENT_TYPE_FILLING, "dinosaur", 200, INGREDIENT_TYPE_FILLING),
    (INGREDIENT_TYPE_FILLING, "sausage", 300, INGREDIENT_TYPE_FILLING)
])
def test_get_type_success(type, name, price, expected):
    ingredient = Ingredient(type, name, price)
    assert ingredient.get_type() == expected
