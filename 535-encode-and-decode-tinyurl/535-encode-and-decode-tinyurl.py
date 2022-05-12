import random
class Codec:
    dit={}
    def encode(self, longUrl: str) -> str:
        res=""
        x=longUrl.index("/")
        res+=longUrl[:x+2]
        res+="tinyurl/"
        temp=random.randint(10,1000)
        res+=str(temp)
        self.dit[temp]=longUrl
        return res
        

    def decode(self, shortUrl: str) -> str:
        res=""
        x=shortUrl.rindex("/")
        res+=shortUrl[x+1:]
        print(self.dit[int(res)])
        return self.dit[int(res)]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))