#
#Kelsey Deuth
#
#04/10/19
#
#Section 12
#Purpose: returns a string representing a number in a different base system


def convert(num, b):
    """Recursive function that returns a string representing num in the base b"""
    alphabet = ["A", "B", "C", "D", "E", "F"]
    n = 0
    quo = num // b
    rem = num % b
    if quo == 0:
        return rem
    if rem >= 10:
        while rem % 10 != n:
            n = n + 1
        rem = alphabet[n]
    return str(convert(quo, b)) + str(rem)

