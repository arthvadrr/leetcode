class Solution(object):
    def isSubsequence(self, s, t):
        string_index = 0

        if len(s) < 1:
            return True

        for i in range(len(t)):

            if s[string_index] == t[i]:
                string_index += 1

                if string_index >= len(s):
                    return True

                if string_index >= len(t):
                    return False

        return False
