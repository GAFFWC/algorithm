import sys
from collections import deque

dq = deque()
output = ""

N = int(sys.stdin.readline())

for i in range(N):
    input = sys.stdin.readline().split()

    if input[0] == "push_back":
        dq.append(input[1])
    
    elif input[0] == "push_front":
        dq.appendleft(input[1])

    elif input[0] == "pop_front":
        output += "-1\n" if len(dq) == 0 else dq.popleft() + "\n"
    
    elif input[0] == "pop_back":
        output += "-1\n" if len(dq) == 0 else dq.pop() + "\n"

    elif input[0] == "front":
        output += "-1\n" if len(dq) == 0 else dq[0] + "\n"
    
    elif input[0] == "back":
        output += "-1\n" if len(dq) == 0 else dq[len(dq) - 1] + "\n"


    elif input[0] == "size":
        output += str(len(dq)) + "\n"
    
    elif input[0] == "empty":
        output += "0\n" if len(dq) > 0 else "1\n"

print(output)