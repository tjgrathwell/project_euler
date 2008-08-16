# THE RULES
# 1. Only I, X, and C can be used as the leading numeral in part of a subtractive pair.
# 2. I can only be placed before V and X.
# 3. X can only be placed before L and C.
# 4. C can only be placed before D and M.
# therefore, we generate this helpful dict of all the possible roman numerals and values
values = {'I' : 1, 'V' : 5, 'X' : 10, 'L' : 50, 'C' : 100, 'D' : 500, 'M' : 1000, 'IV' : 4, 'IX' : 9, 'XL' : 40, 'XC' : 90, 'CD' : 400, 'CM' : 900}
letters = dict([(v,k) for k,v in zip(values.keys(), values.values())])
sorted_values = sorted(letters.keys())
sorted_values.reverse()

def parse_roman(roman):
    '''
    get the numerical value of a valid roman numeral
    
    march forward building up single numerals or pairs from the number, until you either
        1) encounter the same numeral twice in a row
        2) 'fall' from a higher denomination to a lower one
        3) reach the end of the string
    in any of these cases, put the value of the numeral group into the accumulator
    
    no error checking is done; if you wanted some, you could have a value() function instead
    of referencing the values[] dict directly
    '''
    total = 0
    accumulated = []
    for c in roman:
        if accumulated:
            if values[c] <= values[accumulated[-1]]:
                total += values[''.join(accumulated)]
                accumulated = []
        accumulated.append(c)
    total += values[''.join(accumulated)]
    return total
    
def make_roman(number):
    '''
    return the minimal roman numeral equivilent of some number
    '''
    roman = []
    while number:
        for val in sorted_values:
            if val <= number:
                roman.append(letters[val])
                number -= val
                break
            
    return ''.join(roman)
    
saved = 0
for line in open('roman.txt'):
    line = line.strip()
    parsed = parse_roman(line)
    smaller = make_roman(parsed) 
    diff = len(line) - len(smaller)
    print line, parsed, smaller, diff
    saved += diff
print '%d saved' % saved