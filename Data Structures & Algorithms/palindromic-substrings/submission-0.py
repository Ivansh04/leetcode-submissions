class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)

        # -1 = uncomputed, True/False = computed result
        memo = [[None] * n for _ in range(n)]

        def is_palindrome(i, j):
            if i >= j:
                return True

            if memo[i][j] is not None:
                return memo[i][j]

            if s[i] != s[j]:
                memo[i][j] = False
            else:
                memo[i][j] = is_palindrome(i + 1, j - 1)

            return memo[i][j]

        cnt=0

        for i in range(n):
            for j in range(i, n):
                if is_palindrome(i, j):
                    cnt+=1
                    

        return cnt