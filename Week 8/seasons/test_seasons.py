from seasons import day_to_minutes

def test_day_to_minutes():
    assert day_to_minutes(365) == "Five hundred twenty-five thousand, six hundred minutes"
    assert day_to_minutes(730) == "One million, fifty-one thousand, two hundred minutes"
    assert day_to_minutes(8331) == "Eleven million, nine hundred ninety-six thousand, six hundred forty minutes"

