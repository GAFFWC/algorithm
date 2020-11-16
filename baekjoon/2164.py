import sys
from collections import deque

N = int(sys.stdin.readline())

arr = deque()
for i in range(N):
    arr.append(i + 1)

while (len(arr) > 1):
    arr.popleft()
    front = arr.popleft()
    arr.append(front)

print(arr[0])
