# Given two sorted arrays having some elements in common. Find the sum of the maximum sum path to reach from the beginning of any array to the end of any of the two arrays. We can switch from one array to another array only at common elements.
# https://www.geeksforgeeks.org/remove-extra-spaces-string/
# Examples: 

# Input: ar1[] = {2, 3, 7, 10, 12}, ar2[] = {1, 5, 7, 8}
# Output: 35
# Explanation: 35 is sum of 1 + 5 + 7 + 10 + 12.
# Start from the first element of ar2 which is 1, then move to 5, then 7.  From 7 switch to ar1 (as 7 is common) and traverse 10 and 12.

#  2 3 4     7 10 12
# 1      5   78

def max_sum(ar1, ar2):
    sum1 = 0
    sum2 = 0
    answer = 0

    currentIndex = 0
    while currentIndex < len(ar1) and currentIndex < len(ar2):
        cur1 = ar1[currentIndex]
        cur2 = ar2[currentIndex]

        if cur1 == cur2:
            answer += cur1 + max(sum1, sum2)
            sum1 = 0
            sum2 = 0
        else:
            sum1 += cur1
            sum2 += cur2
        
        currentIndex += 1
    
    restArr = []
    if cur1:
        restArr = ar1
    elif cur2:
        restArr = ar2

    if len(restArr) >=1:
        for num in restArr[currentIndex - 1:]:
            answer = answer + num
    
    return answer

# should be 35
ar1 = [2, 3, 7, 10, 12]
ar2 = [1, 5, 7, 8]
print(max_sum(ar1, ar2))

def max_sum_2(ar1, ar2):
    # index of ar1
    i = 0
    # index of ar2
    j = 0
    sum1 = 0
    sum2 = 0
    answer = 0
    while len(ar1) > i and len(ar2) > j:
        cur1, cur2 = ar1[i], ar2[j]
        
        if (cur1 > cur2):
            sum2 = sum2 + cur2
            j += 1
        elif (cur2 > cur1):
            sum1 = sum1 + cur1
            i += 1
        else:
            sum1 = sum1 + cur1
            sum2 = sum2 + cur2
            answer = max(sum1, sum2)
            sam1 = 0
            sum2 = 0
            j += 1
            i += 1

    while len(ar1) > i:
        answer += ar1[i]
        i += 1
    
    while len(ar2) > j:
        answer += ar2[j]
        j += 1
        
    return answer
