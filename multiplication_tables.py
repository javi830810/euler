import sys
__author__ = 'jdepaula'

def l_char_fill(number, char, count):
    str_numb = str(number)

    if len(str_numb) >= count:
        return str_numb

    for x in range(0, count - len(str_numb)):
        str_numb = char + str_numb

    return str_numb


for x in range(1,13):
    row = ''
    for y in range(1,13):
        row += l_char_fill(x*y,' ', 4)
    print row
