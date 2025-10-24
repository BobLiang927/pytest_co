# Example Math Module

The `example_math` module provides basic arithmetic operations on integers. This library showcases fundamental functions for mathematical calculations, including subtraction and multiplication.

## Example Usage

```python
from src.example_math import sub, multiply

result_subtraction = sub(10, 5)
print(f"Subtraction Result: {result_subtraction}") # Output: Subtraction Result: 5

result_multiplication = multiply(10, 5)
print(f"Multiplication Result: {result_multiplication}") # Output: Multiplication Result: 50
```

## API Overview

### `sub(a: int, b: int) -> int`

Subtracts the second integer from the first.

- **Parameters:**
  - `a` (int): The minuend.
  - `b` (int): The subtrahend.

- **Returns:** 
  - `int`: The result of the subtraction.

- **Example:**
  ```python
  result = sub(8, 3) 
  print(result) # Output: 5
  ```

### `multiply(a: int, b: int) -> int`

Multiplies two integers.

- **Parameters:**
  - `a` (int): The first factor.
  - `b` (int): The second factor.

- **Returns:** 
  - `int`: The product of the multiplication.

- **Example:**
  ```python
  result = multiply(4, 5) 
  print(result) # Output: 20
  ``` 

This module is a straightforward utility for performing basic arithmetic calculations in Python.