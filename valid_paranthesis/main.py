class Solution:
    def isValid(self, s):
        stack = []
        bracket_pairs = {')': '(', ']': '[', '}': '{', '>':'<'}

        for ch in s:
            if ch in bracket_pairs.values():
                stack.append(ch)
            else:
                if not stack or stack[-1] != bracket_pairs[ch]:
                    return False
                stack.pop()

        return not stack