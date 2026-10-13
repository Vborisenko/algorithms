class Solution:
    def calculate(self, s: str) -> int:
        """
        3-4*5+4/2+6*7/5-2*(-3)

        1) Stack should collect last found number from the string.
        2) Operations "+" and "-" is a signal to add current number to the stack
        3) Operations "/" and "*" should evaluate last number in stack and next number.
        4) Each operation is a signal to push element to the stack
        """
        calculator_stack = list()
        last_operation = ""
        operations = "+-*/"
        current_number = ""

        for ch in s:
            if ch in operations:
                if calculator_stack:
                    if last_operation == "/":
                        current_number = calculator_stack.pop() / int(current_number)
                    elif last_operation == "*":
                        current_number = calculator_stack.pop() * int(current_number)
                    elif last_operation == "-":
                        current_number = -int(current_number)
                last_operation = ch
                calculator_stack.append(int(current_number))
                current_number = ""
            else:
                current_number += ch

        if last_operation == "/":
            current_number = calculator_stack.pop() / int(current_number)
        elif last_operation == "*":
            current_number = calculator_stack.pop() * int(current_number)
        elif last_operation == "-":
            current_number = -int(current_number)

        calculator_stack.append(int(current_number))
        return sum(calculator_stack)