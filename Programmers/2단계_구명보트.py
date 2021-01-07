def solution(people, limit):
    people.sort()
    count = 0
    i=0
    j = len(people) - 1 
    while i <= j:
        if people[i] + people[j] <= limit:
            count += 1
            i += 1
            j -= 1
        else:
            count += 1
            j -= 1

    return count

print(solution([70, 50, 80, 50], 100))
print(solution([70, 80, 50], 100))