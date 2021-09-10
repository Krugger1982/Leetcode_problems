def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """
    k = len(s)
    result = []                             # список с размерами неповторяющих кусочков строки
    while len(s) > 1:                       # цикл повторяется пока не иссякнет строка (более одного символа)
        i = 1
        for current in s[1:]:               # пробегаем по строке, начиная со второго символа
            if current in s[:i]:            # если встретилась повторяющаяся буква
                result.append(len(s[:i]))   # заносим размер кусочка ДО ВТОРОЙ в паре ПОВТОРЯЮЩЕЙСЯ буквы в результаты
                s = s[s.index(current)+1:]  # и удаляем  кусочек до ПЕРВОЙ повторяющейся (ВКЛЮЧИТЕЛЬНО)
                break
            elif i == len(s) - 1:           # если до конца строки повторов не встретилось
                result.append(len(s))       # заносим в ответы длину остатка
                s = s[:i]
            i += 1
    if len(s) == 1:
        result.append(1)
    if len(result) == 0:
        return k
    return max(result)

        
import unittest

class Tests_Solution(unittest.TestCase):
        
    def test_1_repeating(self):
        S = 'abcabcabcabcdaaaaaaaaaabsdef'
        self.assertEqual(lengthOfLongestSubstring(S), 6)

    def test_2_repeating(self):
        S = 'dvdf'
        self.assertEqual(lengthOfLongestSubstring(S), 3)

    def test_3_repeating(self):
        S = 'abcaaaaaa'
        self.assertEqual(lengthOfLongestSubstring(S), 3)

    def test_4_repeating(self):
        S = 'abcdefghi12345'
        self.assertEqual(lengthOfLongestSubstring(S), 14)

        
if __name__ == '__main__':
    try: unittest.main()
    except SystemExit: pass
