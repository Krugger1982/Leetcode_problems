def findMedianSortedArrays(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: float
    """
    R = addArrays(nums1, nums2)
    if len(R) % 2 == 1:     # Если в суммарном массиве нечетное количество элементов
        return float(R[len(R)//2])
    else:                   # Если четное
        return float((R[len(R)//2 - 1] + R[len(R)//2])/2)
        
def addArrays(N1, N2):
    res = []
    i = 0
    j = 0
    while i < len(N1) and j < len(N2):
        # Пока хотя бы один из массивов не кончился
        if N1[i] < N2[j]:
            res.append(N1[i])
            i += 1
        else:
            res.append(N2[j])
            j += 1
    # когда хотя бы один из массивов закончился, добавляем все что осталось во втором
    if i < len(N1):         # если закончился N2
        for item in N1[i:]:
            res.append(item)
    else:                   # если закончился N1
        for item in N2[j:]:
            res.append(item)
    print(res)
    return res



        
import unittest

class Tests_Solution(unittest.TestCase):
        
    def test_1_repeating(self):
        N1 = [1, 3]
        N2 = [2]
        Mediana = 2.00000
        self.assertEqual(findMedianSortedArrays(N1, N2), Mediana)

    def test_2_repeating(self):
        N1 = [1, 2]
        N2 = [3, 4]
        Mediana = 2.5
        self.assertEqual(findMedianSortedArrays(N1, N2), Mediana)

    def test_3_repeating(self):
        N1 = [0, 0]
        N2 = [0, 0]
        Mediana = 0.00000
        self.assertEqual(findMedianSortedArrays(N1, N2), Mediana)

    def test_4_repeating(self):
        N1 = []
        N2 = [1]
        Mediana = 1.00000
        self.assertEqual(findMedianSortedArrays(N1, N2), Mediana)

    def test_5_repeating(self):
        N1 = [2]
        N2 = []
        Mediana = 2.00000
        self.assertEqual(findMedianSortedArrays(N1, N2), Mediana)
        
if __name__ == '__main__':
    try: unittest.main()
    except SystemExit: pass
