class Solution(object):
    def champagneTower(self, p, row, col):
        li = [[0] * n for n in range(1, row+3)]
        li[0][0] = p
        for i in range(row+1):
            for j in range(i + 1):
                a = li[i][j]
                if a > 1:
                    li[i][j] = 1
                    a = (a - 1) / 2
                    li[i+1][j] += a
                    li[i+1][j+1] += a
        
        return li[row][col]
                
        