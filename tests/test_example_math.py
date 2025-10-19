import pytest
from src.example_math import add, multiply

# Test cases for the add function
@pytest.mark.parametrize("a, b, expected", [
    (1, 2, 3),          # Basic addition
    (-1, 1, 0),         # Negative and positive
    (-1, -2, -3),       # Both negative
    (0, 0, 0),          # Both zeros
    (123456, 654321, 777777), # Large numbers
])
def test_add(a, b, expected):
    assert add(a, b) == expected

@pytest.mark.parametrize("a, b, expected_exception", [
    ("1", 2, TypeError),    # Invalid type: string
    (1.5, 2, TypeError),    # Invalid type: float
    (None, 2, TypeError),   # Invalid type: None
    ([1], 2, TypeError),    # Invalid type: list
    ({1: 2}, 2, TypeError), # Invalid type: dict
])
def test_add_invalid_inputs(a, b, expected_exception):
    with pytest.raises(expected_exception):
        add(a, b)

# Test cases for the multiply function
@pytest.mark.parametrize("a, b, expected", [
    (1, 2, 2),          # Basic multiplication
    (-1, 1, -1),        # Negative and positive
    (-1, -2, 2),        # Both negative
    (0, 5, 0),          # Multiplication with zero
    (123, 0, 0),        # Zero multiplied
    (10, 10, 100),      # Small numbers
    (12345, 6789, 83810205), # Larger numbers
])
def test_multiply(a, b, expected):
    assert multiply(a, b) == expected

@pytest.mark.parametrize("a, b, expected_exception", [
    ("1", 2, TypeError),    # Invalid type: string
    (1.5, 2, TypeError),    # Invalid type: float
    (None, 2, TypeError),   # Invalid type: None
    ([1], 2, TypeError),    # Invalid type: list
    ({1: 2}, 2, TypeError), # Invalid type: dict
])
def test_multiply_invalid_inputs(a, b, expected_exception):
    with pytest.raises(expected_exception):
        multiply(a, b)
