class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        def calculate(a, b, operation) -> int:
            if operation == "+":
                return a + b
            elif operation == "-":
                return a - b
            elif operation == "*":
                return a * b
            elif operation == "/":
                return int(a / b)

        stack = []
        operations = ("+", "-", "/", "*")

        for current_token in tokens:
            if current_token in operations:
                b, a = int(stack.pop()), int(stack.pop())
                stack.append(calculate(a, b, current_token))
                continue
            stack.append(current_token)

        return int(stack[-1])
