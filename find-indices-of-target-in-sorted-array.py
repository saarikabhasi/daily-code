# Given a sorted array, A, with possibly duplicated elements, find the indices of the first and last occurrences of a target element, x. Return -1 if the target is not found.

# Example:
# Input: A = [1,3,3,5,7,8,9,9,9,15], target = 9
# Output: [6,8]

# Input: A = [100, 150, 150, 153], target = 150
# Output: [1,2]

# Input: A = [1,2,3,4,5,6,10], target = 9
# Output: [-1, -1]

class Solution: 
  def getRange(self, arr, target):
    p = len(arr)//2
    mn = 0
    mx = 0
    l=[]
    pivot = arr[p]
    if pivot >target: 
        for i in range(0,p):
            if arr[i] == target:
                l.append(i)
    elif pivot<target:
        for i in range(p,len(arr)):
            if arr[i]==target:
                l.append(i)
    else:
        for i in range(0,len(arr)):
            if arr[i]==target:
                l.append(i)
        
    if len(l)==0:
        return [-1,-1]
    else:
        return [min(l),max(l)]
    
# Test program 
if __name__ == '__main__':
    arr = [150, 150, 150, 150,153]
    x = 153
    print(Solution().getRange(arr, x))
# [1, 4]