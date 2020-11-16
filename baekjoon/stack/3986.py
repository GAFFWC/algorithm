from sys import stdin, stdout
from collections import deque

cnt = 0

N = int(input())

for _ in range(N):
    string = input()
    st = deque()

    for item in string:
        # 여는 괄호일 때
        if item == 'A':
            if len(st) == 0 or st[len(st) - 1] == 'B':
                st.append(item)
            else:
                st.pop()

        if item == 'B':
            if len(st) == 0 or st[len(st) - 1] == 'A':
                st.append(item)
            else:
                st.pop()

    if len(st) == 0:
        cnt += 1

print(cnt)