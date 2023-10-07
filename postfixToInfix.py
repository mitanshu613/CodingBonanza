def postfix_to_infix(postfix_expression):
    def is_operator(char):
        return char in "+-*/^"

    stack = []
    for char in postfix_expression:
        if char.isalnum():  # Operand
            stack.append(char)
        elif is_operator(char):  # Operator
            operand2 = stack.pop()
            operand1 = stack.pop()
            expression = f"({operand1}{char}{operand2})"
            stack.append(expression)

    infix_expression = stack[0]
    return infix_expression

# Example usage:
postfix_expression = "AB+CD-*"
infix_expression = postfix_to_infix(postfix_expression)
print("Postfix Expression:", postfix_expression)
print("Infix Expression:", infix_expression)
