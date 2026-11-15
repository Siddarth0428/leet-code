from typing import List

class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        mod = 10**9 + 7
        even_prefixes = 1  # Includes the empty prefix
        odd_prefixes = 0
        prefix_parity = 0
        count = 0

        for value in arr:
            prefix_parity ^= value & 1

            if prefix_parity == 0:
                count += odd_prefixes
                even_prefixes += 1
            else:
                count += even_prefixes
                odd_prefixes += 1

        return count % mod