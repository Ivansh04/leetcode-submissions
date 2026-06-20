class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        q = deque()
        minu=-1
        ff=0

        def addCell(r, c):
            nonlocal ff
            if (min(r, c) < 0 or r == ROWS or c == COLS or
                (r, c) in visit or grid[r][c] == 0
            ):
                return
            visit.add((r, c))
            ff-=1
            q.append([r, c])

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    ff+=1
                if grid[r][c] == 2:
                    q.append([r, c])
                    visit.add((r, c))
        if not q and ff==0:
            return 0

        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                addCell(r + 1, c)
                addCell(r - 1, c)
                addCell(r, c + 1)
                addCell(r, c - 1)
            minu += 1
        return minu if ff==0 else -1
        