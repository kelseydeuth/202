def bears(n):
    if n == 42:
        return True
    if n < 42:
        return False
    if n > 42:
        if n % 5 == 0:
            n = n - 42
        if n != 42 and n % 3 == 0 or n % 4 == 0:
            n = n - ((n % 10) * int((n / 10 % 10)))
        if n != 42 and n % 2 == 0:
            n = int(n) / 2
        elif n != 42:
            return False
    #while n >= 42:
    return bears(n)