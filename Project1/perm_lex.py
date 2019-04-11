#
#Kelsey Deuth
#
#04/10/19
#
#Project1
#Section 12
#Purpose: To return all possible variations of a given string in dictionary order


def perm_gen_lex(a):
    a = list(a)
    newlist = []
    if len(a) == 1:  #base case
        return a
    if len(a) == 0:  #second base case 
        return a
    for char in range(len(a)):  
        first = a[char]  #takes first character in string
        rest = a[:char] + a[char + 1:]  #takes the rest of the characters in a string
        for order in perm_gen_lex(rest):  #recursively finds all variations of string
            newlist.append(first + order)  #appends variations to the newlist
    return newlist
 
