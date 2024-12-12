import pytest
from calculator import Calculator

@pytest.fixture
def calc_ops():
    return Calculator()

def test_add(calc_ops):
    assert calc_ops.add(2, 3) == 5
    assert calc_ops.add(-1, 1) == 0
    assert calc_ops.add(0, 0) == 0

def test_subtract(calc_ops):
    assert calc_ops.subtract(7, 4) == 3
    assert calc_ops.subtract(0, 5) == -5
    assert calc_ops.subtract(-3, -7) == 4

def test_multiply(calc_ops):
    assert calc_ops.multiply(3, 5) == 15
    assert calc_ops.multiply(-2, 4) == -8
    assert calc_ops.multiply(0, 10) == 0

def test_divide(calc_ops):
    assert calc_ops.divide(10, 2) == 5.0
    assert calc_ops.divide(9, 3) == 3.0
    with pytest.raises(ValueError):
        calc_ops.divide(10, 0)

def test_power(calc_ops):
    assert calc_ops.power(2, 3) == 8
    assert calc_ops.power(5, 0) == 1
    assert calc_ops.power(3, -2) == pytest.approx(0.1111, rel=1e-3)

def test_modulus(calc_ops):
    assert calc_ops.modulus(10, 3) == 1
    assert calc_ops.modulus(7, 5) == 2
    assert calc_ops.modulus(0, 3) == 0
