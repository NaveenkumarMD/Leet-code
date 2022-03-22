class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        def getFileContent(file):
            return file[file.find("("):file.find(")")]
        def getFileName(file):
            return file[:file.find("(")]
        
        contentToFile = defaultdict(set)
        for path in paths:
            splitPath = path.split(" ")
            directory = splitPath[0]
            
            for file in splitPath[1:]:
                content = getFileContent(file)
                fileName = getFileName(file)
                contentToFile[content].add(directory + "/" + fileName)
        
        return [list(contentToFile[key]) for key in contentToFile.keys() if len(contentToFile[key]) > 1]