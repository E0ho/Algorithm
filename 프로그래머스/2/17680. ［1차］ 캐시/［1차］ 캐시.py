# DB cache 크기에 따른 실행 속도

# cache Hit -> 1초
# cache Miss -> 5초

from collections import deque

def solution(cacheSize, cities):
    answer = 0
    time = 0
    
    # cache 생성
    cache = deque()
    
    # cache 사용 x
    if cacheSize == 0:
        time = len(cities) * 5
    
    # cache 사용 o
    else:
        
        # 모든 도시 검색
        for city in cities:
            city = city.upper()

            # cache Hit -> 1초
            if city in cache:
                time += 1

                # cache 업데이트
                cache.remove(city)
                cache.append(city)


            # cache Miss -> 5초
            else:
                time += 5       

                # 가장 오래된 cache 삭제
                if len(cache) == cacheSize:
                    cache.popleft()

                # cache에 도시 추가
                cache.append(city)
                
    answer = time
    return answer