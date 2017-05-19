
"""
关键是找出循环节，使用map记录除数，当除数重复出现时，循环节出现
"""
class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        sign = '-' if numerator*denominator < 0 else ''
        numerator,denominator = abs(numerator),abs(denominator)
        part1 = numerator / denominator
        numerator = numerator - part1*denominator
        if numerator == 0:return sign+str(part1)
        part2 = {}
        subres = ""
        i=0
        while numerator!=0 and numerator not in part2:
            part2[numerator] = i
            i+=1
            numerator*=10
            subres+=str(numerator/denominator)
            numerator%=denominator
        if numerator!=0:
            i = part2[numerator]
            subres = subres[:i]+'('+subres[i:]+')'
        res = str(part1)+'.'+subres
        return sign+res
