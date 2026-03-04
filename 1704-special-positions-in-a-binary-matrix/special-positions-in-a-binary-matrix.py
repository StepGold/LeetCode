class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        res = 0
        li = []
        for i in range(len(mat)):
            if sum(mat[i]) == 1:
                li.append(i)
        print(li)
        for i in range(len(mat[0])):
            cur = -1
            summ = 0
            for j in range(len(mat)):
                if mat[j][i]:
                    if cur != -1:
                        summ = 2
                        break
                    else:
                        summ = 1
                        cur = j
            if summ == 1:
                if cur in li:
                    res += 1
        
        return res