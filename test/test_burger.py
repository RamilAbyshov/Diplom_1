import pytest
from unittest.mock import Mock
from praktikum.praktikum import Burger
from praktikum.praktikum import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

# Тесты для класса Burger
class TestBurger:
    # Тестирование инициализации бургера
    def test_burger_initialization(self):
        burger = Burger()
        assert burger.bun is None and burger.ingredients == []

    # Тестирование установки булочек
    def test_set_buns(self, mock_bun):
        burger = Burger()
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun

    # Тестирование добавления ингредиента
    def test_add_ingredient(self, mock_ingredient):
        burger = Burger()
        burger.add_ingredient(mock_ingredient)
        assert len(burger.ingredients) == 1 and burger.ingredients[0] == mock_ingredient

    # Тестирование удаления ингредиента
    def test_remove_ingredient(self, mock_ingredient):
        burger = Burger()
        burger.add_ingredient(mock_ingredient)
        burger.add_ingredient(Mock(spec=Ingredient))
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 1

    # Тестирование перемещения ингредиента
    def test_move_ingredient(self, mock_ingredient):
        burger = Burger()
        mock_ingredient2 = Mock(spec=Ingredient)
        mock_ingredient3 = Mock(spec=Ingredient)

        burger.add_ingredient(mock_ingredient)
        burger.add_ingredient(mock_ingredient2)
        burger.add_ingredient(mock_ingredient3)

        burger.move_ingredient(0, 2)
        assert burger.ingredients[2] == mock_ingredient

    @pytest.mark.parametrize("bun_price,ingredient_prices,expected_total", [
        (100.0, [50.0, 75.0], 325.0),  # 100*2 + 50 + 75
        (200.0, [100.0], 500.0),  # 200*2 + 100
        (150.0, [], 300.0),  # 150*2 + 0
        (0.0, [0.0, 0.0], 0.0)  # 0*2 + 0 + 0
    ])
    # Параметризованный тест для расчета цены бургера
    def test_get_price(self, mock_bun, mock_ingredient, bun_price, ingredient_prices, expected_total):
        burger = Burger()
        mock_bun.get_price.return_value = bun_price
        burger.set_buns(mock_bun)

        for price in ingredient_prices:
            ingredient_mock = Mock(spec=Ingredient)
            ingredient_mock.get_price.return_value = price
            burger.add_ingredient(ingredient_mock)

        assert burger.get_price() == expected_total

    # Тестирование расчета цены без установленной булочки
    def test_get_price_without_bun(self):
        burger = Burger()

        mock_ingredient = Mock(spec=Ingredient)
        mock_ingredient.get_price.return_value = 100.0
        burger.add_ingredient(mock_ingredient)

        with pytest.raises(AttributeError):
            burger.get_price()

    # Тестирование формирования чека
    def test_get_receipt(self, mock_bun, mock_ingredient):
        burger = Burger()

        mock_bun.get_name.return_value = "Test Bun"
        mock_ingredient.get_type.return_value = INGREDIENT_TYPE_SAUCE
        mock_ingredient.get_name.return_value = "Test Sauce"

        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)

        receipt = burger.get_receipt()

        assert all([
            "(==== Test Bun ====)" in receipt,
            "= sauce Test Sauce =" in receipt,
            "Price:" in receipt,
            "Test Bun" in receipt
        ]), "Чек содержит не все необходимые элементы"

    # Тестирование чека с несколькими ингредиентами
    def test_get_receipt_with_multiple_ingredients(self, mock_bun):

        burger = Burger()

        mock_bun.get_name.return_value = "Special Bun"
        mock_bun.get_price.return_value = 100.0
        burger.set_buns(mock_bun)

        sauce_mock = Mock(spec=Ingredient)
        sauce_mock.get_type.return_value = INGREDIENT_TYPE_SAUCE
        sauce_mock.get_name.return_value = "Hot Sauce"
        sauce_mock.get_price.return_value = 50.0

        filling_mock = Mock(spec=Ingredient)
        filling_mock.get_type.return_value = INGREDIENT_TYPE_FILLING
        filling_mock.get_name.return_value = "Cutlet"
        filling_mock.get_price.return_value = 75.0

        burger.add_ingredient(sauce_mock)
        burger.add_ingredient(filling_mock)

        receipt = burger.get_receipt()

        assert all([
            "(==== Special Bun ====)" in receipt,
            "= sauce Hot Sauce =" in receipt,
            "= filling Cutlet =" in receipt,
            "Price:" in receipt,
            "Price: 325" in receipt
        ]), "Чек содержит не все необходимые элементы или неверную цену"