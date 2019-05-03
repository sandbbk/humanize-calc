import pytest
from humanize_calc import calc


@pytest.mark.parametrize("string, out_string", [("2+7= 9", "two plus seven equals nine"), ("44 + 78=  122   ",
                                                "forty four plus seventy eight equals one hundred twenty two"),
                                                ("  1 + 2=3", "one plus two equals three"), ("222+111=333",
                                                "two hundred twenty two plus one hundred eleven equals three "
                                                "hundred thirty three"), ("12 + 888 = 900", "twelve plus eight hundred "
                                                "eighty eight equals nine hundred"), ("0+0=0", "zero plus zero equals "
                                                "zero")])
def test_valid_string_plus(string, out_string):
    assert calc(string) == out_string, f"error with processing {string}"


@pytest.mark.parametrize("string, out_string", [("2++7= 9", "invalid input"), ("44 + 78==  122   ", "invalid input"),
                                                ("  3 = 2+1", "invalid input"), ("2322+111=2433",
                                                "invalid input"), ("12 + 8 88 = 900", "invalid input"),
                                                ("1 2 + 8 88 = 9 00", "invalid input"),
                                                ("0+0=1", "invalid input"), ("p0+0=0", "invalid input"),
                                                ("0+0=0\n", "invalid input")])
def test_invalid_string_plus(string, out_string):
    assert calc(string) == out_string, f"error with processing  {string}"


@pytest.mark.parametrize("string, out_string", [("7-2= 5", "seven minus two equals five"), ("122 - 78=  44   ",
                                                "one hundred twenty two minus seventy eight equals forty four"),
                                                ("  3 - 2=1", "three minus two equals one"), ("222-111=111",
                                                "two hundred twenty two minus one hundred eleven equals one hundred"
                                                " eleven"), ("900 - 12 = 888 ", "nine hundred minus twelve equals eight"
                                                " hundred eighty eight"), ("0-0=0", "zero minus zero equals zero")])
def test_valid_string_minus(string, out_string):
    assert calc(string) == out_string, f"error with processing {string}"


@pytest.mark.parametrize("string, out_string", [("7--2= 5", "invalid input"), ("44 - 78==  -34   ", "invalid input"),
                                                ("  3 = 4-1", "invalid input"), ("2322-555=1767", "invalid input"),
                                                ("0-0=1", "invalid input")])
def test_invalid_string_minus(string, out_string):
    assert calc(string) == out_string, f"error with processing  {string}"


@pytest.mark.parametrize("string, out_string", [(" 5*2= 10", "five multiply two equals ten"), ("17 *50=850 ",
                                                "seventeen multiply fifty equals eight hundred fifty"),
                                                ("0 * 100 = 0", "zero multiply one hundred equals zero")])
def test_valid_string_multiply(string, out_string):
    assert calc(string) == out_string, f"error with processing  {string}"


@pytest.mark.parametrize("string, out_string", [("(7*2)= 14", "invalid input"), ("44 * 78==  3432   ", "invalid input"),
                                                (" * 1=0", "invalid input"), ("? * 4 = 12", "invalid input"),
                                                ("0*0=1", "invalid input"), ("3.4 * 5 = 17", "invalid input")])
def test_invalid_string_multiply(string, out_string):
    assert calc(string) == out_string, f"error with processing  {string}"


@pytest.mark.parametrize("string, out_string", [(" 10/2= 5", "ten divide two equals five"), ("740 /   20 = 37  ",
                                                "seven hundred forty divide twenty equals thirty seven")])
def test_valid_string_divide(string, out_string):
    assert calc(string) == out_string, f"error with processing  {string}"


@pytest.mark.parametrize("string, out_string", [(" 10/0= 999", "ZeroDivisionError"), ("740 /   2 0 = 37  ",
                                                "invalid input"), ("70\10 = 7", "invalid input")])
def test_invalid_string_divide(string, out_string):
    assert calc(string) == out_string, f"error with processing  {string}"
