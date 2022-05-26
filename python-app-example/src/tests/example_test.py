# assert de def test_add_one - asevera que si al método le paso 3, me da 4

import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../app_example")))
import example


def test_add_one():
    assert example.add_one(3)==4  
