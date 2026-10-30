class Fenwick:
    def __init__(self, n):
        self.n = n
        self.bit = [0] * (n + 1)

    def add(self, i, value):
        while i <= self.n:
            self.bit[i] ^= value
            i += i & -i

    def query(self, i):
        result = 0
        while i:
            result ^= self.bit[i]
            i -= i & -i
        return result


class Solution:
    def palindromePath(self, n, edges, s, queries):
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        # Iterative DFS computes Euler tour intervals, parents, and depths.
        tin = [0] * n
        tout = [0] * n
        parent = [-1] * n
        depth = [0] * n
        timer = 0
        stack = [(0, -1, False)]

        while stack:
            u, p, exiting = stack.pop()
            if exiting:
                tout[u] = timer
                continue

            parent[u] = p
            tin[u] = timer
            timer += 1

            stack.append((u, p, True))
            for v in graph[u]:
                if v != p:
                    depth[v] = depth[u] + 1
                    stack.append((v, u, False))

        # Binary lifting for lowest common ancestor queries.
        log = n.bit_length()
        up = [[0] * n for _ in range(log)]

        for u in range(n):
            up[0][u] = u if parent[u] == -1 else parent[u]

        for k in range(1, log):
            for u in range(n):
                up[k][u] = up[k - 1][up[k - 1][u]]

        def lca(a, b):
            if depth[a] < depth[b]:
                a, b = b, a

            diff = depth[a] - depth[b]
            for k in range(log):
                if diff >> k & 1:
                    a = up[k][a]

            if a == b:
                return a

            for k in range(log - 1, -1, -1):
                if up[k][a] != up[k][b]:
                    a = up[k][a]
                    b = up[k][b]

            return parent[a]

        fenwick = Fenwick(n)

        # Range-XOR updates make each node's letter affect root paths
        # ending inside that node's subtree.
        for u in range(n):
            mask = 1 << (ord(s[u]) - ord('a'))
            fenwick.add(tin[u] + 1, mask)
            if tout[u] < n:
                fenwick.add(tout[u] + 1, mask)

        def root_parity(u):
            return fenwick.query(tin[u] + 1)

        letters = list(s)
        answer = []

        for query in queries:
            parts = query.split()

            if parts[0] == "update":
                u = int(parts[1])
                c = parts[2]

                delta = (1 << (ord(letters[u]) - ord('a'))) ^ (
                    1 << (ord(c) - ord('a'))
                )
                if delta:
                    fenwick.add(tin[u] + 1, delta)
                    if tout[u] < n:
                        fenwick.add(tout[u] + 1, delta)
                    letters[u] = c
            else:
                u, v = int(parts[1]), int(parts[2])
                ancestor = lca(u, v)
                parity = (
                    root_parity(u)
                    ^ root_parity(v)
                    ^ (1 << (ord(letters[ancestor]) - ord('a')))
                )
                answer.append((parity & (parity - 1)) == 0)

        return answer
        