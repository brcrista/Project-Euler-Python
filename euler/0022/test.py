from solution import alphabetic_value, name_score, solution

def test_alphabetic_value():
    assert alphabetic_value('a') == 1
    assert alphabetic_value('A') == 1
    assert alphabetic_value('b') == 2
    assert alphabetic_value('B') == 2

def test_name_score():
    assert name_score('COLIN', 938) == 49714

def test_solution():
    assert solution() == 871198282
