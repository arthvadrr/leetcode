# https://leetcode.com/problems/longest-valid-parentheses/submissions/

class Solution(object):
    def longestValidParentheses(self, s):
        stack = [-1]
        longest = 0

        for i, char in enumerate(s):
            if char == "(":
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    longest = max(longest, i - stack[-1])

        return longest