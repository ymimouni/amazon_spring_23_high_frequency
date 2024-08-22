from typing import List

from collections import deque


class Solution:
    def timeTaken(self, arrival: List[int], state: List[int]) -> List[int]:
        n = len(arrival)
        ans = [0] * n

        enter_queue, exit_queue = deque(), deque()

        prev_state = None
        curr_time = arrival[0]

        i = 0
        while i < n or enter_queue or exit_queue:
            while i < n and arrival[i] <= curr_time:
                if state[i] == 0:
                    enter_queue.append(i)
                else:
                    exit_queue.append(i)
                i += 1

            if not enter_queue and not exit_queue:
                curr_time = arrival[i]
                prev_state = None
                continue

            if prev_state == 0:
                if enter_queue:
                    idx = enter_queue.popleft()
                    ans[idx] = curr_time
                    curr_time += 1
                    prev_state = 0
                elif exit_queue:
                    idx = exit_queue.popleft()
                    ans[idx] = curr_time
                    curr_time += 1
                    prev_state = 1
            else:
                if exit_queue:
                    idx = exit_queue.popleft()
                    ans[idx] = curr_time
                    curr_time += 1
                    prev_state = 1
                elif enter_queue:
                    idx = enter_queue.popleft()
                    ans[idx] = curr_time
                    curr_time += 1
                    prev_state = 0

        return ans
