# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/submissions/

import re

class Solution(object):
    def strStr(self, haystack, needle):
        reggie = re.search(needle, haystack)

        if reggie:
            return reggie.start()

        return -1

 
