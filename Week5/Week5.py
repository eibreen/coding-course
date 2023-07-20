import pytest 

def multipy_by_2(value):
 return value * 2
print(multipy_by_2(2))
def test_multipy_by_2():
    output= multipy_by_2(2)
    assert output == 4
