# Write a program that converts a positive integer into the Roman number system. The Roman number
# system has digits I (1), V (5), X (10), L (50), C(100), D(500) and M(1000). Numbers up to 3999 are  formed according to the following rules:
# a) As in the decimal system, the thousands, hundreds, tens and ones are expressed separately.
# b) The numbers 1 to 9 are expressed as: 1 I 6 VI 2 II 7 VII 3 III 8 VIII4 IV 9 IX 5 V (An I preceding a V or X is subtracted from the value, and there cannot be more than threeI’s in a row.)
# c) Tens and hundreds are done the same way, except that the letters X, L, C, and C, D, Mare used
# instead of I, V, X respectively.
# Example: Your program should take an input, such as 1978, and convert it to Roman numerals, MCMLXXVIII

def integer_to_roman(num):
    val = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4,
        1
    ]
    syms = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV",
        "I"
    ]
    roman_num = ''
    i = 0
    while num > 0:
        for _ in range(num // val[i]):
            roman_num += syms[i]
            num -= val[i]
        i += 1
    return roman_num

number = int(input("Enter a positive integer: "))
if number <= 0 or number > 3999:
    print("Please enter a positive integer between 1 and 3999.")
else:
    print("Roman numeral:", integer_to_roman(number))



