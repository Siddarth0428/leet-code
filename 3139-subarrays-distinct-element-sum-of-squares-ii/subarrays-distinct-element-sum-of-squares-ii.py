class Solution:
    def sumCounts(self, nums: list[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)

        total = [0] * (4 * n)
        squares = [0] * (4 * n)
        lazy = [0] * (4 * n)
        last = {}

        def apply(node: int, left: int, right: int, delta: int) -> None:
            length = right - left + 1
            old_sum = total[node]
            squares[node] = (
                squares[node] + 2 * delta * old_sum + delta * delta * length
            ) % MOD
            total[node] = (old_sum + delta * length) % MOD
            lazy[node] += delta

        def push(node: int, left: int, right: int) -> None:
            if lazy[node] == 0 or left == right:
                return
            mid = (left + right) // 2
            apply(node * 2, left, mid, lazy[node])
            apply(node * 2 + 1, mid + 1, right, lazy[node])
            lazy[node] = 0

        def add(node: int, left: int, right: int, ql: int, qr: int) -> None:
            if ql <= left and right <= qr:
                apply(node, left, right, 1)
                return

            push(node, left, right)
            mid = (left + right) // 2
            if ql <= mid:
                add(node * 2, left, mid, ql, qr)
            if qr > mid:
                add(node * 2 + 1, mid + 1, right, ql, qr)

            total[node] = (total[node * 2] + total[node * 2 + 1]) % MOD
            squares[node] = (squares[node * 2] + squares[node * 2 + 1]) % MOD

        answer = 0
        for r, value in enumerate(nums):
            left = last.get(value, -1) + 1
            add(1, 0, n - 1, left, r)
            last[value] = r
            answer = (answer + squares[1]) % MOD

        return answer