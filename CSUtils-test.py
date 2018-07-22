import CSUtils
import traceback


def test_match_data():
    return


def test_line_count():

    file = open("CSUtils-test.py", "r")
    data = file.readlines()
    file.close()

    lines = len(data)

    try:
        assert(CSUtils.count_project_lines(includes="CSUtils-test.py") == lines)
        assert(CSUtils.count_project_lines() != lines)
    except AssertionError:
        print(traceback.format_exc())

    return 0


def test_switch():
    return


if __name__ == "__main__":
    print(test_line_count())
