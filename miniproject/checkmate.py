def checkmate(board):
    try:
        grid = [row for row in board.split("\n") if row]
        n = len(grid)

        if n == 0 or any(len(row) != n for row in grid):
            print("Error")
            return

        pieces = {"P", "Q", "K", "B", "R"}

        kings = []
        for i in range(n):
            for j in range(n):
                if grid[i][j] == "K":
                    kings.append((i, j))

        if len(kings) != 1:
            print("Error")
            return

        kx, ky = kings[0]

        def inside(x, y):
            return 0 <= x < n and 0 <= y < n

        # ✅ Pawn (reversed rule: pawn below king)
        for dx, dy in [(1, -1), (1, 1)]:
            x, y = kx + dx, ky + dy
            if inside(x, y) and grid[x][y] == "P":
                print("Success")
                return

        # ✅ Rook + Queen (straight) — FIXED
        for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
            x, y = kx + dx, ky + dy
            while inside(x, y):
                if grid[x][y] in pieces:
                    if grid[x][y] in ("R", "Q"):
                        print("Success")
                        return
                    break
                x += dx
                y += dy

        # ✅ Bishop + Queen (diagonal) — FIXED
        for dx, dy in [(1,1), (1,-1), (-1,1), (-1,-1)]:
            x, y = kx + dx, ky + dy
            while inside(x, y):
                if grid[x][y] in pieces:
                    if grid[x][y] in ("B", "Q"):
                        print("Success")
                        return
                    break
                x += dx
                y += dy

        print("Fail")

    except:
        print("Error")