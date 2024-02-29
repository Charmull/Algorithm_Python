def solution(cacheSize, cities):
    answer = 0
    cache = []
    cnt = 0
    if not cacheSize:
        return len(cities) * 5
    
    for city in cities:
        city = city.lower()
        is_in_cache = False
        for i in range(cnt):
            if cache[i] == city:
                answer += 1
                cache.pop(i)
                cache.append(city)
                is_in_cache = True
                break
                
        if not is_in_cache:
            answer += 5
            if cnt >= cacheSize:
                cache.pop(0)
                cnt -= 1
            cache.append(city)
            cnt += 1
    return answer