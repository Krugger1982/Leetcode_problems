class Solution:
        
    def generatePermutations(self, words):
        ''' Generates a matrix (a list with nested lists) of various combinations of words
            example:
            result = [['a', 'b', 'c'], ['a', 'c', 'b'], ['b', 'a', 'c'], ['b', 'c', 'a'], ['c', 'a', 'b'], ['c', 'b', 'a']]
        '''
        
        res = []
        if not words:
            return res
        if len(words) == 1:
            return [words]
        prev = self.generatePermutations(words[1:])     # permutations of a list without the 1st member
        word = words[0]
            
        for permutation in prev:
            # iterating over the previous permutations
            for position in range(len(permutation) + 1):
                # sorting through the places to insert a new word
                permutation1 = permutation[:position] + [word] + permutation[position:]         #  insert a new word
                if not permutation1 in res:              # avoid repetitions
                    res.append(permutation1)
        return res
                                  
    def findSubstring(self, s, words):
        result = []
        permutations = self.generatePermutations(words)
        for permutation in permutations:
            permutation = ''.join(permutation)
            for i in range(len(s) - len(permutation)+1):
                if s[i:i+len(permutation)] == permutation and not i in result:
                    result.append(i)
        return result
 
        
        
        



import unittest
        
class Tests_Solution(unittest.TestCase):
        
    def test_1_generatePermutations(self):
        enter = ['odin', 'dwa']
        out =  [['odin', 'dwa'], ['dwa', 'odin']]
        
        answer = Solution()
        z = answer.generatePermutations(enter)        
        for i in out:
            self.assertTrue(i in z)
        for i in z:
            self.assertTrue(i in out)
                
    def test_2_generatePermutations(self):
        enter = ['odin']
        out =  [['odin']]
        
        answer = Solution()
        z = answer.generatePermutations(enter)        
        for i in out:
            self.assertTrue(i in z)
        for i in z:
            self.assertTrue(i in out)

    def test_3_generatePermutations(self):
        enter = []
        out =  []
        
        answer = Solution()
        z = answer.generatePermutations(enter)        
        for i in out:
            self.assertTrue(i in z)
        for i in z:
            self.assertTrue(i in out)
            
    def test_4_generatePermutations(self):
        enter = ['odin', 'dwa', 'tri']
        out =  [['odin', 'dwa', 'tri'], ['dwa', 'odin', 'tri'], ['odin', 'tri', 'dwa'], ['dwa', 'tri', 'odin'], ['tri', 'odin', 'dwa'], ['tri', 'dwa', 'odin']]
        
        answer = Solution()
        z = answer.generatePermutations(enter)        
        for i in out:
            self.assertTrue(i in z)
        for i in z:
            self.assertTrue(i in out)

    def test_5_findSubstring(self):
        s = "barfoothefoobarman"
        words = ["foo","bar"]
        out = [0, 9]
        answer = Solution()
        z = answer.findSubstring(s, words)
        for i in out:
            self.assertTrue(i in z)
        for i in z:
            self.assertTrue(i in out)

    def test_6_findSubstring(self):
        s = "barfoofoobarthefoobarman"
        words = ["bar","foo","the"]
        out = [6,9,12]
        answer = Solution()
        z = answer.findSubstring(s, words)
        for i in out:
            self.assertTrue(i in z)
        for i in z:
            self.assertTrue(i in out)

    def test_7_findSubstring(self):
        s = "wordgoodgoodgoodbestword"
        words = ["word","good","best","word"]
        out = []
        answer = Solution()
        z = answer.findSubstring(s, words)
        for i in out:
            self.assertTrue(i in z)
        for i in z:
            self.assertTrue(i in out)



    def test_8_findSubstring(self):
        s = "wordgoodgoodgoodbestword"
        words = ["word","good","best","good"]
        out = [8]
        answer = Solution()
        z = answer.findSubstring(s, words)
        for i in out:
            self.assertTrue(i in z)

        for i in z:
            self.assertTrue(i in out)
            
    def test_9_findSubstring(self):
        s = "pjzkrkevzztxductzzxmxsvwjkxpvukmfjywwetvfnujhweiybwvvsrfequzkhossmootkmyxgjgfordrpapjuunmqnxxdrqrfgkrsjqbszgiqlcfnrpjlcwdrvbumtotzylshdvccdmsqoadfrpsvnwpizlwszrtyclhgilklydbmfhuywotjmktnwrfvizvnmfvvqfiokkdprznnnjycttprkxpuykhmpchiksyucbmtabiqkisgbhxngmhezrrqvayfsxauampdpxtafniiwfvdufhtwajrbkxtjzqjnfocdhekumttuqwovfjrgulhekcpjszyynadxhnttgmnxkduqmmyhzfnjhducesctufqbumxbamalqudeibljgbspeotkgvddcwgxidaiqcvgwykhbysjzlzfbupkqunuqtraxrlptivshhbihtsigtpipguhbhctcvubnhqipncyxfjebdnjyetnlnvmuxhzsdahkrscewabejifmxombiamxvauuitoltyymsarqcuuoezcbqpdaprxmsrickwpgwpsoplhugbikbkotzrtqkscekkgwjycfnvwfgdzogjzjvpcvixnsqsxacfwndzvrwrycwxrcismdhqapoojegggkocyrdtkzmiekhxoppctytvphjynrhtcvxcobxbcjjivtfjiwmduhzjokkbctweqtigwfhzorjlkpuuliaipbtfldinyetoybvugevwvhhhweejogrghllsouipabfafcxnhukcbtmxzshoyyufjhzadhrelweszbfgwpkzlwxkogyogutscvuhcllphshivnoteztpxsaoaacgxyaztuixhunrowzljqfqrahosheukhahhbiaxqzfmmwcjxountkevsvpbzjnilwpoermxrtlfroqoclexxisrdhvfsindffslyekrzwzqkpeocilatftymodgztjgybtyheqgcpwogdcjlnlesefgvimwbxcbzvaibspdjnrpqtyeilkcspknyylbwndvkffmzuriilxagyerjptbgeqgebiaqnvdubrtxibhvakcyotkfonmseszhczapxdlauexehhaireihxsplgdgmxfvaevrbadbwjbdrkfbbjjkgcztkcbwagtcnrtqryuqixtzhaakjlurnumzyovawrcjiwabuwretmdamfkxrgqgcdgbrdbnugzecbgyxxdqmisaqcyjkqrntxqmdrczxbebemcblftxplafnyoxqimkhcykwamvdsxjezkpgdpvopddptdfbprjustquhlazkjfluxrzopqdstulybnqvyknrchbphcarknnhhovweaqawdyxsqsqahkepluypwrzjegqtdoxfgzdkydeoxvrfhxusrujnmjzqrrlxglcmkiykldbiasnhrjbjekystzilrwkzhontwmehrfsrzfaqrbbxncphbzuuxeteshyrveamjsfiaharkcqxefghgceeixkdgkuboupxnwhnfigpkwnqdvzlydpidcljmflbccarbiegsmweklwngvygbqpescpeichmfidgsjmkvkofvkuehsmkkbocgejoiqcnafvuokelwuqsgkyoekaroptuvekfvmtxtqshcwsztkrzwrpabqrrhnlerxjojemcxel"
        words = ["dhvf","sind","ffsl","yekr","zwzq","kpeo","cila","tfty","modg","ztjg","ybty","heqg","cpwo","gdcj","lnle","sefg","vimw","bxcb"]
        out = [8]
        answer = Solution()
        z = answer.findSubstring(s, words)
        for i in out:
            self.assertTrue(i in z)

        for i in z:
            self.assertTrue(i in out)            
        
if __name__ == '__main__':
    try: unittest.main()
    except SystemExit: pass
