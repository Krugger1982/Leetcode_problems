class Solution:
                                          
    def findSubstring(self, s, words):
        result = []
        window_len = 0
        for word in words:
            window_len += len(word)
            
        for i in range(len(s)-window_len+1):
            window = s[i:i+window_len]
            words_copy = []
            
            for word in words:
                words_copy.append(word)         # создадим копию списка слов для работы)
        
            if  window_is_words(window, words_copy):
                result.append(i)
        return result
            
 
def window_is_words(window, words):
    while len(window) > 0:
        len_before = len(window)
        for word in words:
            if window[:len(word)] == word:
                window = window[len(word):]                     # вырезаем найденное слово из куска строки
                words.remove(word)                              # и из списка слов, во избежание повторов
                
        if len(window) == len_before:
            # если хотя бы одно слово не найдено - цикл надо прерывать
            return False
    return True
        



import unittest
        
class Tests_Solution(unittest.TestCase):
        
    def test_1_window_is_words(self):
        window = 'defgabchigkabcabc'
        words = ['gk', 'hi', 'defg', 'abc', 'abc', 'abc']
        self.assertTrue(window_is_words(window, words))

    def test_2_window_is_words(self):
        window = 'abcdefgabchigkabc'
        words = ['gk', 'hi', 'mno', 'defg', 'abc', 'abc']
        self.assertFalse(window_is_words(window, words))

    def test_3_window_is_words(self):
        window = 'mnoabcdefgabchigkabc'
        words = ['gk', 'hi', 'defg', 'abc', 'abc']
        self.assertFalse(window_is_words(window, words))
        
    def test_3_1_findSubstring(self):
        s = "barfoothefoobarman"
        words = ["foo","bar"]
        out = [0, 9]
        answer = Solution()
        z = answer.findSubstring(s, words)
        for i in out:
            self.assertTrue(i in z)
        for i in z:
            self.assertTrue(i in out)

    def test_4_findSubstring(self):
        s = "barfoofoobarthefoobarman"
        words = ["bar","foo","the"]
        out = [6,9,12]
        answer = Solution()
        z = answer.findSubstring(s, words)
        for i in out:
            self.assertTrue(i in z)
        for i in z:
            self.assertTrue(i in out)

    def test_5_findSubstring(self):
        s = "wordgoodgoodgoodbestword"
        words = ["word","good","best","word"]
        out = []
        answer = Solution()
        z = answer.findSubstring(s, words)
        for i in out:
            self.assertTrue(i in z)
        for i in z:
            self.assertTrue(i in out)



    def test_6_findSubstring(self):
        s = "wordgoodgoodgoodbestword"
        words = ["word","good","best","good"]
        out = [8]
        answer = Solution()
        z = answer.findSubstring(s, words)
        for i in out:
            self.assertTrue(i in z)

        for i in z:
            self.assertTrue(i in out)
            
    def test_7_findSubstring(self):
        s = "pjzkrkevzztxductzzxmxsvwjkxpvukmfjywwetvfnujhweiybwvvsrfequzkhossmootkmyxgjgfordrpapjuunmqnxxdrqrfgkrsjqbszgiqlcfnrpjlcwdrvbumtotzylshdvccdmsqoadfrpsvnwpizlwszrtyclhgilklydbmfhuywotjmktnwrfvizvnmfvvqfiokkdprznnnjycttprkxpuykhmpchiksyucbmtabiqkisgbhxngmhezrrqvayfsxauampdpxtafniiwfvdufhtwajrbkxtjzqjnfocdhekumttuqwovfjrgulhekcpjszyynadxhnttgmnxkduqmmyhzfnjhducesctufqbumxbamalqudeibljgbspeotkgvddcwgxidaiqcvgwykhbysjzlzfbupkqunuqtraxrlptivshhbihtsigtpipguhbhctcvubnhqipncyxfjebdnjyetnlnvmuxhzsdahkrscewabejifmxombiamxvauuitoltyymsarqcuuoezcbqpdaprxmsrickwpgwpsoplhugbikbkotzrtqkscekkgwjycfnvwfgdzogjzjvpcvixnsqsxacfwndzvrwrycwxrcismdhqapoojegggkocyrdtkzmiekhxoppctytvphjynrhtcvxcobxbcjjivtfjiwmduhzjokkbctweqtigwfhzorjlkpuuliaipbtfldinyetoybvugevwvhhhweejogrghllsouipabfafcxnhukcbtmxzshoyyufjhzadhrelweszbfgwpkzlwxkogyogutscvuhcllphshivnoteztpxsaoaacgxyaztuixhunrowzljqfqrahosheukhahhbiaxqzfmmwcjxountkevsvpbzjnilwpoermxrtlfroqoclexxisrdhvfsindffslyekrzwzqkpeocilatftymodgztjgybtyheqgcpwogdcjlnlesefgvimwbxcbzvaibspdjnrpqtyeilkcspknyylbwndvkffmzuriilxagyerjptbgeqgebiaqnvdubrtxibhvakcyotkfonmseszhczapxdlauexehhaireihxsplgdgmxfvaevrbadbwjbdrkfbbjjkgcztkcbwagtcnrtqryuqixtzhaakjlurnumzyovawrcjiwabuwretmdamfkxrgqgcdgbrdbnugzecbgyxxdqmisaqcyjkqrntxqmdrczxbebemcblftxplafnyoxqimkhcykwamvdsxjezkpgdpvopddptdfbprjustquhlazkjfluxrzopqdstulybnqvyknrchbphcarknnhhovweaqawdyxsqsqahkepluypwrzjegqtdoxfgzdkydeoxvrfhxusrujnmjzqrrlxglcmkiykldbiasnhrjbjekystzilrwkzhontwmehrfsrzfaqrbbxncphbzuuxeteshyrveamjsfiaharkcqxefghgceeixkdgkuboupxnwhnfigpkwnqdvzlydpidcljmflbccarbiegsmweklwngvygbqpescpeichmfidgsjmkvkofvkuehsmkkbocgejoiqcnafvuokelwuqsgkyoekaroptuvekfvmtxtqshcwsztkrzwrpabqrrhnlerxjojemcxel"
        words = ["dhvf","sind","ffsl","yekr","zwzq","kpeo","cila","tfty","modg","ztjg","ybty","heqg","cpwo","gdcj","lnle","sefg","vimw","bxcb"]
        out = [935]
        answer = Solution()
        z = answer.findSubstring(s, words)
        for i in out:
            self.assertTrue(i in z)

        for i in z:
            self.assertTrue(i in out)            
        
if __name__ == '__main__':
    try: unittest.main()
    except SystemExit: pass
