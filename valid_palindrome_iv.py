class Solution:
    def makePalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        changes = 0

        while left < right:
            if s[left] != s[right]:
                changes += 1
                if changes > 2:
                    return False

            left += 1
            right -= 1

        return True
