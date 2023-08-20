from plates import is_valid

def test_length():
    # maximum of 6 and minimum of 2 characters
    assert is_valid("WXCS2976") == False
    assert is_valid("WX") == True
    assert is_valid("KY7689") == True

def test_firstTwoCharacter():
    # must start with at least 2 letters
    assert is_valid("TY") == True
    assert is_valid("F5") == False
    assert is_valid("2976") ==  False

def test_symbols():
    # No periods, spaces, or punctuation marks are allowed
    assert is_valid("WXCS2#") == False
    assert is_valid("J@KOL!") == False

def test_format():
    # Numbers cannot be used in the middle of a plate; they must come at the end.
    # For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable.
    # The first number used cannot be a '0'
    assert is_valid("AAA222") == True
    assert is_valid("AAA22A") == False
    assert is_valid("AAA022") == False

