import sys
from collections import deque

output = ""

T = int(input())

for t in range(T):
    direction = 0 # l -> r
    dq = deque()
    commandLine = input().replace("RR", "")
    N = int(input())
    arr = input().strip('[]\n').split(',')

    if arr[0] != '':
        dq.extend(list(map(int, arr)))

    flag = True
    for command in commandLine:
        if command == 'R':
            direction = 1 if direction == 0 else 0

        else: # D
            if len(dq) == 0:
                print("error")
                flag = False
                break
            else:
                if direction == 1: # r -> l
                    dq.pop()
                else: # l -> r
                    dq.popleft()
                    
    if flag:
        if direction == 1:
            dq.reverse()
        print(str(dq).strip('deque()').replace(' ', ''))
