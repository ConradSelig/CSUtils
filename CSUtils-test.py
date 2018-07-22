import CSUtils
import traceback

from collections import OrderedDict


def test_match_data():

    errors = 0

    try:
        assert(CSUtils.match_data("a,c,e,f", "a,b,c,d,e") == "a,c,e,b,d")
        assert(CSUtils.match_data([1, 3, 5, 6], [1, 2, 3, 4, 5]) == [1, 3, 5, 2, 4])
        assert(CSUtils.match_data('{"a": [1, 2], "c": [5, 6], "e": [9, 10]}',
                                  '{"a": [1, 2], "b": [3, 4], "c": [5, 6], "d": [7, 8], "e": [9, 10]}') ==
               OrderedDict([('a', [1, 2]), ('c', [5, 6]), ('e', [9, 10]), ('b', [3, 4]), ('d', [7, 8])]))
    except AssertionError:
        errors += 1

    return errors


def test_line_count():

    errors = 0

    file = open("CSUtils-test.py", "r")
    data = file.readlines()
    file.close()

    lines = len(data)

    try:
        assert(CSUtils.count_project_lines(includes="CSUtils-test.py") == lines)
        assert(CSUtils.count_project_lines() != lines)
    except AssertionError:
        errors += 1

    return errors


def test_switch():
    return 0


def run_tests():
    test_results = 0

    test_results += test_match_data()
    test_results += test_line_count()
    test_results += test_switch()

    return test_results


if __name__ == "__main__":
    print(run_tests())
