# Example Math Module

The `example_math` module provides basic mathematical operations for integers, such as addition and multiplication. It is designed to be simple and user-friendly, making it suitable for educational purposes or straightforward arithmetic computations in various applications.

## Example Usage

Here is a quick example of how you can use the functions provided by the `example_math` module:

```python
from src.example_math import add, multiply

# Addition of two integers
sum_result = add(2, 3)
print(f"Sum: {sum_result}")  # Output: Sum: 5

# Multiplication of two integers
product_result = multiply(4, 5)
print(f"Product: {product_result}")  # Output: Product: 20
```

## API Overview

The module includes the following functions:

### `add(a: int, b: int) -> int`

Adds two integers and returns the result.

- **Parameters:**
  - `a` (int): The first integer operand.
  - `b` (int): The second integer operand.

- **Returns:** 
  - The sum of `a` and `b` as an integer.

### `multiply(a: int, b: int) -> int`

Multiplies two integers and returns the result.

- **Parameters:**
  - `a` (int): The first integer operand.
  - `b` (int): The second integer operand.

- **Returns:** 
  - The product of `a` and `b` as an integer.

These straightforward functions can be directly used to perform basic arithmetic operations on integer values.