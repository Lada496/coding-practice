#User function Template for python3
# I II III IV V VI VII VIII IX X XI XII XIII XIV XV XVI
class Solution:
    def romanToDecimal(self, s):
        # code here
        r_to_d = {
            "I":1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        
        if len(s) == 1:
            return r_to_d[s[0]]
        
            # check 4
        if r_to_d[s[0]] < r_to_d[s[1]]:
            return (r_to_d[s[1]] - r_to_d[s[0]]) + self.romanToDecimal(s[2:]) if len(s) > 2 else (r_to_d[s[1]] - r_to_d[s[0]])
        else:
            return r_to_d[s[0]] + self.romanToDecimal(s[1:])