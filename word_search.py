def exist(board: list[list[str]], word:str) -> bool:
    rows, cols = len(board), len(board[0])

    def dfs(r:int, c:int, index: int, visited: set) -> bool:
        if index == len(word):
            return True

        if (r < 0 or r >=rows or c < 0 or c >= cols or
            board[r][c] != word[index] or (r, c) in visited):
            return False

        visited.add((r, c))

        found = (dfs( r + 1,c, index + 1, visited) or
                 dfs(r - 1, c, index + 1, visited) or
                 dfs(r, c + 1, index + 1, visited) or
                 dfs(r, c - 1, index + 1, visited))

        visited.remove((r, c))

        return found

    for i in range(rows):
        for j in range(cols):
            if dfs(i, j, 0, set()):
                return True

    return False