#You are given two linked-lists representing two non-negative integers. 
#The digits are stored in reverse order and each of their nodes contain a single digit. 
#Add the two numbers and return it as a linked list.

# Definition for singly-linked list.
#Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
#Output: 7 -> 0 -> 8
#Explanation: 342 + 465 = 807.
class ListNode(object):
  def __init__(self, x):
    self.val = x
    self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2, c = 0):
        head = 0
        while l1!=None and l2!=None:
            if c != 0:
                s = c + l1.val + l2.val
                
            else:
                s = l1.val + l2.val
                
            
            if len(str(s))>1:
                c = int(str(s)[0])
                s = int(str(s)[1::])

            if head == 0:
                res= ListNode(s)
                head = res
            else:
                res.next = ListNode(s)
                res = res.next

            l1 = l1.next
            l2 = l2.next
            

        return head
            
        
            

       
if __name__ == '__main__':
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)

    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)

    result = Solution().addTwoNumbers(l1, l2)
    while result:
        print(result.val)
        result = result.next