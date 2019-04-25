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
    ops = ['+', '-', '*', '/', '**', '>>', '<<']
    nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    num_counter = 0
    op_counter = 0
    for num in input_str:
        if num not in ops and num not in nums:
            raise PostfixFormatException("Invalid token")
        if num in nums:
            num_counter += 1
        if num in ops:
            op_counter += 1
    for num in input_str:
        if num_counter <= op_counter:
            raise PostfixFormatException("Insufficient operands")
        elif (op_counter + 1) != num_counter:
            raise PostfixFormatException("Too many operands")
        if num not in ops:
            stack.push(num)  # pushes value onto stack
        else:  # if the element is a operator, pop operands for the operator from stack.
            num2 = int(stack.pop())
            num1 = int(stack.pop())
            new = do_math(num, num1, num2)  # evaluate the operator and push the result back to the stack
            stack.push(new)
    return float(stack.pop())   # when the expression is ended, the number in the stack is the final answer


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
    elif op == '**':
        return int(num1 ** num2)
    elif op == '>>':
        if isinstance(num1, int) and isinstance(num2, int):
            return int(num1 >> num2)
        else:
            raise PostfixFormatException("Illegal bit shift operand")
    else:
        if isinstance(num1, int) and isinstance(num2, int):
            return int(num1 << num2)
        else:
            raise PostfixFormatException("Illegal bit shift operand")




def infix_to_postfix(input_str):
    """Converts an infix expression to an equivalent postfix expression"""

    """Input argument:  a string containing an infix expression where tokens are 
    space separated.  Tokens are either operators + - * / ^ parentheses ( ) or numbers
    Returns a String containing a postfix expression """
    order = {'-': 1, '+': 1, '*': 2, '/': 2, '**': 3, '>>': 4, '<<': 4}
    op_stack = Stack(30)
    output_expression = []
    ops = ['+', '-', '*', '/', '**', '>>', '<<']
    input_str = input_str.split(" ")
    for num in input_str:
        if num == "(":
            op_stack.push(num)
        elif num == ")":
            while op_stack.peek() != '(':
                output_expression.append(op_stack.pop())
            op_stack.pop()
        elif num not in ops:  # if num is a number, add it to the stack
            output_expression.append(num)
        else:
            if op_stack.size() > 0:
                n = op_stack.peek()
                if n == "(":
                    op_stack.push(num)
                elif order[num] <= order[n]:
                    k = op_stack.pop()
                    output_expression.append(k)  # remove operators on the stack; append them to the output
                    op_stack.push(num)
                else:
                    op_stack.push(num)
            else:
                op_stack.push(num)
    while op_stack.is_empty() is False:  # when the input expression has been processed, check the op_stack.
        n = op_stack.pop()
        output_expression.append(n)  # any operators still on the stack are removed and appended to output stack.
    new = ' '.join(output_expression)
    return new


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
    new = op_stack.pop()
    new = ' '.join(new)
    return new





