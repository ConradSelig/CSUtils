import CSUtils
import calendar

import datetime
from collections import OrderedDict


def test_match_data():

    try:
        assert(CSUtils.match_data("a,c,e,f", "a,b,c,d,e") == "a,c,e,b,d")
        assert(CSUtils.match_data([1, 3, 5, 6], [1, 2, 3, 4, 5]) == [1, 3, 5, 2, 4])
        assert(CSUtils.match_data('{"a": [1, 2], "c": [5, 6], "e": [9, 10]}',
                                  '{"a": [1, 2], "b": [3, 4], "c": [5, 6], "d": [7, 8], "e": [9, 10]}') ==
               OrderedDict([('a', [1, 2]), ('c', [5, 6]), ('e', [9, 10]), ('b', [3, 4]), ('d', [7, 8])]))
    except AssertionError:
        return 1

    return 0


def test_line_count():

    file = open("CSUtils-test.py", "r")
    data = file.readlines()
    file.close()

    lines = len(data)

    try:
        assert(CSUtils.count_project_lines(includes="CSUtils-test.py") == lines)
        assert(CSUtils.count_project_lines() != lines)
    except AssertionError:
        return 1

    return 0


def test_switch():

    day_of_week = datetime.date.today()
    day_of_week = calendar.day_name[day_of_week.weekday()]

    with CSUtils.Switch(datetime.datetime.now().weekday()) as case:
        if case(0):
            day = "Monday"
        elif case(1):
            day = "Tuesday"
        elif case(2):
            day = "Wednesday"
        elif case(3):
            day = "Thursday"
        elif case(4):
            day = "Friday"
        elif case(5):
            day = "Saturday"
        elif case(6):
            day = "Sunday"
        elif case():
            day = "No day found with that index."

    switch = CSUtils.Switch(1 == 1)

    if switch.case(True):
        boolean_test = True
    elif switch.case(False):
        boolean_test = False
    else:
        boolean_test = None

    try:
        assert(day_of_week == day)
        assert(boolean_test is True)
    except AssertionError:
        return 1

    return 0


def test_flip():

    try:
        assert(CSUtils.flip(True) is False)
        assert(CSUtils.flip(False) is True)
        assert(CSUtils.flip("Hello World") == "dlroW olleH")
        assert(CSUtils.flip(["Hello", "World"]) == ["World", "Hello"])
        assert(CSUtils.flip(("Hello", "World")) == ("World", "Hello"))
        assert(CSUtils.flip(123456789) == 987654321)
        assert(CSUtils.flip(123456789) == 987654321)
        assert(CSUtils.flip(1, 10) == 19)
        assert(CSUtils.flip(3, 1) == -1)
        assert(CSUtils.flip(-5, 5) == 15)
        assert(CSUtils.flip(5, -5) == -15)
        assert(CSUtils.flip(-1, -10) == -19)
    except AssertionError:
        return 1

    return 0

def run_tests():

    test_results = 0

    test_results += test_match_data()
    test_results += test_line_count()
    test_results += test_switch()
    test_results += test_flip()

    return test_results


if __name__ == "__main__":
    print(run_tests())
