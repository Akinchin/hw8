
"""
Протестируйте классы из модуля homework/models.py
"""
import pytest
from selenium.webdriver.common.devtools.v85.log import clear

from homework.models import Product, Cart


@pytest.fixture
def product():
    return Product("book", 100, "This is a book", 1000)

@pytest.fixture
def product1():
    return Product("ps", 500, "This is gamestation", 100)



@pytest.fixture
def cart():
    return Cart()


class TestProducts:
    """
    Тестовый класс - это способ группировки ваших тестов по какой-то тематике
    Например, текущий класс группирует тесты на класс Product
    """

    def test_product_check_quantity(self, product):
        # TODO напишите проверки на метод check_quantity
        assert product.check_quantity(1000) is True
        assert product.check_quantity(0) is True
        assert product.check_quantity(1001) is False
        assert product.check_quantity(500) is True



    def test_product_buy(self, product):
        # TODO напишите проверки на метод buy
        assert product.buy(1) == 1001

    def test_product_buy_more_than_available(self, product):
        # TODO напишите проверки на метод buy,
        #  которые ожидают ошибку ValueError при попытке купить больше, чем есть в наличии
        with pytest.raises(ValueError):
            assert product.buy(2000)


class TestCart:
    """
    TODO Напишите тесты на методы класса Cart
        На каждый метод у вас должен получиться отдельный тест
        На некоторые методы у вас может быть несколько тестов.
        Например, негативные тесты, ожидающие ошибку (используйте pytest.raises, чтобы проверить это)
    """
    def test_add_in_cart(self, product, cart):
        cart.add_product(product, 100)
        assert cart.products[product] == 100


    def test_remove(self, product, cart):
        cart.add_product(product,buy_count=5)
        cart.remove_product(product, remove_count=4)
        assert cart.products[product] == 1

    def test_full_remove(self, product, cart):
        cart.remove_product(product)
        assert product not in cart.products

    def test_clear_cart(self,product, cart):
        cart.add_product(product, 20)
        cart.remove_product(product, remove_count=20)
        assert len(cart.products) == 0

    def test_total_price(self, product, product1, cart):
        cart.add_product(product, 25)
        cart .add_product(product1, 30)
        assert cart.get_total_price() ==17500


    def test_buy_with_insufficient_stock(self, cart, product, product1):
        cart.add_product(product1,101)

        # Покупка должна вызвать ValueError из-за недостатка товара
        with pytest.raises(ValueError, match=f"Товара не хватает на складе"):
            cart.buy()



