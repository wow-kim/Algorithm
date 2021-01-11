from collections import Counter
def solution(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    str1 = Counter([a + b for a, b in zip(str1[:-1], str1[1:]) if (a+b).isalpha()])
    str2 = Counter([a + b for a, b in zip(str2[:-1], str2[1:]) if (a+b).isalpha()])

    if len(str1) + len(str2) == 0:
        return 65536

    product = str1 & str2
    union = str1 | str2

    answer = len(list(product.elements())) / len(list(union.elements()))

    return int(65536 * answer)