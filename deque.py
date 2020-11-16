from collections import deque

dq = deque([1, 2, 3, 4, 5])


# 원소 제거
dq.pop()  # [1, 2, 3, 4]
print(dq)

dq.popleft()  # [2, 3, 4]
print(dq)


# 원소 삽입
dq.append(5)  # [2, 3, 4, 5]
print(dq)

dq.appendleft(1)  # [1, 2, 3, 4, 5]
print(dq)


# 리스트 삽입 (-> 추가할 리스트 첫 원소부터 순서대로 삽입)
tempArr = [1, 2, 3]
dq.extend(tempArr)  # [1, 2, 3, 4, 5, 1, 2, 3]
print(dq)

dq.extendleft(tempArr)  # [3, 2, 1, 1, 2, 3, 4, 5, 1, 2, 3]
print(dq)


# 순서 변경 (역순, 회전)
dq.reverse()  # [3, 2, 1, 5, 4, 3, 2, 1, 1, 2, 3]
print(dq)

dq.rotate(1)  # [3, 3, 2, 1, 5, 4, 3, 2, 1, 1, 2]
print(dq)

dq.rotate(-1)  # [3, 2, 1, 5, 4, 3, 2, 1, 1, 2, 3]
print(dq)


# etc

# 처음으로 만나는 값(1)을 제거 (없을 시 ValueError)
dq.remove(1)  # [3, 2, 5, 4, 3, 2, 1, 1, 2, 3]
print(dq)

# parameter와 값이 같은 원소의 갯수를 반환
print(dq.count(3))  # 3

# 덱 초기화
dq.clear()
