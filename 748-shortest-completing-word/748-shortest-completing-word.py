class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        dict_licensePlate={}
        for i in licensePlate:
            if i==" " or i.isnumeric():
                continue
            i=i.lower()
            if i not in dict_licensePlate:
                dict_licensePlate[i]=1
            else:
                dict_licensePlate[i]+=1
        print(dict_licensePlate)
        min_length=999999999
        for word in words:
            dict_letter={}
            for letter in word:
                if letter not in dict_letter:
                    dict_letter[letter]=1
                else:
                    dict_letter[letter]+=1
            flag=True
            for i in dict_licensePlate:
                if i not in dict_letter:
                    flag=False
                    break
                if dict_licensePlate[i]>dict_letter[i]:
                    flag=False
                    break
            if flag:
                if(len(word)<min_length):
                    min_length=len(word)
                    return_word=word
        return return_word
        
