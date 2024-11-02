import pytest
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


types = [INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_SAUCE,
         INGREDIENT_TYPE_FILLING, INGREDIENT_TYPE_FILLING, INGREDIENT_TYPE_FILLING]
names = ["hot sauce", "sour cream", "chili sauce", "cutlet", "dinosaur", "sausage"]
prices = [100, 200, 300, 100, 200, 300]

class TestIngredients:
    @pytest.mark.parametrize("type, name, price, expected", zip(types, names, prices, prices))
    def test_get_price_success(self, type, name, price, expected):
        ingredient = Ingredient(type, name, price)
        assert ingredient.get_price() == expected

    @pytest.mark.parametrize("type, name, price, expected", zip(types, names, prices, names))
    def test_get_name_success(self, type, name, price, expected):
        ingredient = Ingredient(type, name, price)
        assert ingredient.get_name() == expected

    @pytest.mark.parametrize("type, name, price, expected", zip(types, names, prices, types))
    def test_get_type_success(self, type, name, price, expected):
        ingredient = Ingredient(type, name, price)
        assert ingredient.get_type() == expected
