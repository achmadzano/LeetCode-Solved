class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        def evaluate_expression(tokens):
            stack = []
            sign = 1
            result = 0

            for token in tokens:
                if token.isdigit():
                    result += sign * int(token)
                elif token == '+':
                    sign = 1
                elif token == '-':
                    sign = -1
                elif token == '(':
                    stack.append(result)
                    stack.append(sign)
                    result = 0
                    sign = 1
                elif token == ')':
                    result *= stack.pop()
                    result += stack.pop()

            return result

        # Removing white spaces from the expression
        s = s.replace(" ", "")

        # Tokenizing the expression
        tokens = []
        i = 0
        while i < len(s):
            if s[i].isdigit():
                j = i
                while j < len(s) and s[j].isdigit():
                    j += 1
                tokens.append(s[i:j])
                i = j
            else:
                tokens.append(s[i])
                i += 1

        return evaluate_expression(tokens)