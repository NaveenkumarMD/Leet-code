from typing import Dict, List

class TrieNode:
    def __init__(self)->None:
        #children dict of keys (a to z) values(child Trienode)
        self.children:Dict[str:str]={}
        #end variable represents the end of the word
        self.end:bool=False
class Trie:
    def __init__(self)->None:
        self.root:TrieNode=TrieNode()
    #words is an list of words Ex:["naveen","sethu","logan"]
    def build(self,words:List[str])->None:
        for word in words:
            self.insert(word)
    def insert(self,word:str)->None:
        node:Trie=self.root
        #looping through characters to insert in the trie
        for char in word:
            #checking whether the character is already present in the particular level of the tree
            # if not present a new node is created and linked
            if char not in node.children:
                node.children[char]=TrieNode()
            #moving to the next node ie the next character
            node=node.children[char]
        #marking the end of word
        node.end=True
    def search(self,word)->bool:
        node:Trie=self.root
        for char in word:
            #checking whether the character is present in the trie
            if char in node.children:
                node=node.children[char]
            else:
                return False
        #checking whether we are at the end of the word or not
        return node.end
    
    def walktrie(self,node,prefix:str,suggestions:List[str])->None:
        if node.children:
            for char in node.children :
                suggestion_word=prefix+char
                if node.children[char].end:
                    suggestions.append(suggestion_word)
                self.walktrie(node.children[char],suggestion_word,suggestions)
        
    def autocomplete(self,prefix:str)->List[str]:
        # Lets take prefix="na" moving to "a"
        node=self.root
        suggestions:List[str]=[]
        for char in prefix:
            if char in node.children:
                node=node.children[char]
            else:
                return suggestions
        #checking if prefix form a word of its own
        if node.end:
            suggestions.append(prefix)
        self.walktrie(node,prefix,suggestions)
        return suggestions
            
if __name__=="__main__":
    word_dict:Trie=Trie()
    word_dict.build(["naveen","sethu","logan","nainika"])
    suggestions:List[str]=word_dict.autocomplete("na")
    for i in suggestions:
        print(i)

    
            
    
            