def __test():
    print("Local Copy!")
    return


def match_data(current, all_data):
    import json
    from collections import OrderedDict

    def try_dict(current_dict, all_data_dict):
        if "{" in current_dict and "{" in all_data_dict:
            try:
                try:
                    all_data_dict = json.loads(all_data_dict, object_pairs_hook=OrderedDict)
                except ValueError:
                    return None
                except SyntaxError:
                    return current_dict
                try:
                    current_dict = json.loads(current_dict, object_pairs_hook=OrderedDict)
                except ValueError:
                    return None
                except SyntaxError:
                    return all_data_dict
                if isinstance(current_dict, dict):
                    for key in all_data_dict:
                        current_dict.setdefault(key, all_data_dict[key])
                    return current_dict
            except ValueError:
                return None

    dict_return = try_dict(current, all_data)
    if dict_return is not None:
        return dict_return

    was_string = False
    if isinstance(current, str):
        was_string = True
        current = current.replace(", ", ",").split(",")
        all_data = all_data.replace(", ", ",").split(",")

    for element in all_data:
        if element not in current:
            current.append(element)
    for element in current:
        if element not in all_data:
            current.remove(element)

    if was_string:
        current = ",".join(current)

    return current


def count_project_lines(project_path="", file_types=[], includes=[], excludes=[]):
    import os

    if project_path == "":
        project_path = os.getcwd()

    try:
        project_files = os.listdir(project_path)
    except FileNotFoundError:
        return None

    if isinstance(file_types, str):
        file_types = file_types.split(",")

    if isinstance(includes, str):
        includes = includes.split(",")

    if isinstance(excludes, str):
        excludes = excludes.split(",")

    lines = 0

    if len(includes) > 0:
        for project_file in project_files:
            for file in includes:
                if file in project_file and not any([file in out_file for out_file in excludes]):
                    try:
                        io_file = open(file, 'r')
                    except (PermissionError, FileNotFoundError, IsADirectoryError):
                        continue
                    data = io_file.readlines()
                    io_file.close()
                    lines += len(data)
        return lines

    if len(file_types) > 0:
        for file_type in file_types:
            for file in project_files:
                if file_type in file and not any([file in out_file for out_file in excludes]):
                    try:
                        io_file = open(file, 'r')
                    except (PermissionError, FileNotFoundError, IsADirectoryError):
                        continue
                    data = io_file.readlines()
                    io_file.close()
                    lines += len(data)
    else:
        for file in project_files:
            if not any([file in out_file for out_file in excludes]):
                try:
                    io_file = open(file, 'r')
                except (PermissionError, FileNotFoundError, IsADirectoryError):
                    continue
                data = io_file.readlines()
                io_file.close()
                lines += len(data)

    return lines


class Switch(object):
    expression_value = ""

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        pass

    def __init__(self, expression):
            self.expression_value = expression

    def __call__(self, value=""):
        return self.case(value)

    def case(self, value=""):
        if value == "":
            return True
        if value == self.expression_value:
            return True
        return False

    def get_expression_value(self):
        return self.expression_value


def flip(data, point_num=""):

    if isinstance(data, bool):
        if data:
            return False
        else:
            return True

    if isinstance(data, int) and isinstance(point_num, int):
        if point_num >= data:
            distance = point_num - data
            return point_num + distance
        else:
            distance = data - point_num
            return point_num - distance

    if isinstance(data, int):
        return int(str(data)[::-1])
    if isinstance(data, str) or isinstance(data, list) or isinstance(data, tuple):
        return data[::-1]

    return None


def args2dict(args):
    """ Takes a list of command line arguments and converts it into a dictionary, catches invalid arguments.

    This function does not expect any manipulation of the command line arguments to be done before they are passed in,
    i.e. the first argument should still be the execution location.

    Expected Argument Formats:
        No dash (x):        value. follows a double dash parameter
        Single dash (-x):   flag. Indicates a boolean value, does not have extended arguments
        Double dash (--x):  parameter. Indicates a following value is present.

    Valid Examples (with function outputs):
        foo.exe -x                      => {"x": True}
        foo.exe --my-param "bar"        => {"my_param": "bar"}
        foo.exe -my-flag --y "bar" -z   => {"my_flag": True, "y": "bar", "z": True}

    Invalid Examples:
        foo.exe -x --x "bar"        (dictionaries cannot have duplicate keys)
        foo.exe --x -y              (x parameter was not given a value)


    Author: Conrad Selig

    :param args: list of command line arguments
    :return: dict containing parsed args, or None if invalid arguments were given
    """

    # boolean will denote if the next argument needs to be skipped, this is used after a parameter is found.
    skip_next = False
    # dictionary we'll be returning
    parsed_args = {}

    # for all the given arguments, skip the first one (execution location)
    for i, arg in enumerate(args[1:]):

        # if we are skipping this arg
        if skip_next:
            # reset the skip flag
            skip_next = False
            # go to the next iter
            continue

        # if there are no dashes
        if arg[0] != "-":
            # invalid arguments given, return None
            return None
        # else check if it a param and not just a flag
        elif arg[1] == "-":
            # convert the arg to a list so we can change individual letters
            arg = list(arg)
            # loop through the argument (except the first two dashes), replacing dashes with underscores.
            for j, letter in enumerate(arg[2:]):
                if letter == "-":
                    arg[j + 2] = "_"
            # convert the arg back to a string
            arg = "".join(arg)

            # check to make sure this key is not already being used
            if arg[2:] in parsed_args.keys():
                # return invalid
                return None

            # insert that param into the parsed dictionary, as well as a holder value until we can pick up the real
            # value
            parsed_args[arg[2:]] = "tmp"

            # check to make sure the next argument does not have any dashes, plus 2 is one for skipping the first arg
            # and one for "next arg"
            if args[i+2][0] == "-":
                # if it does, given args are invalid
                return None

            # given args are still valid, replace tmp value with real value, plus 2 is one for skipping the first arg
            # and one for "next arg"
            parsed_args[arg[2:]] = args[i+2]

            # set the skip next flag, so the next given argument is not processed normally
            skip_next = True

        # else given arg is a flag
        else:

            # convert the arg to a list so we can change individual letters
            arg = list(arg)
            # loop through the argument (except the first two dashes), replacing dashes with underscores.
            for j, letter in enumerate(arg[1:]):
                if letter == "-":
                    arg[j + 1] = "_"
            # convert the arg back to a string
            arg = "".join(arg)

            # check to make sure this key is not already being used
            if arg[1:] in parsed_args.keys():
                # return invalid
                return None

            # add the flag to parsed args dict, with value True
            parsed_args[arg[1:]] = True

    # return the dictionary
    return parsed_args
