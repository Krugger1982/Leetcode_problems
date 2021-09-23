# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

##  k == lists.length
##  0 <= k <= 10^4
##  0 <= lists[i].length <= 500
##  -10^4 <= lists[i][j] <= 10^4
##  lists[i] is sorted in ascending order.
##  The sum of lists[i].length won't exceed 10^4.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
         

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        
        totalArray = []
        for i in lists:
            j = i
            while(j != None):
                totalArray.append(j.val)
                j = j.next
        if len(totalArray) == 0:
            return None
        
        res = sorted(totalArray)
       
        start = ListNode()
        start.val = res[0]
        start.next = None
        strt = start 
        for i in res[1:]:
            new_node = ListNode()
            new_node.val = i
            new_node.next = None
            strt.next = new_node
            strt = strt.next
       
        return start           

        
        



import unittest
        
class Tests_Solution(unittest.TestCase):
        
    def test_1_merge_K_Lists(self):
        enter1 = []
        enter2 = []
        enter3 = [2, 6]
        head1 = ListNode(enter1[0]) if enter1 else None
        head2 = ListNode(enter2[0]) if enter2 else None
        head3 = ListNode(enter3[0]) if enter3 else None
        # Создаем первый LinkedList
        current = head1
        for element in enter1[1:]:
            New_Node = ListNode(element)
            current.next = New_Node
            current = current.next
            
        # Создаем второй LinkedList
        current = head2
        for element in enter2[1:]:
            New_Node = ListNode(element)
            current.next = New_Node
            current = current.next
            
        # Создаем третий LinkedList
        current = head3
        for element in enter3[1:]:
            New_Node = ListNode(element)
            current.next = New_Node
            current = current.next

        out =  [2,6]
        answer = Solution()
        z = answer.mergeKLists([head1, head2, head3])
        current3 = z
        for i in out:
            self.assertEqual(current3.val, i)
            current3 = current3.next

    def test_2_merge_K_Lists(self):
        enter1 = []

        head1 = ListNode(enter1[0]) if enter1 else None

        # Создаем первый LinkedList
        current = head1
        for element in enter1[1:]:
            New_Node = ListNode(element)
            current.next = New_Node
            current = current.next
        out =  []
        answer = Solution()
        z = answer.mergeKLists([head1])
        current3 = z
        for i in out:
            self.assertEqual(current3.val, i)
            current3 = current3.next

    def test_3_merge_K_Lists(self):
        enter1 = []

        head1 = ListNode(enter1[0]) if enter1 else None

        # Создаем первый LinkedList
        current = head1
        for element in enter1[1:]:
            New_Node = ListNode(element)
            current.next = New_Node
            current = current.next
        out =  []
        answer = Solution()
        z = answer.mergeKLists([head1])
        self.assertIsNone(z)


if __name__ == '__main__':
    try: unittest.main()
    except SystemExit: pass
