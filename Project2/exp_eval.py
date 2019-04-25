#
#Kelsey Deuth
#
#04/23/19
#
#Project2
#Section 11
#this code solves prexif, infix, and postfix expressions using stack arrays

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
    stack = Stack(30)
    ops = ['+', '-', '*', '/', '**']
    for num in input_str:
        if len(input_str) <= 2 and (num in ops or num in '0123456789'):
            raise PostfixFormatException("Insufficient operands")
        if num not in ops and not '0123456789':
            raise PostfixFormatException("Invalid token")
        if num not in ops:
            stack.push(num)  # pushes value onto stack
        else:  # if the element is a operator, pop operands for the operator from stack.
            num2 = int(stack.pop())
            num1 = int(stack.pop())
            new = do_math(num, num1, num2)  # evaluate the operator and push the result back to the stack
            stack.push(new)
    if stack.size() > 1:
        if stack.peek() in ops:
            raise PostfixFormatException("Insufficient operands")
        else:
            raise PostfixFormatException("Too many operands")
    return stack.pop()   # when the expression is ended, the number in the stack is the final answer


def do_math(op, num1, num2):
    if op == "+":
        return int(num1 + num2)
    elif op == "-":
        return int(num1 - num2)
    elif op == "*":
        return int(num1 * num2)
    elif op == "/":
        if num2 == 0:
            raise ValueError
        return int(num1 / num2)
    else:
        return int(num1 ** num2)


def infix_to_postfix(input_str):
    """Converts an infix expression to an equivalent postfix expression"""

    """Input argument:  a string containing an infix expression where tokens are 
    space separated.  Tokens are either operators + - * / ^ parentheses ( ) or numbers
    Returns a String containing a postfix expression """
    order = {'-': 1, '+': 1, '*': 2, '/': 2, '**': 3}
    op_stack = Stack(30)
    output_expression = []
    ops = ['+', '-', '*', '/', '**']
    input_str = input_str.split(" ")
    for num in input_str:
        if num not in ops:  # if num is a number, add it to the stack
            output_expression.append(num)
        if num == "(":
            op_stack.push(num)
        if num == ")":
            while op_stack.peek() != '(' or op_stack.size() == 0:
                output_expression.append(op_stack.pop())
            op_stack.pop()
        if num in ops:
            while op_stack.size() > 0 and order[num] >= op_stack.peek():
                output_expression.append(op_stack.pop())  # remove operators on the stack; append them to the output
            op_stack.push(num)
    while op_stack.is_empty() is not True:  # when the input expression has been processed, check the op_stack.
        n = op_stack.pop()
        output_expression.append(n)  # any operators still on the stack are removed and appended to output stack.
    new = ' '.join(output_expression)
    return new


# infix_to_postfix('3 + 4 * 2 / (1 - 5) ** 2 **3')


def prefix_to_postfix(input_str):
    """Converts a prefix expression to an equivalent postfix expression"""
    """Input argument: a string containing a prefix expression where tokens are 
    space separated.  Tokens are either operators + - * / ^ parentheses ( ) or numbers
    Returns a String containing a postfix expression(tokens are space separated)"""
    input_str = input_str.split(" ")
    op_stack = Stack(30)
    ops = ['+', '-', '*', '/', '**']
    for num in input_str[::-1]:
        if num not in ops:  # if num is a number, add it to the stack
            op_stack.push(num)
        else:
            op1 = op_stack.pop()
            op2 = op_stack.pop()
            n = op1 + op2 + num
            op_stack.push(n)
        return op_stack.pop()


print(prefix_to_postfix('* - 3 / 2 1 - / 4 5 6'))




