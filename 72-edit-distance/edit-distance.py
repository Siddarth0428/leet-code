class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # Convert an empty word to word2's prefixes using insertions.
        dp = list(range(len(word2) + 1))

        for i, char1 in enumerate(word1, start=1):
            diagonal = dp[0]  # Previous row's dp[j - 1]
            dp[0] = i         # Delete i characters to reach an empty word

            for j, char2 in enumerate(word2, start=1):
                above = dp[j]  # Previous row's dp[j]

                if char1 == char2:
                    dp[j] = diagonal
                else:
                    dp[j] = 1 + min(
                        dp[j - 1],  # Insert
                        above,      # Delete
                        diagonal,   # Replace
                    )

                diagonal = above

        return dp[-1]