from response import is_valid

def test_is_valid():
    assert is_valid("malan@harvard.edu") == "Valid"
    assert is_valid("clarence.sarmiento@g.batstate-u.edu.ph") == "Valid"
    assert is_valid("sarmiento.clarence1020@gmail.com") == "Valid"
    assert is_valid("malan@@@harvard.edu") == "Invalid"
    assert is_valid("sarmiento.clarence1020@gmail..com") == "Invalid"