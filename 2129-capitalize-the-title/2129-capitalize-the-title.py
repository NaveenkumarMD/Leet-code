class Solution:
    def capitalizeTitle(self, title: str) -> str:
        li=title.split(" ")
        li=[(i.casefold()).capitalize() if len(i)>2 else i.casefold() for i in li ]
        return " ".join(li)
        