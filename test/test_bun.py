import pytest
from praktikum.praktikum import Bun

# Тесты для класса Bun
class TestBun:

    @pytest.mark.parametrize("name,price", [
        ("black bun", 100.0),
        ("white bun", 200.0),
        ("red bun", 300.0),
        ("", 0.0),
        ("special bun", 999.99)
    ])
    # Тестирование инициализации булочки с различными параметрами
    def test_bun_initialization(self, name, price):
        bun = Bun(name, price)
        assert bun.name == name and bun.price == price

    # Тестирование метода get_name
    def test_get_name(self):
        bun = Bun("Test Bun", 150.0)
        assert bun.get_name() == "Test Bun"

    # Тестирование метода get_price
    def test_get_price(self):
        bun = Bun("Test Bun", 150.0)
        assert bun.get_price() == 150.0

    # Тестирование, что имя остается неизменным после создания
    def test_get_name_after_creation(self):
        original_name = "Original Bun"
        bun = Bun(original_name, 100.0)
        bun.name = "Changed Bun"
        assert bun.get_name() == "Changed Bun"

    # Тестирование, что цена остается неизменной после создания
    def test_get_price_after_creation(self):
        original_price = 100.0
        bun = Bun("Test Bun", original_price)
        bun.price = 200.0
        assert bun.get_price() == 200.0