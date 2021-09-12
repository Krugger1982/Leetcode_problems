class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
         
class Solution:
    def mergeTwoLists(self, l1, l2):
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        # Сначала сравниваем головы, чтоб установить указатель head
        current1 = l1
        current2 = l2
        if current1.val <= current2.val:
            head = l1
        else:
            head = l2
            
        
        # Затем сравниваем  ноды до тех пор, пока какой-нибудь список не закончится
        while current1 is not None and current2 is not None:
            if current1.val <= current2.val and (current1.next is None or current1.next.val > current2.val):
                # встраиваем С2 между С1 и С1.next
                prev1 = current1
                prev2 = current2
                current1 = current1.next
                while current2.next is not None and current2.val == current2.next.val:
                    current2 = current2.next
                current2 = current2.next
                prev1.next = prev2
                while prev2.next is not None and prev2.val == prev2.next.val:
                    prev2 = prev2.next
                prev2.next = current1
                current1 = prev2

            elif current1.val <= current2.val and (current1.next is not None and current1.next.val <= current2.val):
                current1 = current1.next

            elif current1.val > current2.val and (current2.next is None or current1.val <= current2.next.val):
                # встраиваем С1 между С2 и С2.next
                prev1 = current1
                prev2 = current2
                while current1.next is not None and  current1.val == current1.next.val:
                    current1 = current1.next
                current1 = current1.next
                current2 = current2.next
                prev2.next = prev1
                while prev1.next is not None and prev1.val == prev1.next.val:
                    prev1 = prev1.next
                prev1.next = current2
                current2 = prev1
            elif current1.val > current2.val and (current2.next is not None and current1.val > current2.next.val):
                current2 = current2.next
        return head
        
        
        



import unittest
        
class Tests_Solution(unittest.TestCase):
        
    def test_1_mergeTwoLists(self):
        enter1 = [1,2,4]
        enter2 = [1,3,4]        
        head1 = ListNode(enter1[0]) if enter1 else None
        head2 = ListNode(enter2[0]) if enter2 else None
        
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
            
        out =  [1,1,2,3,4,4]
        answer = Solution()
        z = answer.mergeTwoLists(head1, head2)
        current3 = z
        for i in out:
            self.assertEqual(current3.val, i)
            current3 = current3.next

    def test_2_mergeTwoLists_one_list_is_empty(self):
        enter1 = [1,2,4]
        enter2 = []        
        head1 = ListNode(enter1[0]) if enter1 else None
        head2 = ListNode(enter2[0]) if enter2 else None
        
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
            
        out =  [1,2,4]
        answer = Solution()
        z = answer.mergeTwoLists(head1, head2)
        current3 = z
        for i in out:
            self.assertEqual(current3.val, i)
            current3 = current3.next

    def test_3_mergeTwoLists_one_list_is_empty(self):
        enter1 = []
        enter2 = [1,3,4]        
        head1 = ListNode(enter1[0]) if enter1 else None
        head2 = ListNode(enter2[0]) if enter2 else None
        
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
            
        out =  [1,3,4]
        answer = Solution()
        z = answer.mergeTwoLists(head1, head2)
        current3 = z
        for i in out:
            self.assertEqual(current3.val, i)
            current3 = current3.next

    def test_4_mergeTwoLists_both_lists_empty(self):
        enter1 = []
        enter2 = []        
        head1 = ListNode(enter1[0]) if enter1 else None
        head2 = ListNode(enter2[0]) if enter2 else None
        
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
            
        out =  []
        answer = Solution()
        z = answer.mergeTwoLists(head1, head2)
        self.assertIsNone(z)


    def test_5_mergeTwoLists(self):
        enter1 = [1,2,4]
        enter2 = [5, 6, 8]        
        head1 = ListNode(enter1[0]) if enter1 else None
        head2 = ListNode(enter2[0]) if enter2 else None
        
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
            
        out =  [1,2, 4, 5, 6, 8]
        answer = Solution()
        z = answer.mergeTwoLists(head1, head2)
        current3 = z
        for i in out:
            self.assertEqual(current3.val, i)
            current3 = current3.next

        
    def test_6_mergeTwoLists_single_elements(self):
        enter1 = [1]
        enter2 = [4]        
        head1 = ListNode(enter1[0]) if enter1 else None
        head2 = ListNode(enter2[0]) if enter2 else None
        
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
            
        out =  [1,4]
        answer = Solution()
        z = answer.mergeTwoLists(head1, head2)
        current3 = z
        for i in out:
            self.assertEqual(current3.val, i)
            current3 = current3.next
            
    def test_7_mergeTwoLists_equal_elements(self):
        enter1 = [1]
        enter2 = [1]        
        head1 = ListNode(enter1[0]) if enter1 else None
        head2 = ListNode(enter2[0]) if enter2 else None
        
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
            
        out =  [1,1]
        answer = Solution()
        z = answer.mergeTwoLists(head1, head2)
        current3 = z
        for i in out:
            self.assertEqual(current3.val, i)
            current3 = current3.next
            
    def test_8_mergeTwoLists_with_repeats(self):
        enter1 = [-9,-5,-3,-2,-2,3,7]
        enter2 = [-10,-8,-4,-3,-1,3]
        head1 = ListNode(enter1[0]) if enter1 else None
        head2 = ListNode(enter2[0]) if enter2 else None
        
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
            
        out =  [-10,-9,-8,-5,-4,-3,-3,-2,-2,-1,3,3,7]
        answer = Solution()
        z = answer.mergeTwoLists(head1, head2)
        current3 = z
        for i in out:
            self.assertEqual(current3.val, i)
            current3 = current3.next
            
    def test_9_mergeTwoLists_with_repeats(self):
        enter1 = [-9,-5,-3,-2,-2,3,7]
        enter2 = [-10, -10, -10,-8,-4,-3,-1,3]
        head1 = ListNode(enter1[0]) if enter1 else None
        head2 = ListNode(enter2[0]) if enter2 else None
        
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
            
        out =  [-10, -10, -10,-9,-8,-5,-4,-3,-3,-2,-2,-1,3,3,7]
        answer = Solution()
        z = answer.mergeTwoLists(head1, head2)
        current3 = z
        for i in out:
            self.assertEqual(current3.val, i)
            current3 = current3.next
            
    def test_10_mergeTwoLists_with_repeats(self):
        enter1 = [-9, -9, -9,-5,-3,-2,-2,3,7]
        enter2 = [-10,-8,-4,-3,-1,3]
        head1 = ListNode(enter1[0]) if enter1 else None
        head2 = ListNode(enter2[0]) if enter2 else None
        
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
            
        out =  [-10,-9, -9, -9,-8,-5,-4,-3,-3,-2,-2,-1,3,3,7]
        answer = Solution()
        z = answer.mergeTwoLists(head1, head2)
        current3 = z
        for i in out:
            self.assertEqual(current3.val, i)
            current3 = current3.next
if __name__ == '__main__':
    try: unittest.main()
    except SystemExit: pass
