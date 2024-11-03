from praktikum.burger import Burger
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE
from unittest.mock import Mock


def test_set_bun_success():
    burger = Burger()
    bun = Bun("black bun", 100)
    burger.set_buns(bun)
    assert (burger.bun.get_name(), burger.bun.get_price()) == ("black bun", 100)


def test_add_ingredient_success():
    burger = Burger()
    ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", 100)
    burger.add_ingredient(ingredient)
    assert burger.ingredients == [ingredient]


def test_remove_ingredient_success():
    burger = Burger()
    ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", 100)
    burger.add_ingredient(ingredient)
    burger.remove_ingredient(0)
    assert len(burger.ingredients) == 0


def test_move_ingredient_success():
    burger = Burger()
    bun = Bun("black bun", 100)
    burger.set_buns(bun)
    ingredient_1 = Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", 100)
    ingredient_2 = Ingredient(INGREDIENT_TYPE_SAUCE, "sour cream", 200)
    burger.add_ingredient(ingredient_1)
    burger.add_ingredient(ingredient_2)
    burger.move_ingredient(0, 1)
    assert burger.ingredients[1].get_name() == "hot sauce"


def test_get_price_success():
    burger = Burger()
    bun_mock = Mock()
    bun_mock.get_price.return_value = 100
    burger.set_buns(bun_mock)
    ingredient_mock = Mock()
    ingredient_mock.get_price.return_value = 100
    burger.add_ingredient(ingredient_mock)
    assert burger.get_price() == 300


def test_get_receipt_success():
    burger = Burger()
    bun = Bun("black bun", 100)
    burger.set_buns(bun)
    ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", 100)
    burger.add_ingredient(ingredient)
    expected_receipt = (
        '(==== black bun ====)\n'
        '= sauce hot sauce =\n'
        '(==== black bun ====)\n\n'
        'Price: 300'
    )
    assert burger.get_receipt() == expected_receipt
