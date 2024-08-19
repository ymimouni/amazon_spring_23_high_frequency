class Solution:
    def partitionString(self, s: str) -> int:
        min_sstrings = 1

        seen = set()

        for c in s:
            if c in seen:
                seen = set()
                min_sstrings += 1
            seen.add(c)

        return min_sstrings
