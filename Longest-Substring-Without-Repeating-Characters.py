class Solution(object):
    def lengthOfLongestSubstring(self, s):
        dict = {}
        sentence = []
        if s.__len__() ==0:
            return 0
        elif s.__len__() ==1:
            return 1
        for word in s:
            if sentence.__contains__(word):
                sentence = sentence[sentence.index(word)+1:]
                sentence.append(word)
                temp1 = ""
                for i in sentence:
                    temp1 = temp1 + i
                dict[temp1] = len(sentence)
            else:
                sentence.append(word)
                temp2 = ""
                for j in sentence:
                    temp2 = temp2 + j
                dict[temp2] = len(sentence)

        result = sorted(dict, key=lambda x: dict[x])[-1]
        return len(result)

solu = Solution()
print solu.lengthOfLongestSubstring("dvdf")







