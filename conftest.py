import pytest
from unittest.mock import Mock

from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


@pytest.fixture
def mock_bun():
    """Фикстура для создания мока булочки"""
    mock = Mock(spec=Bun)
    mock.get_name.return_value = "Test Bun"
    mock.get_price.return_value = 100.0
    return mock


@pytest.fixture
def mock_ingredient():
    """Фикстура для создания мока ингредиента"""
    mock = Mock(spec=Ingredient)
    mock.get_name.return_value = "Test Ingredient"
    mock.get_price.return_value = 50.0
    mock.get_type.return_value = INGREDIENT_TYPE_SAUCE
    return mock


@pytest.fixture
def sample_buns():
    """Фикстура с тестовыми данными булочек"""
    return [
        Bun("black bun", 100),
        Bun("white bun", 200),
        Bun("red bun", 300)
    ]


@pytest.fixture
def sample_ingredients():
    """Фикстура с тестовыми данными ингредиентов"""
    return [
        Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", 100),
        Ingredient(INGREDIENT_TYPE_SAUCE, "sour cream", 200),
        Ingredient(INGREDIENT_TYPE_FILLING, "cutlet", 150)
    ]