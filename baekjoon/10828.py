from sys import stdin, stdout
from collections import deque

output = ""

N = int(stdin.readline())

dq = deque()
for _ in range(N):
    command = stdin.readline().split()
    
    if command[0] == "push":
        dq.append(command[1])
    
    if command[0] == "pop":
        output += dq.pop() + "\n" if len(dq) > 0 else "-1\n"

    if command[0] == "size":
        output += str(len(dq)) + "\n"

    if command[0] == "empty":
        output += "1\n" if len(dq) == 0 else "0\n"

    if command[0] == "top":
        output += dq[len(dq) - 1] + "\n" if len(dq) > 0 else "-1\n"

stdout.write(output) 
