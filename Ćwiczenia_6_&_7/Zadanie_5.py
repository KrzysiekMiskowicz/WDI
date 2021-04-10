def knight(board, r, c, moves, nr):
        dim = len(board)
        if r < 0 or r >= dim or c < 0 or c >= dim or board[r][c]:
            return
        board[r][c] = True
        moves[r][c] = nr
        if nr == dim*dim:
            for i in range(dim):
                for j in range(dim):
                    print("%3d" % moves[i][j], end=" ")
                print()
            print()
            #trzeba chyba false pole
            board[r][c] = False
            return

        jumps = ((-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1))
        for i in jumps:
            knight(board, r+i[0], c+i[1], moves, nr+1)

        board[r][c] = False


board = [[False for _ in range(5)] for _ in range(5)]
moves = [[0 for _ in range(5)] for _ in range(5)]
knight(board, 0, 0, moves, 1)

