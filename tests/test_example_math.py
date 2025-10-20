import pytest
import importlib

def _import_target():
    # Import the module being tested
    return importlib.import_module("src.example_math")

def test_import():
    mod = _import_target()
    assert mod is not None

# TODO: Add more unit tests for functions
# Example:
# def test_add():
#     mod = _import_target()
#     assert mod.add(1, 2) == 3