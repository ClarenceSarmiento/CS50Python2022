from twttr import shorten

def test_lower():
    assert(shorten("twitter")) == "twttr"

def test_upper():
    assert(shorten("TWITTER")) == "TWTTR"

def test_numbers():
    assert(shorten("TwiTT3r")) == "TwTT3r"

def test_symbols():
    assert(shorten("!!tWitTer")) == "!!tWtTr"