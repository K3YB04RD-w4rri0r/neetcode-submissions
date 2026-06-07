class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for l in s:
            print(stack)
            if stack != []:
                last_elem = stack[-1]

                if l == "}" and last_elem == "{":
                    stack.pop()

                elif l == "]" and last_elem == "[":
                    stack.pop()


                elif l == ")" and last_elem == "(":
                    stack.pop()

                else:
                    stack.append(l)
            else:
                stack.append(l)

        return len(stack) == 0
