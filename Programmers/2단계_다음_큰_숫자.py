def solution(n):
    bin_n = format(n, 'b')
    num_1 = bin_n.count("1")

    i=1
    while num_1 != format(n+i, "b").count("1"):
        i += 1

    return n+i

print(solution(78))