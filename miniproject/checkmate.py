def checkmate(board: str):
    try:
        print(board)  # แสดงกระดานที่รับเข้ามา
        # แปลงกระดานจาก string เป็น list ของแถว
        grid = [row for row in board.split("\n") if row]
        # ขนาดของกระดาน (ต้องเป็น NxN)
        n = len(grid)
        # ตรวจสอบว่ากระดานเป็นสี่เหลี่ยมจัตุรัสหรือไม่
        if n == 0 or any(len(row) != n for row in grid):
            print("Error")
            return
        # กำหนดตัวหมากที่ใช้งานในเกม
        pieces = {"P", "Q", "K", "B", "R"}
        # ค้นหาตำแหน่งของ King ทั้งหมดในกระดาน
        kings = []
        for i in range(n):
            for j in range(n):
                if grid[i][j] == "K":
                    kings.append((i, j))
        # ต้องมี King เพียงตัวเดียว
        if len(kings) != 1:
            print("Error")
            return
        # ตำแหน่งของ King
        kx, ky = kings[0]
        # ฟังก์ชันตรวจสอบว่าอยู่ในขอบกระดานหรือไม่
        def inside(x, y):
            return 0 <= x < n and 0 <= y < n
        # ----------------------------
        # ตรวจ Pawn (กฎ: อยู่ใต้ King และโจมตีเฉียงขึ้น)
        # ----------------------------
        for dx, dy in [(1, -1), (1, 1)]:
            x, y = kx + dx, ky + dy
            if inside(x, y) and grid[x][y] == "P":
                print("Success")
                return
        # ----------------------------
        # ตรวจ Rook และ Queen (แนวตรง)
        # ----------------------------
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            x, y = kx + dx, ky + dy
            # เดินไปตามแนวเส้นตรงทีละช่อง
            while inside(x, y):
                # ถ้าเจอหมากตัวแรกในเส้นทาง
                if grid[x][y] in pieces:
                    # ถ้าเป็น Rook หรือ Queen แสดงว่าโจมตีได้
                    if grid[x][y] in ("R", "Q"):
                        print("Success")
                        return
                    # ถ้าไม่ใช่ แปลว่าถูกบล็อก
                    break
                x += dx
                y += dy
        # ----------------------------
        # ตรวจ Bishop และ Queen (แนวทแยง)
        # ----------------------------
        for dx, dy in [(1, 1), (1, -1), (-1, 1), (-1, -1)]:
            x, y = kx + dx, ky + dy
            # เดินไปตามแนวทแยงทีละช่อง
            while inside(x, y):
                # ถ้าเจอหมากตัวแรกในเส้นทาง
                if grid[x][y] in pieces:
                    # ถ้าเป็น Bishop หรือ Queen แสดงว่าโจมตีได้
                    if grid[x][y] in ("B", "Q"):
                        print("Success")
                        return
                    # ถ้าถูกบล็อก
                    break
                x += dx
                y += dy

        # ถ้าไม่มีใครโจมตี King ได้
        print("Fail")
    except:
        # กรณีข้อมูลผิดหรือ error ใด ๆ
        print("Error")
