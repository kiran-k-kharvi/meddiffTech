class Path:
    def __init__(self, currentPath):
        self.initialPath = currentPath
    
    def cd(self, changedNewPath):
        i=0
        newPathList=changedNewPath.split('/')
        pathLength=len(newPathList)
        initialPathList=self.initialPath.split('/')
        if newPathList[0]=='':
            del initialPathList[:]
            initialPathList.append('/'+newPathList[1])
            i=i+2
        while(i<pathLength):
            j=len(initialPathList)-1
            if newPathList[i]=='..':
                initialPathList.pop(j)
            else:
                initialPathList.append(newPathList[i])
            i=i+1
        self.initialPath="/".join(initialPathList)

        pass


path = Path('/a/b/c/d')
path.cd('../x/y/../z')
print(path.initialPath)