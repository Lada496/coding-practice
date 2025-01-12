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
        
        
        # 2 or 3
        j = 1
        count = 1
        should_count = s[0] == s[1]
        while j < len(s) and should_count:
            if s[0] == s[j]:
                count += 1
            else:
                should_count = False
            j += 1
        
        if count == 1:
            # check 4
            if ((s[0] == "I" and s[1] == "V") or (s[0] == "I" and s[1] == "X") or
                (s[0] == "X" and s[1] == "L") or (s[0] == "X" and s[1] == "C") or
                (s[0] == "C" and s[1] == "D") or (s[0] == "C" and s[1] == "M")):
                return (r_to_d[s[1]] - r_to_d[s[0]]) + self.romanToDecimal(s[2:]) if len(s) > 2 else (r_to_d[s[1]] - r_to_d[s[0]])
            return r_to_d[s[0]] + self.romanToDecimal(s[1:]) if len(s) >= 2 else r_to_d[s[0]]
        else:
            if len(s) <= count:
                return count * r_to_d[s[0]]
            return count * r_to_d[s[0]] + self.romanToDecimal(s[count:])