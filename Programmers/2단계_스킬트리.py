def solution(skill, skill_trees):
    
    def find_index(tree):
        skill_index = []
        for s in skill:
            skill_index.append(tree.find(s))

        no = 0
        for i in skill_index:
            if i == -1:
                no = 1
            if no == 1 and i != -1:
                return False

        skill_index = [i for i in skill_index if i >= 0 ]

        if skill_index != sorted(skill_index):
            return False

        return True

    return sum(list(map(find_index, skill_trees)))

answer = solution("CBD",["BACDE", "CBADF", "AECB", "BDA"])
print(answer)