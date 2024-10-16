from praktikum.database import Database
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


def test_available_buns_success():
    data_burger = Database()
    bun_list = data_burger.available_buns()
    check_buns = []
    for bun in bun_list:
        check_buns.append({"name": bun.get_name(), "price": bun.get_price()})
    expected_buns = [
        {"name": "black bun", "price": 100},
        {"name": "white bun", "price": 200},
        {"name": "red bun", "price": 300}
    ]
    assert check_buns == expected_buns


def test_available_ingredients_success():
    data_burger = Database()
    ingredient_list = data_burger.available_ingredients()
    check_ingredients = []
    for i in ingredient_list:
        check_ingredients.append({"type": i.get_type(), "name": i.get_name(), "price": i.get_price()})
    expected_ingredient = [
        {"type": INGREDIENT_TYPE_SAUCE, "name": "hot sauce", "price": 100},
        {"type": INGREDIENT_TYPE_SAUCE, "name": "sour cream", "price": 200},
        {"type": INGREDIENT_TYPE_SAUCE, "name": "chili sauce", "price": 300},
        {"type": INGREDIENT_TYPE_FILLING, "name": "cutlet", "price": 100},
        {"type": INGREDIENT_TYPE_FILLING, "name": "dinosaur", "price": 200},
        {"type": INGREDIENT_TYPE_FILLING, "name": "sausage", "price": 300}
    ]
    assert check_ingredients == expected_ingredient
