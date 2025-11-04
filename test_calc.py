import pytest
from calc import add, sub, div, mul

def test_add():
   assert add(1,3) == 4

def test_mul():
   assert mul(5,5) == 25

def test_div():
   assert div(10,5) == 2

def test_sub():
   assert sub(10,5) == 5
