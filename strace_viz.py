import sys
import PidTree
import string
from os import listdir
from os.path import isfile, join, dirname

def main():
    if len(sys.argv) < 2 or len(sys.argv) > 4:
        print("usage: python strace_viz.py <strace-file> --hide-pid --hide-proc-name")
        return
    hidePid = True if '--hide-pid' in sys.argv else False
    hideProcName = True if '--hide-proc-name' in sys.argv else False
    if hidePid and hideProcName:
        print("Hiding all data...why are you even running this.........")
        return
    strace_file = sys.argv[1]
    pid = (strace_file.rpartition('.'))[2]

    fp = open(strace_file, 'r')

    curPid = PidTree.Pid(int(pid))
    tree = PidTree.PidTree(curPid, hidePid=hidePid, hideProcName=hideProcName)

    pidDict = {int(pid): curPid}

    curDir = dirname(strace_file)
    files = [ join(curDir,f) for f in listdir(curDir) if isfile(join(curDir,f))]
    files.remove(strace_file)

    parse_clones(fp, curPid, pidDict)

    for f in files:
        fp = open(f, 'r')
        pid = int((f.rpartition('.'))[2])
        if pid in pidDict:
            curPid = pidDict[pid]
        else:
            curPid = PidTree.Pid(pid)
            pidDict[pid] = curPid
        parse_clones(fp, curPid, pidDict)

    tree.printTree()

def parse_clones(fp, curPid, pidDict):
    for line in fp:
        if 'clone(' in line:
            newPid = curPid.addChild(PidTree.Pid(parse_pid(line)))
            pidDict[newPid.getVal()] = newPid
        if 'execve(' in line:
            idx1 = line.find('(')+1
            idx2 = line.find(')')
            curPid.addProcName(line[idx1:idx2])




def parse_pid(line):
    pid = ((line.rpartition('='))[2]).strip()
    return int(pid)


if __name__ == '__main__':
    main()