# strace-pid-visualizer
Script to create a parent/child process relationship tree

Usage:
python strace_viz.py <strace-file> [--hide-pid, --hide-proc-name]

The strace file that you specify in will be the head of the pid tree that will be generated.

--hide-pid:
  This will hide the pid when examining the tree. Useful if you only want to examine the names of the processes being forked
  
--hide-proc-name:
  This will hide the proccess name and arguments and only show the pid in the tree.

Typical strace command used for this utility: strace -tt -ff -o strace.log <command-to-trace>
