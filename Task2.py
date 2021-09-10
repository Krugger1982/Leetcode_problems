# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
         
class Solution(object):
    pass 
def addTwoNumbers(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
        
    cur1 = l1
    cur2 = l2
    Res = ListNode()
    current = Res
    v_ume = 0
    while cur1 is not None or cur2 is not None or v_ume != 0:
        little_summa = sum_nodes(cur1, cur2, v_ume)
        current.val = little_summa[0].val 
        v_ume = little_summa[1]
        if cur1 is not None:
            cur1 = cur1.next
        if cur2 is not None:
            cur2 = cur2.next
        if cur1 is not None or cur2 is not None or v_ume != 0:
            current.next = ListNode()
        current = current.next
        print ('ответ - ',  little_summa[0].val, '  в уме - ', v_ume)
    
    return Res
        
def sum_nodes(N1, N2, v_ume=0):
    if N1 is None and N2 is None:                               # когда числа кончились, но есть еще цифра "в уме"
        return (ListNode(v_ume), 0)
    elif N1 is None and N2 is not None:                         # одно из чисел кончилось
        return(ListNode((N2.val + v_ume)% 10), (N2.val + v_ume)// 10)
    elif N2 is None and N1 is not None:                         # или другое кончилось
        return(ListNode((N1.val + v_ume)% 10), (N1.val + v_ume)// 10)
    else:
        return(ListNode((N1.val + N2.val + v_ume) % 10), (N1.val + N2.val + v_ume) // 10)           # есть оба числа и "в уме"
        
def Linkedlist(List):
    if len(List) == 0:
        return None
    Res = ListNode(List[0])
    current = Res
    if len(List) > 1:
        for item in List[1:-1]:        
            current.next = ListNode(item)
            current = current.next
            current.val = item
        current.next = ListNode(List[-1])
    return Res

import unittest

class Tests_Solution(unittest.TestCase):
        
    def test_1_sumnodes(self):
        N1 = ListNode(1, None)
        N2 = ListNode(9, None)
        Sum = sum_nodes(N1, N2)
        self.assertEqual(Sum[0].val, 0)
        self.assertEqual(Sum[1], 1)
                
        N1 = ListNode(1, None)
        N2 = ListNode(1, None)
        Sum = sum_nodes(N1, N2)
        self.assertEqual(Sum[0].val, 2)
        self.assertEqual(Sum[1], 0)

        N1 = None
        N2 = ListNode(9, None)
        Sum = sum_nodes(N1, N2)
        self.assertEqual(Sum[0].val, 9)
        self.assertEqual(Sum[1], 0)


        N1 = ListNode(9, None)
        N2 = None
        Sum = sum_nodes(N1, N2)
        self.assertEqual(Sum[0].val, 9)
        self.assertEqual(Sum[1], 0)
        
        N1 = None
        N2 = None
        Sum = sum_nodes(N1, N2)
        self.assertEqual(Sum[0].val, 0)
        self.assertEqual(Sum[1], 0)

    def test2_Linkedlist(self):
        list1 = [0]
        Linkedlist1 = Linkedlist(list1)
        cur = Linkedlist1
        C = 0
        while cur is not None:
            self.assertEqual(cur.val, list1[C])
            cur = cur.next
            C += 1
            
    def test_3_Solution1(self):
        list1 = [2, 4, 3]
        list2 = [5, 6, 4]
        list_Sum = [7, 0, 8]
        Linked_Sum = addTwoNumbers(Linkedlist(list1), Linkedlist(list2))
        cur = Linked_Sum
        C = 0
        while cur is not None:
            self.assertEqual(cur.val, list_Sum[C])
            cur = cur.next
            C += 1        
        
    def test_4_Solution2(self):
        list1 = [0]
        list2 = [0]
        list_Sum = [0]
        Linked_Sum = addTwoNumbers(Linkedlist(list1), Linkedlist(list2))
        cur = Linked_Sum
        C = 0
        while cur is not None:
            self.assertEqual(cur.val, list_Sum[C])
            cur = cur.next
            C += 1                

    def test_5_Solution3(self):
        list1 = [9,9,9,9,9,9,9]
        list2 = [9,9,9,9]
        list_Sum = [8,9,9,9,0,0,0,1]
        Linked_Sum = addTwoNumbers(Linkedlist(list1), Linkedlist(list2))
        cur = Linked_Sum
        C = 0
        while cur is not None:
            self.assertEqual(cur.val, list_Sum[C])
            cur = cur.next
            C += 1        
        
if __name__ == '__main__':
    try: unittest.main()
    except SystemExit: pass
