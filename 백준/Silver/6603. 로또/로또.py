import sys
input = sys.stdin.readline

from itertools import combinations

while True:

    # 입력
    elements = list(map(int, input().split()))
    
    k = elements[0]   # 크기 k
    s = elements[1:]  # 집합 S

    # 종료 조건
    if k == 0: 
        break
    
    
    # 조합 찾기
    for combination in combinations(s, 6):
        print(" ".join(map(str, combination)))
    print()