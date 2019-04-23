from stack_array import Stack

# You do not need to change this class
class PostfixFormatException(Exception):
    pass

def postfix_eval(input_str):
    """Evaluates a postfix expression"""
    """Input argument:  a string containing a postfix expression where tokens 
    are space separated.  Tokens are either operators + - * / ^ or numbers
    Returns the result of the expression evaluation. 
    Raises an PostfixFormatException if the input is not well-formed"""
    input_str = input_str.split(" ")
    stack = Stack()
    ops = ['+', '-', '*', '/', '^']
    for num in input_str:
        if num not in ops:
            stack = push(stack, num)
        else:





def infix_to_postfix(input_str):
    """Converts an infix expression to an equivalent postfix expression"""

    """Input argument:  a string containing an infix expression where tokens are 
    space separated.  Tokens are either operators + - * / ^ parentheses ( ) or numbers
    Returns a String containing a postfix expression """
    op_stack = Stack()
    output_list = []
    ops = ['+', '-', '*', '/', '^']
    
    for num in input_str:
        if num not in ops:
            output_list.append(num)
        if num == "(":
            op_stack.push(num)
        if num == ")":
            for n in op_stack[-1]:
                if n == "("
                    op_stack.remove(n)
                    break
                else:
                    output_list.append(n)
        if num in ops:

            num.push(op_stack)
            pop(op_stack)


def prefix_to_postfix(input_str):
    """Converts a prefix expression to an equivalent postfix expression"""
    """Input argument: a string containing a prefix expression where tokens are 
    space separated.  Tokens are either operators + - * / ^ parentheses ( ) or numbers
    Returns a String containing a postfix expression(tokens are space separated)"""
    input_str = list(input_str)
    counter = 0
    new_list = []
    for num in input_str:
        if num == " ":
            input_str.remove(num)
    for num in input_str[:2]:
        new_list.append(num)
        counter += 1
    for num in input_str[2:]:
        if num == '+' or num == '-' or num == '*' or num == '/' or num == '^':
            input_str.insert(counter - 1, num)
        else:
            new_list.append(num)
            counter += 1


