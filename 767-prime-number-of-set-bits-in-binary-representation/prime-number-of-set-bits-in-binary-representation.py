class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        def prime_list(n):
            global li
            i = 0
            while 2**i <= n:
                i += 1
            
            li = [i for i in range(2, i+1)]
            for i in range(len(li) // 2):
                if li[i] != -1:
                    n = li[i] + i
                    while n < len(li):
                        li[n] = -1
                        n += li[i]
            
            li = set(li)
            #print(li)
            return

        def is_prime(n):
            global li
            return n in li


        li = []
        prime_list(right)

        r = 0
        for i in range(left, right + 1):
            n = sum(map(int, bin(i)[2:]))
            r += is_prime(n)
        
        return r
