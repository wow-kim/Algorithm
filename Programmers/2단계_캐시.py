def solution(cacheSize, cities):
    cache = []
    answer = 0
    if cacheSize == 0:
        return len(cities) * 5
      
    for city in cities:
        city = city.upper()
        if not city in cache:
            answer += 5
            if len(cache) < cacheSize:
                cache.append(city)
            else:
                cache.pop(0)
                cache.append(city)
        else:
            answer +=1
            cache.pop(cache.index(city))
            cache.append(city)
    return answer

#1.새로운 데이터가 들어온 경우
#캐시에 넣어준다.
#캐시가 가득차있다면, 가장 오래된 데이터를 제거하고 넣어준다.
#2.존재하는 데이터가 들어온 경우
#해당 데이터를 꺼낸 뒤,
#가장 최근 데이터 위치로 보내준다.