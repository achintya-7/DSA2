class Solution:
    def answer(self, s: str):
        l = 0
        r = len(str) - 1

        while l <= r:
            while l < r and not s[l].isalnum:
                l += 1

            while l < r and not s[r].isalnum:
                r -= 1

            if s[l] != s[r]:
                return False

            l, r = l + 1, r - 1

        return True
                


