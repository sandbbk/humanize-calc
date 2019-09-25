import operator

# define consts

digits = '0123456789'

ops = '+-*/'

ops_dict = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}

allchars = digits + ops + '= '

inv = 'invalid input'

calc_dict = {'0': 'zero', '1': 'one', '2': 'two', '3': 'three', '4': 'four', '5': 'five', '6': 'six',
             '7': 'seven', '8': 'eight', '9': 'nine', '10': 'ten', '11': 'eleven', '12': 'twelve', '13':
             'thirteen', '14': 'fourteen', '15': 'fifteen', '16': 'sixteen', '17': 'seventeen', '18': 'eighteen',
             '19': 'nineteen', '20': 'twenty', '30': 'thirty', '40': 'forty', '50': 'fifty', '60': 'sixty',
             '70': 'seventy', '80': 'eighty', '90': 'ninety', '+': 'plus', '-': 'minus',
             '*': 'multiply', '/': 'divide', '=': 'equals'}

# this function provides the main operations of the humanize calculator.

def calc(string=None):

    if string is None:
        string = input('Type an expression like "2 + 3 = 5" or exit() to finish the program. \n'
                       'Your string is invalid, if it contains characters besides digits, symbols of operator and \n'
                       'equals with whitespace or contains negative numbers, and if your string is invalid like \n'
                       'mathematical expression (left part not equals to right part), or bit-depth of operands or \n'
                       'result greater than three: \n\n')

    if string in ('exit()', 'exit', 'q', '-q', 'quit'):
        exit(0)

    if len(set(string).difference(allchars)) != 0:
        return inv

    sstring = string.strip()  # deleting whitespaces around the string
    eqtuple = sstring.partition('=')  # tuple as ('xxx', '=', 'xxx')
    end = eqtuple[2].strip()

    if not end.isdecimal() or len(end) > 3:
        return inv

    find = 0
    lefttup = None

    for char in eqtuple[0]:  # before =
        for oper in ops:
            if char == oper:
                lefttup = eqtuple[0].partition(char)
                find += 1

    if find != 1:
        return inv

    first = lefttup[0].strip()
    second = lefttup[2].strip()

    if not(first.isdecimal() and second.isdecimal()) or len(first) > 3 or len(second) > 3:
        return inv

    try:
        if not ops_dict[lefttup[1]](int(lefttup[0]), int(lefttup[2])) == int(end):
            return inv
    except ZeroDivisionError:
        return "ZeroDivisionError"

    tup_of_strings = (first, lefttup[1], second, '=', end)
    endlist = []

    for string in tup_of_strings:
        num = calc_dict.get(string)
        if num:
            endlist.append(num)
        else:
            num = int(string)
            hundred = num // 100
            ten = (num % 100) // 10
            one = (num % 100) % 10
            if hundred:
                endlist.append(calc_dict[str(hundred)] + ' hundred')
            if ten == 1 and one:
                endlist.append(calc_dict[str(num % 100)])
                continue
            elif ten:
                endlist.append(calc_dict[str(ten) + '0'])
            if one:
                endlist.append(calc_dict[str(one)])
    return ' '.join(endlist)


if __name__ == "__main__":
    while True:
        print(calc())
