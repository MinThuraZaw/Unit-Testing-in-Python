import pytest
from ShoppingCart import ShoppingCart

#test - can create instance of ShoppingCart class
#test - can add item price
@pytest.fixture()
def shopping_cart():
    cart = ShoppingCart()
    cart.add_item_price('coffee cup', 5)
    cart.add_item_price('mouse', 50)
    return cart


#test - can add item
def test_can_calculate_total(shopping_cart):
    shopping_cart.add_item('coffee cup')
    assert shopping_cart.calculate_total() == 5


def test_get_total_with_multiple_items(shopping_cart):
    shopping_cart.add_item('mouse')
    shopping_cart.add_item('coffee cup')
    assert shopping_cart.calculate_total() == 55


def test_can_add_discount_rule(shopping_cart):
    shopping_cart.add_discount('mouse', 5, 20)


def test_can_apply_discount_rule(shopping_cart):
    shopping_cart.add_discount('mouse', 3, 85)
    shopping_cart.add_item('mouse')
    shopping_cart.add_item('mouse')
    shopping_cart.add_item('mouse')
    assert shopping_cart.calculate_total() == 85


def test_exception_with_bad_item(shopping_cart):
    with pytest.raises(Exception):
        shopping_cart.add_item('headphone')
