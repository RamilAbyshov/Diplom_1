import pytest

from praktikum.praktikum import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

# Тесты для класса Ingredient
class TestIngredient:

    @pytest.mark.parametrize("ingredient_type,name,price", [
        (INGREDIENT_TYPE_SAUCE, "hot sauce", 100.0),
        (INGREDIENT_TYPE_FILLING, "cutlet", 150.0),
        (INGREDIENT_TYPE_SAUCE, "", 0.0),
        (INGREDIENT_TYPE_FILLING, "special filling", 999.99)
    ])
    # Тестирование инициализации ингредиента с различными параметрами
    def test_ingredient_initialization(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)

        assert all([
        ingredient.type == ingredient_type,
        ingredient.name == name,
        ingredient.price == price
        ])

    # Тестирование метода get_price
    def test_get_price(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "Test Sauce", 75.0)
        assert ingredient.get_price() == 75.0

    # Тестирование метода get_name
    def test_get_name(self):
        ingredient = Ingredient(INGREDIENT_TYPE_FILLING, "Test Filling", 100.0)
        assert ingredient.get_name() == "Test Filling"

    # Тестирование метода get_type
    def test_get_type(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "Test Sauce", 75.0)
        assert ingredient.get_type() == INGREDIENT_TYPE_SAUCE

    # Тестирование неизменяемости атрибутов после создания
    def test_ingredient_attributes_immutability(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "Original", 100.0)

        ingredient.name = "Changed"
        ingredient.type = INGREDIENT_TYPE_FILLING
        ingredient.price = 200.0

        assert all([
            ingredient.get_name() == "Changed",
            ingredient.get_type() == INGREDIENT_TYPE_FILLING,
            ingredient.get_price() == 200.0
        ])
