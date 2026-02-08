class Solution:
    def intToRoman(self, num: int) -> str:
        s=''
        s+='M'*(num//1000)
        r = num%1000
        if r>899:
            s += 'CM'
            r-=900
        elif r>499:
            s+='D'
            r-=500
        elif r>399:
            s+='CD'
            r-=400

        s+='C'*(r//100)
        r%=100
        if r>89:
            s += 'XC'
            r-=90
        elif r>49:
            s+='L'
            r-=50
        elif r>39:
            s+='XL'
            r-=40
            
        s+='X'*(r//10)
        r%=10
        if r>8:
            s += 'IX'
            r-=9
        elif r>4:
            s+='V'
            r-=5
        elif r>3:
            s+='IV'
            r-=4

        s+='I'*r

        return s
