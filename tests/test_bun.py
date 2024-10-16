import pytest
from praktikum.bun import Bun


@pytest.mark.parametrize("name, price, expected", [
    ("black bun", 100, "black bun"),
    ("white bun", 200, "white bun"),
    ("red bun", 300, "red bun")
])
def test_get_name_success(name, price, expected):
    bun = Bun(name, price)
    assert bun.get_name() == expected


@pytest.mark.parametrize("name, price, expected", [
    ("black bun", 100, 100),
    ("white bun", 200, 200),
    ("red bun", 300, 300)
])
def test_get_price_success(name, price, expected):
    bun = Bun(name, price)
    assert bun.get_price() == expected
