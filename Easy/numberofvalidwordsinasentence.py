class Solution:
    def countValidWords(self, sentence: str) -> int:
        #separating the words from the sentence
        words=sentence.split(" ")
        count=0
        print(words)
        for word in words:
            #condition1 check for lowercase letters        
            for letter in word:
                if letter.isnumeric():
                    continue
            count+=1
        print (count)
x=Solution()
x.countValidWords(sentence = "/^*naveen")
