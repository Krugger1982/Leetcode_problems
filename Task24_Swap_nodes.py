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
    def swapPairs(self, head):
        """
        :type head: List[ListNode]
        :rtype: ListNode
        """
        # Если на вход подан пустой список или состоящий из елинственной ноды
        if head is None or head.next is None:
            return head
        # Сначала переворачиваем первые два элемента списка (head и head.next)

                            # БЫЛО   A -> B -> C ...
                            #       head
        
        A = head        # первый член
        B = head.next   # второй член
        head = B
        A.next = B.next
        B.next = A

                            # СТАЛО  B -> A -> C ... 
                            #       head

        # переходим к следующей паре
        B = A.next
        if B is None or B.next is None:
            return head
        C = B.next
                            # Теперь стало:  (X) -> (A) -> B -> C -> ...
                            #               head
        # В скобках - ноды которые уже поменяны
        # теперь надо менять B и C

        # Теперь циклично повторяем обмены и переходы пока не встретим None
        while B is not None and C is not None:
            # обмен
            A.next = C
            B.next = C.next
            C.next = B                   # (X)->(A)->(C)->(B)->

            # переход
            A = B
            B = A.next
            if B is not None:
                C = B.next              # (X)->(X)->(X)->(A) -> B -> C(or NOne)->...
        return head


import unittest
        
class Tests_Solution(unittest.TestCase):
        
    def test_1_swapPairs_4etniy(self):
        enter = [1, 2, 3, 4]
        head = ListNode(enter[0]) if enter else None
        # Создаем первый LinkedList
        current = head
        for element in enter[1:]:
            New_Node = ListNode(element)
            current.next = New_Node
            current = current.next
            
        out =  [2, 1, 4, 3]
        answer = Solution()
        z = answer.swapPairs(head)
        current3 = z
        for i in out:
            self.assertEqual(current3.val, i)
            current3 = current3.next

    def test_2_swapPairs_emptyList(self):
        enter = []
        head = ListNode(enter[0]) if enter else None
        # Создаем первый LinkedList
        current = head
        for element in enter[1:]:
            New_Node = ListNode(element)
            current.next = New_Node
            current = current.next
        answer = Solution()
        z = answer.swapPairs(head)
        self.assertIsNone(z)

            
    def test_3_swapPairs_singleNodeList(self):
        enter = [1]
        head = ListNode(enter[0]) if enter else None
        # Создаем первый LinkedList
        current = head
        for element in enter[1:]:
            New_Node = ListNode(element)
            current.next = New_Node
            current = current.next
        current = head    
        answer = Solution()
        z = answer.swapPairs(current)
        self.assertEqual(z, head)
            
    def test_4_swapPairs_Ne4etniy(self):
        enter = [1, 2, 3, 4, 5]
        head = ListNode(enter[0]) if enter else None
        # Создаем первый LinkedList
        current = head
        for element in enter[1:]:
            New_Node = ListNode(element)
            current.next = New_Node
            current = current.next
            
        out =  [2, 1, 4, 3, 5]
        answer = Solution()
        z = answer.swapPairs(head)
        current3 = z
        for i in out:
            self.assertEqual(current3.val, i)
            current3 = current3.next

if __name__ == '__main__':
    try: unittest.main()
    except SystemExit: pass
