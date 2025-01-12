
class Solution:
    def convertRoman(self, n):
        #Code here
        romanMap = {
            1:"I",
            4:"IV",
            5: "V",
            9:"IX",
            10: "X",
            40:"XL",
            50: "L",
            90:"XC",
            100: "C",
            400:"CD",
            500: "D",
            900:"CM",
            1000: "M",
            }
        
        if n in romanMap:
            return romanMap[n]
        
        ans = ''
        
        while n > 0:
            largest = 0
            if n >= 1000:
                largest = 1000
            elif n >= 900:
                largest = 900
            elif n >= 500:
                largest = 500
            elif n >= 400:
                largest = 400
            elif n >= 100:
                largest = 100
            elif n >= 90:
                largest = 90
            elif n >= 50:
                largest = 50
            elif n >= 40:
                largest = 40
            elif n >= 10:
                largest = 10
            elif n >= 9:
                largest = 9
            elif n >= 5:
                largest = 5
            elif n >= 4:
                largest = 4
            elif n >= 1:
                largest = 1
            
            n -= largest
            ans += romanMap[largest]
        
        return ans