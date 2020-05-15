# You are given a list of numbers, and a target number k.
#Return whether or not there are two numbers in the list that add up to k.

# Example:
# Given [4, 7, 1 , -3, 2] and k = 5,
# return true since 4 + 1 = 5.
#Try to do it in a single pass of the list. - > iterative through list only once



# naive approach (two pass of the list )

def two_sum_naive(list, k):
    
    for i in list:
      for j in range(1,len(list)):
          if i+list[j] == k : 
              
              return True 
   
    return False

#Single pass approach
def two_sum_one_pass(list,k):
    
    s = set(list)
    for i in list:
        t = k-i
        if t in s:
            return True
        
    return False

a = [4, 7, 1 , -3, 2]
print (two_sum_naive(a , 5))
print (two_sum_one_pass(a , 5))
