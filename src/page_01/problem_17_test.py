from .problem_17 import number_letter_counts, solution, to_english

def test_to_english():
    assert to_english(1) == 'one'
    assert to_english(15) == 'fifteen'
    assert to_english(20) == 'twenty'
    assert to_english(22) == 'twenty two'
    assert to_english(60) == 'sixty'
    assert to_english(64) == 'sixty four'
    assert to_english(100) == 'one hundred'
    assert to_english(297) == 'two hundred and ninety seven'
    assert to_english(811) == 'eight hundred and eleven'
    assert to_english(1000) == 'one thousand'

def test_number_letter_counts():
    assert number_letter_counts(5) == 19

def test_solution():
    assert solution() == 21124
