import pytest
from main import min_coins # Replace 'your_module_name' with the actual name of your Python file.

def test_min_coin():
    # Test Case 1: Basic test with common denominations
    coins = [1, 4, 6, 9, 14]
    target_amount = 26
    assert min_coins(coins, target_amount) == 3 

