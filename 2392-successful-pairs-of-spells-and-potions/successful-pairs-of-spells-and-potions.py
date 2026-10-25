from bisect import bisect_left
from typing import List

class Solution:
    def successfulPairs(
        self, spells: List[int], potions: List[int], success: int
    ) -> List[int]:
        potions.sort()
        m = len(potions)
        pairs = []

        for spell in spells:
            # Smallest potion strength that satisfies spell * potion >= success
            threshold = (success + spell - 1) // spell
            first_success = bisect_left(potions, threshold)
            pairs.append(m - first_success)

        return pairs