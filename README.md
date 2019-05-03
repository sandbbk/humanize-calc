# humanize-calc
Description
------------------------------------------------------------------------------------------------
Simple program humanize-calc, which converts string like `5 + 7 = 12`
into `five plus seven equals twelve`.

Installation and use
------------------------------------------------------------------------------------------------

Yo may simple copy and paste text of program to Your code, or clone
repo to local storage:

    $ git clone https://github.com/sandbbk/humanize_calc.git
    
and inport `from humanize_calc import calc` in Your code.
Or run it like this:

    $ python3 humanize_calc.py
    
### Use:

Type an expression like `2 + 3 = 5` or `exit()` to finish the program. Your string is invalid,
if it contains characters besides digits, symbols of operator and equals with whitespace or
contains negative numbers, and if your string is invalid like mathematical expression
(left part not equals to right part), or bit-depth of operands or result greater than three.

### Run tests:

Type in the command line:

    $ cd humanize_calc
    $ py.test
