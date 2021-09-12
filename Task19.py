# Definiition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def removeNthFromEnd(self, head, n):
        count = 1
        current = head
        # частный случай - удаление единственного элемента
        if head.next is None and n == 1:
            head = None
        else:
            # Сначала пробежим по списку и посчитаем его элементы
            while current.next is not None:
                count += 1
                current = current.next
            
            current = head                          # Снова поставим указатель на "голову"
            # Частный случай - удаление первого элемента
            if n == count:
                head = head.next
            else:
                for iterator in range(count - 1 - n):   # Пробегаем до  элемента, предшествующего удаляемому
                    current = current.next
                current.next = current.next.next        # И перезаписываем эту ссылку
#                  \                 \
#        было       \                 \
#[Элемент(iterator)] --> [Удаляемый ] --> Удаляемый.next
#        стало
# [Элемент(iterator)] --> Удаляемый.next
        
        return head
        
        
        



import unittest
        
class Tests_Solution(unittest.TestCase):
        


    def test_1_fourSums(self):
        enter = [1,2,3,4,5]
        target = 2
        head = ListNode(enter[0])
        current = head
        for element in enter[1:]:
            New_Node = ListNode(element)
            current.next = New_Node
            current = current.next
        out =  [1,2,3,5]
        answer = Solution()
        z = answer.removeNthFromEnd(head, target)
        current2 = z
        for i in out:
            self.assertEqual(current2.val, i)
            current2 = current2.next

    def test_2_fourSums(self):
        enter = [1]
        target = 1
        head = ListNode(enter[0])
        current = head
        for element in enter[1:]:
            New_Node = ListNode(element)
            current.next = New_Node
            current = current.next
        out =  []
        answer = Solution()
        z = answer.removeNthFromEnd(head, target)
        for i in out:
            self.assertEqual(current2.val, i)
            current2 = current2.next
            
    def test_3_fourSums(self):
        enter = [1,2]
        target = 1
        head = ListNode(enter[0])
        current = head
        for element in enter[1:]:
            New_Node = ListNode(element)
            current.next = New_Node
            current = current.next
        out =  [1]
        answer = Solution()
        z = answer.removeNthFromEnd(head, target)
        current2 = z
        for i in out:
            self.assertEqual(current2.val, i)
            current2 = current2.next

    def test_4_fourSums(self):
        enter = [1,2]
        target = 2
        head = ListNode(enter[0])
        current = head
        for element in enter[1:]:
            New_Node = ListNode(element)
            current.next = New_Node
            current = current.next
        out =  [2]
        answer = Solution()
        z = answer.removeNthFromEnd(head, target)
        current2 = z
        for i in out:
            self.assertEqual(current2.val, i)
            current2 = current2.next
if __name__ == '__main__':
    try: unittest.main()
    except SystemExit: pass
