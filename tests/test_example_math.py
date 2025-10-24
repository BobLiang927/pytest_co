Here's a pytest module that tests the `sub` and `multiply` functions from the `src.example_math` module:

```python
import pytest
from src.example_math import sub, multiply

def test_sub():
    # Test valid cases
    assert sub(10, 5) == 5
    assert sub(0, 0) == 0
    assert sub(-5, -3) == -2
    assert sub(5, 10) == -5

    # Test invalid cases (these should raise TypeError)
    with pytest.raises(TypeError):
        sub(10.5, 5)
    with pytest.raises(TypeError):
        sub("10", 5)
    with pytest.raises(TypeError):
        sub(10, None)

def test_multiply():
    # Test valid cases
    assert multiply(3, 4) == 12
    assert multiply(0, 5) == 0
    assert multiply(-2, 3) == -6
    assert multiply(-3, -3) == 9

    # Test invalid cases (these should raise TypeError)
    with pytest.raises(TypeError):
        multiply(3.5, 4)
    with pytest.raises(TypeError):
        multiply("3", 4)
    with pytest.raises(TypeError):
        multiply(3, None)
```

**Explanation:**
- The functions are tested for both valid and invalid inputs.
- Valid tests cover a range of integer inputs, including positive, zero, and negative values.
- Invalid tests check for non-integer inputs like floating-point numbers, strings, and `None`, expecting a `TypeError`. This assumes the functions strictly require integers based on their type hints.