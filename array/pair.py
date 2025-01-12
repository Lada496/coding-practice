# Examples: 

# Input: arr[] = [0, -1, 2, -3, 1], target = -2
# Output: true
# Explanation: There is a pair (1, -3) with the sum equal to given target, 1 + (-3) = -2.


# Input: arr[] = [1, -2, 1, 0, 5], target = 0
# Output: false
# Explanation: There is no pair with sum equals to given target.

# [-3, -1, 0, 1, 2]


#Function to perform binary search
    # static boolean binarySearch(int[] arr, int left,
    #                             int right, int target){
    #     while (left <= right) {
    #         int mid = left + (right - left) / 2;

    #         if (arr[mid] == target)
    #             return true;
    #         if (arr[mid] < target)
    #             left = mid + 1;
    #         else
    #             right = mid - 1;
    #     }
    #     return false;
    # }


def pair(arr, target):
    sorted = arr.sort()
    i = 0
    for i in range(len(arr)):
        complement = target - arr[i]
        start = i + 1 # left
        end = len(arr) - 1 # right
        middle = (end + start) // 2
        while start < end:
            if arr[middle] < target:
                end = middle
            elif arr[middle] > target:
                start = middle
            # when we find the pair
            else:
                return True
    return False


pair([0, -1, 2, -3, 1], -2)

# sort
# get compliment
# search it with binary search
# O(nlogn)
# [-3, -1, 0, 1, 2]
#{1: -3, -1: -1, -2: 0, -3: 1, -4: 2}
def pair(arr, target):
    complementMap = {}
    for n in arr:
        complement = target - n
        complementMap[complement] = n
    
    for n in arr:
        if n in complementMap:
            return True
    
    return False