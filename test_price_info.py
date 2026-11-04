
import pytest
import price_info


# Test total shopping cost
def test_total_cost_shopping():
    result = price_info.total_cost_shopping()
    assert result == pytest.approx(46.75)


# Test cost of 10 apples
def test_cost_of_fruits_apple():
    result = price_info.cost_of_fruits('apple', 10)
    assert result == pytest.approx(12.00)


# Test cost of 2 watermelons
def test_cost_of_fruits_watermelon():
    result = price_info.cost_of_fruits('watermelon', 2)
    assert result == pytest.approx(13.00)
