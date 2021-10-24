import os
if __name__=="__main__":
    if os.path.exists("demo.txt"):
        print("exisr")
        os.remove("demo.txt")

