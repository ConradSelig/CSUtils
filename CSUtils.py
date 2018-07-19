
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


def count_project_lines(project_path="", file_types=[], file_names=[], discludes=[]):
    import os

    if project_path == "":
        project_path = os.getcwd()

    try:
        project_files = os.listdir(project_path)
    except FileNotFoundError:
        return None

    lines = 0

    if len(file_names) > 0:
        for project_file in project_files:
            for file in file_names:
                if file in project_file and not any([file in out_file for out_file in discludes]):
                    try:
                        io_file = open(file, 'r')
                    except PermissionError:
                        continue
                    except FileNotFoundError:
                        continue
                    data = io_file.readlines()
                    io_file.close()
                    lines += len(data) + 1
        return lines

    if len(file_types) > 0:
        for file_type in file_types:
            for file in project_files:
                if file_type in file and not any([file in out_file for out_file in discludes]):
                    try:
                        io_file = open(file, 'r')
                    except PermissionError:
                        continue
                    except FileNotFoundError:
                        continue
                    data = io_file.readlines()
                    io_file.close()
                    lines += len(data) + 1
    else:
        for file in project_files:
            if not any([file in out_file for out_file in discludes]):
                try:
                    io_file = open(file, 'r')
                except PermissionError:
                    continue
                except FileNotFoundError:
                    continue
                data = io_file.readlines()
                io_file.close()
                lines += len(data) + 1

    return lines
