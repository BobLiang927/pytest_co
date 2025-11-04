

import importlib

def _target():
    return importlib.import_module("src.example_math")

def test_import():
    mod = _target()
    assert mod is not None
