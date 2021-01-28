class Solution:
    def isAlienSorted(self, words: list[str], order: str) -> bool:
        mapping = {}
        eng_order = "abcdefghijklmnopqrstuvwxyz"
        for index, value in enumerate(order):
            mapping[value] = eng_order[index]
        for i_word, word in enumerate(words):  
            new_word = ""           
            for index, c in enumerate(word):
                new_word += mapping[c]
            words[i_word] = new_word
        print(words)   
        if(words == sorted(words)): 
            return True

        return False             

                
def test_func():    
    test = Solution()
    assert test.isAlienSorted(["hello","leetcode"], "hlabcdefgijkmnopqrstuvwxyz") == True
    assert test.isAlienSorted(["word","world", "row"], "worldabcefghijkmnpqstuvxyz") == False
    assert test.isAlienSorted(["apple","app"], "abcdefghijklmnopqrstuvwxyz") == False
