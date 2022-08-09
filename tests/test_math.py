import sys
sys.path.append('./src')
import mathlib
 
def test_addition():
    output = mathlib.addition(2,4)
    assert output == 6, "Test Passed"
 
