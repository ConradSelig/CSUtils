# CSUtils
A small set of Utilities designed by Conrad Selig for general use in almost any project.


## How to Install

Activate your virtual environment from the command line, run:
> pip install git+https://github.com/ConradSelig/CSUtils

To use in your code:
> import CSUtils <br>
> CSUtils.function(params)

or
> from CSUtils import function <br>
> function(params)

## Documentation

**match_data(current, all_data):**

* Take in two similar structures of data
* Currently Supports the following structures:
	* comma separated string
	* list
	* dictionary (does not remove elements)
* matches "current" to "all_data" by adding missing elements and removing extra elements - retains "current"'s original order.
* Example:
	* current = "a,c,d,f"
	* all = "a,b,c,d,e"
	* output = "a,c,d,b,e"

**count_project_lines(project_path="", file_types=[], file_names=[], discludes=[]):**
* Counts the lines of a project given specifying parameters.
* Takes the name of the directory to count, as well as:
    * List of string file type ie [".py",".txt"].
    * List of file names to count ie ["manage.py","test.py"].
    * List of files not to include in the count ie ["temp.py","notes.txt"].
* Uses current working directory if not directory is provided.
* Outputs 0 if project directory not found.
* Adds 0 to count for every file provided not found, or files with permissions errors (".gitignore" for example).

**class Switch(expression):**
* A basic implementation of Switch Case in Python.
* How to use:
    * Option 1: Use the Switch Case as a namespace (example 1)
    * Option 2: Instantiate the class to a variable with an expression, then call your_var.case(case_value).
* Switch.case(value) returns a boolean.
* Switch.case() return True (default case)
* Given a conditional statement, Switch evaluates it to a boolean.<br>

Ready to use examples:
> from CSUtils import Switch <br>
> import datetime <br>
>
> with Switch(datetime.datetime.now().weekday()) as case: <br>
>   &nbsp;&nbsp;&nbsp;&nbsp;if case(0): <br>
>       &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;day = "Monday" <br>
>   &nbsp;&nbsp;&nbsp;&nbsp;elif case(1): <br>
>       &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;day = "Tuesday" <br>
>   &nbsp;&nbsp;&nbsp;&nbsp;elif case(2): <br>
>       &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;day = "Wednesday" <br>
>   &nbsp;&nbsp;&nbsp;&nbsp;elif case(3): <br>
>       &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;day = "Thursday" <br>
>   &nbsp;&nbsp;&nbsp;&nbsp;elif case(4): <br>
>       &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;day = "Friday" <br>
>   &nbsp;&nbsp;&nbsp;&nbsp;elif case(5): <br>
>        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;day = "Saturday" <br>
>   &nbsp;&nbsp;&nbsp;&nbsp;elif case(6): <br>
>        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;day = "Sunday" <br>
>   &nbsp;&nbsp;&nbsp;&nbsp;elif case(): <br>
>        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;day = "No day found with that index."
>
> print(day)

Using it like this allows the switch to be persistent, this means more case statements can be used with the same expression later in the code.

> from CSUtils import Switch <br>
>
> switch = Switch(1 == 1)
>
> if switch.case(True): <br>
> &nbsp;&nbsp;&nbsp;&nbsp;print("Expression True!") <br>
> elif switch.case(False): <br>
> &nbsp;&nbsp;&nbsp;&nbsp;print("Expression False!") <br>


This readme was built with https://pandao.github.io/editor.md/en.html and https://jbt.github.io/markdown-editor/. Thank you!
