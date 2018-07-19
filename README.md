# CSUtils
A small set of Utilities designed by Conrad Selig for general use in almost any project.


## How to Install

Activate your virtual environment from the command line, run:
> pip install git+https://github.com/ConradSelig/CSUtils

To use in your code:
> import CSUtils
> CSUtils.function(params)

or
> from CSUtils import function
> function(params)

## Documentation

**match_data(current, all_data):**

* Take in two similar stuctures of data
* Currently Supports the following stuctures:
	* comma seperated string
	* list
	* dictionary (does not remove elements)
* matches "current" to "all_data" by adding missing elements and removing extra elements - retains "current"'s original order.
* Example:
	* current = "a,c,d,f"
	* all = "a,b,c,d,e"
	* output = "a,c,d,b,e"

This readme was built with https://pandao.github.io/editor.md/en.html and https://jbt.github.io/markdown-editor/. Thank you!
