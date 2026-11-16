class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s) > k:
            parts = []
            for i in range(0, len(s), k):
                digit_sum = sum(int(digit) for digit in s[i:i + k])
                parts.append(str(digit_sum))
            s = "".join(parts)
        return s