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
         

class Solution():
    def reverseKGroup(self, head, k):

        Reverce = True  # Флаг, обозначающий необходимость реверса, то есть последовательность - не хвостовая
        Nodes = []      # промежуточный список
        current = head
        
        # Сначала первые k элементов списка помещаем с список Nodes
        for i in range(k):
            if current is not None:
                Nodes.append(current)
                current = current.next
            else:               # Когда встретим конец списка 
                Reverce = False # переворачивать остаток уже не надо
                break
        # В конце этого цикла указатель current стоит на k+1 элементе, то есть на первом элементе следующего "куска"
        
        if Reverce:                         # Если "кусок" не концевой
            head = Nodes.pop()              # переставляем указатель head
            current_out = head
            while Nodes:     
                current_out.next = Nodes.pop()  # вытаскиваем элементы из списка Nodes  в обратном порядке, с хвоста
                current_out = current_out.next
            current_out.next = current

        
        # Теперь циклично пробежим по оставшимся кускам
        while Reverce:
            for i in range(k):
                if current is not None:
                    Nodes.append(current)
                    current = current.next
                else:                   # Когда встретим конец списка 
                    Reverce = False     # переворачивать остаток уже не надо
                    break

            if Reverce:                         # Если "кусок" не концевой
                while Nodes:     
                    current_out.next = Nodes.pop()  # вытаскиваем элементы из списка Nodes  в обратном порядке, с хвоста
                    current_out = current_out.next
                current_out.next = current

        return head


import unittest
        
class Tests_Solution(unittest.TestCase):
        
    def test_1_reverseKGroup_4etniy(self):
        enter = [1]
        k = 1
        head = ListNode(enter[0]) if enter else None
        # Создаем первый LinkedList
        current = head
        for element in enter[1:]:
            New_Node = ListNode(element)
            current.next = New_Node
            current = current.next
            
        answer = Solution()
        z = answer.reverseKGroup(head, k)
        current3 = z
        while current3 is not None:
            print(current3.val)
            current3 = current3.next


if __name__ == '__main__':
    try: unittest.main()
    except SystemExit: pass
