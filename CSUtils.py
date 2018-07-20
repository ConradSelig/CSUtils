
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


def count_project_lines(project_path="", file_types=[], file_names=[], excludes=[]):
    import os

    if project_path == "":
        project_path = os.getcwd()

    try:
        project_files = os.listdir(project_path)
    except FileNotFoundError:
        return None

    if isinstance(file_types, str):
        file_types = file_types.split(",")

    if isinstance(file_names, str):
        file_names = file_names.split(",")

    if isinstance(excludes, str):
        excludes = excludes.split(",")

    lines = 0

    if len(file_names) > 0:
        for project_file in project_files:
            for file in file_names:
                if file in project_file and not any([file in out_file for out_file in excludes]):
                    try:
                        io_file = open(file, 'r')
                    except PermissionError:
                        continue
                    except FileNotFoundError:
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
                    except PermissionError:
                        continue
                    except FileNotFoundError:
                        continue
                    data = io_file.readlines()
                    io_file.close()
                    lines += len(data)
    else:
        for file in project_files:
            if not any([file in out_file for out_file in excludes]):
                try:
                    io_file = open(file, 'r')
                except PermissionError:
                    continue
                except FileNotFoundError:
                    continue
                data = io_file.readlines()
                io_file.close()
                lines += len(data)

    return lines


class Switch:
    expression_value = ""

    def __init__(self, expression):

        if isinstance(expression, str):
            self.expression_value = expression
            expression = expression.replace(" ", "")

            if "==" in expression:
                sides = expression.split("==")
                if sides[0] == sides[1]:
                    self.expression_value = True
                else:
                    self.expression_value = False

            elif ">=" in expression:
                sides = expression.split(">=")
                if sides[0] >= sides[1]:
                    self.expression_value = True
                else:
                    self.expression_value = False

            elif "<=" in expression:
                sides = expression.split("<=")
                if sides[0] <= sides[1]:
                    self.expression_value = True
                else:
                    self.expression_value = False

            elif ">" in expression:
                sides = expression.split(">")
                if sides[0] > sides[1]:
                    self.expression_value = True
                else:
                    self.expression_value = False

            elif "<" in expression:
                sides = expression.split("<")
                if sides[0] < sides[1]:
                    self.expression_value = True
                else:
                    self.expression_value = False
        else:
            self.expression_value = expression

    def case(self, value=""):
        if value == "":
            return True
        if value == self.expression_value:
            return True
        return False

    def get_expression_value(self):
        return self.expression_value
