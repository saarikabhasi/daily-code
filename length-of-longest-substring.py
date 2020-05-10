#Given a string, find the length of the longest substring without repeating characters.
#string:abrkaabcdefghijjxxx 
#answer:10

class Solution:
  def lengthOfLongestSubstring(self, s):
    a = 26 *[0]
    c =0
    max=0
    for i in s:
        a[ord(i) - ord('a')]+=1
        if a[ord(i) - ord('a')]>1:
            if max <c:
                max=c
                c=0
                a=26*[0]


        else:
            c+=1

    if max<c:
        max =c

    
    return max

if __name__ == '__main__':
    print (Solution().lengthOfLongestSubstring('tracecars'))


