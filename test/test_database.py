import pytest

from praktikum.praktikum import Database
from praktikum.praktikum import Bun
from praktikum.praktikum import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

# Тесты для класса Database
class TestDatabase:
    # Тестирование инициализации базы данных
    def test_database_initialization(self):
        db = Database()
        assert len(db.buns) == 3
        assert len(db.ingredients) == 6

    # Тестирование количества возвращаемых булочек
    def test_available_buns_count(self):
        db = Database()
        buns = db.available_buns()
        assert len(buns) == 3

    # Тестирование типов возвращаемых булочек
    def test_available_buns_types(self):
        db = Database()
        buns = db.available_buns()
        assert all(isinstance(bun, Bun) for bun in buns)

    # Тестирование названий возвращаемых булочек
    def test_available_buns_names(self):
        db = Database()
        buns = db.available_buns()
        bun_names = {bun.get_name() for bun in buns}
        assert bun_names == {"black bun", "white bun", "red bun"}

    # Тестирование количества возвращаемых ингредиентов
    def test_available_ingredients_count(self):
        db = Database()
        ingredients = db.available_ingredients()
        assert len(ingredients) == 6

    # Тестирование типов возвращаемых ингредиентов
    def test_available_ingredients_types(self):
        db = Database()
        ingredients = db.available_ingredients()
        assert all(isinstance(ingredient, Ingredient) for ingredient in ingredients)

    # Тестирование количества соусов
    def test_available_ingredients_sauce_count(self):
        db = Database()
        ingredients = db.available_ingredients()
        sauce_count = sum(1 for ing in ingredients if ing.get_type() == INGREDIENT_TYPE_SAUCE)
        assert sauce_count == 3

    # Тестирование количества начинок
    def test_available_ingredients_filling_count(self):
        db = Database()
        ingredients = db.available_ingredients()
        filling_count = sum(1 for ing in ingredients if ing.get_type() == INGREDIENT_TYPE_FILLING)
        assert filling_count == 3

    @pytest.mark.parametrize("ingredient_name", [
        "hot sauce", "sour cream", "chili sauce",  # соусы
        "cutlet", "dinosaur", "sausage"  # начинки
    ])
    # Тестирование наличия конкретного ингредиента
    def test_ingredient_exists(self, ingredient_name):
        db = Database()
        ingredients = db.available_ingredients()
        ingredient_names = [ing.get_name() for ing in ingredients]
        assert ingredient_name in ingredient_names

    @pytest.mark.parametrize("ingredient_name", [
        "hot sauce", "sour cream", "chili sauce",  # соусы
        "cutlet", "dinosaur", "sausage"  # начинки
    ])
    # Тестирование цены конкретного ингредиента
    def test_ingredient_price(self, ingredient_name):
        db = Database()
        ingredients = db.available_ingredients()
        ingredient = next(ing for ing in ingredients if ing.get_name() == ingredient_name)
        assert ingredient.get_price() in [100, 200, 300]

    # Тестирование цен булочек
    def test_bun_prices(self):
        db = Database()
        buns = db.available_buns()

        prices = [bun.get_price() for bun in buns]
        assert all(price in [100, 200, 300] for price in prices)