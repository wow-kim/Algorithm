def solution(phone_book):
    
    phone_book = sorted(phone_book, key=lambda x: len(x))

    i = 0
    for p in phone_book:
        i += 1
        if i == len(phone_book): 
            return True

        def cut(number):
            number = number[:len(p)]
            return number

        comp = phone_book[i:]
        cutted = list(map(cut, comp))

        if p in cutted:
            return False
        
#--------------------------------------------------

def solution(phone_book):
    answer = True
    hash_map = {}
    for phone_number in phone_book:
        hash_map[phone_number] = 1
    for phone_number in phone_book:
        temp = ""
        for number in phone_number:
            temp += number
            if temp in hash_map and temp != phone_number:
                answer = False
    return answer