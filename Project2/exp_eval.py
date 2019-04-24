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
        if num not in ops:
            stack = stack.push(num)  # pushes value onto stack
        else:  # if the element is a operator, pop operands for the operator from stack.
            num1 = stack.pop()
            num2 = stack.pop()
            new = do_math(num, num1, num2)  # evaluate the operator and push the result back to the stack
        stack.push(new)
    if size(stack) > 1:
        raise PostfixFormatException
    return stack   # when the expression is ended, the number in the stack is the final answer


def do_math(op, num1, num2):
    if op == "+":
        return num1 + num2
    elif op == "-":
        return num1 - num2
    elif op == "*":
        return num1 * num2
    elif op == "/":
        return num1 / num2
    else:
        return num1 ** num2


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
        if num not in ops: #if num is a number, add it to the stack
            output_expression.append(num)
        if num == "(":
            op_stack.push(num)
        if num == ")":
            while peek(op_stack) != '(' or len(op_stack) == 0:
                output_expression.append(op_stack.pop())
            op_stack.pop()
        if num in ops:
            for op in op_stack[-1]:
                while num in order >= op in op_stack:
                    output_expression.append(op_stack.pop())  # remove operators on the stack; append them to the output stack.
            output_expression.append(num)
        return output_expression

        # when the input expression has been completely processed, check the op_stack.
        # any operators still on the stack can be removed and appended to the end of the output stack.


def prefix_to_postfix(input_str):
    """Converts a prefix expression to an equivalent postfix expression"""
    """Input argument: a string containing a prefix expression where tokens are 
    space separated.  Tokens are either operators + - * / ^ parentheses ( ) or numbers
    Returns a String containing a postfix expression(tokens are space separated)"""
    input_str = input_str.split(" ")
    op_stack = Stack(30)
    output_expression = []
    ops = ['+', '-', '*', '/', '**']
    for num in input_str[-1]:
        if num not in ops: # if num is a number, add it to the stack
            output_expression.append(num)
        if num in ops:
            op1 = op_stack.pop()
            op2 = op_stack.pop()
            output_expression.append(op1 + op2 + num)
            stack.push(output_expression)
        return output_expression




