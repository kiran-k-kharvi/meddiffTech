def groupByOwner(kv):
    newDict = {}
    for k,v in kv.items():
        if v in newDict:
            temp = newDict[v]
            temp.append(k)
            newDict[v]=temp
        else:
            newDict[v]=[k]
    print(newDict)

a = {'Input.txt': 'Randy', 'Code.py': 'Stan', 'Output.txt': 'Randy'}

groupByOwner(a)