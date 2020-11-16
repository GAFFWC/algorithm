from sys import stdin, stdout
from collections import deque

output = ""

T = int(stdin.readline())

for _ in range(T):
    string = stdin.readline().split()[0]
    st = deque()

    flag = True
    for item in string:
        # 여는 괄호일 때
        if item == '(':
            st.append(item)

        # 닫는 괄호일 때
        # 스택이 비었거나 top이 여는 괄호가 아닌 경우
        elif len(st) == 0 or st[len(st) - 1] != '(':
            flag = False
            break

        # 스택이 비지 않았고, top이 여는 괄호인 경우
        else:
            st.pop()

    # 여닫는 쌍이 맞지 않거나 아직 괄호가 남은 경우 NO, 이외에는 YES
    output += "NO\n" if len(st) > 0 or flag == False else "YES\n"

stdout.write(output)