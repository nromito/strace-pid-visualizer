class PidTree:
    def __init__(self, hidePid=False, hideProcName=False):
        self.head = None
        self.hidePid = hidePid
        self.hideProcName = hideProcName
    def __init__(self, pidObject, hidePid=False, hideProcName=False):
        self.head = pidObject
        self.hidePid = hidePid
        self.hideProcName = hideProcName
    def empty(self):
        return self.head == None
    def addHead(self, pidObject):
        self.head = pidObject
        return pidObject
    def printTree(self):
        printTreeRec(self.head, 0, self.hidePid, self.hideProcName)

class Pid:
    def __init__(self, val):
        self.val = val
        self.name = "---"
        self.children = []
    def getVal(self):
        return self.val
    def getProcName(self):
        return self.name
    def getChildren(self):
        return self.children
    def addChild(self, childPid):
        self.children.append(childPid)
        return childPid
    def addProcName(self, name):
        self.name = name

def printTreeRec(curPid, depth, hidePid, hideProcName):
    spaces = ""
    for i in range(depth*3):
        spaces += " "
    if hidePid:
        print('{0}{1}'.format(spaces, curPid.getProcName()))
    elif hideProcName:
        print('{0}{1}'.format(spaces, curPid.getVal()))
    else:
        print('{0}{1} {2}'.format(spaces, curPid.getVal(), curPid.getProcName()))
    for child in curPid.getChildren():
        printTreeRec(child, depth + 1, hidePid, hideProcName)