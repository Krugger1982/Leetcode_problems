class Solution:
    def strStr(self, haystack, needle):
        if len(needle) == 0:
            return 0
        for index in range(len(haystack)):
            if haystack[index] != needle[0]:
                continue
            else:
                if haystack[index:index+len(needle)] == needle:
                    return index
            
        return -1   

        

