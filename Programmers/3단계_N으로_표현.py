import collections
def solution(N, number):
    if N == number:
        return 1
    dp = collections.defaultdict(list)
    dp[1].append(N)

    for i in range(2,9):
        dp[i].append(int(str(N)*i))
        for j in range(1,5):
            # dp[i]는 dp[i-j]와 dp[j]의 조합
            for d_i in dp[i-j]:
                dp[i].extend(list(map(lambda x:x+d_i, dp[j])))
                dp[i].extend(list(map(lambda x:x-d_i, dp[j])))
                dp[i].extend(list(map(lambda x:x*d_i, dp[j])))
                try:
                    dp[i].extend(list(map(lambda x:x//d_i, dp[j])))
                except:
                    continue
        if number in dp[i]:
            return i

    return -1