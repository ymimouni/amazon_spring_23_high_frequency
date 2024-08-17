from math import floor, sqrt


class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        for i in range(1, floor(sqrt(n)) + 1):
            if n % i == 0:
                if k == 1:
                    return i
                k -= 1

        if floor(sqrt(n)) ** 2 == n:
            i -= 1

        for j in range(i, 0, -1):
            if n % j == 0:
                if k == 1:
                    return n // j
                k -= 1

        return -1


# class Solution:
#     def kthFactor(self, n: int, k: int) -> int:
#         for i in range(1, n + 1):
#             if n % i == 0:
#                 if k == 1:
#                     return i
#                 else:
#                     k -= 1
#         return -1
