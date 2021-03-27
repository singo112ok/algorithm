# https://programmers.co.kr/learn/courses/30/lessons/49993

# level2
# 쉬운문제 처음엔 필요없는 문자들을 모두 제거 후 스킬 트리에 맞는지 비교해보려 했으나
# 오히려 제거 하는데 시간이 더 걸릴것 같아 변경함
# for else 라는걸 첨 배웠다 맨날 if문해서 마지막 루프까지 돌면 이라는 조건을 줬었는데 
# 더 깔끔하게 하는법 배움 꿀이득



# def findskill(skill, x):
#     if skill.pos(x) > 0:
#         return x

# def solution(skill, skill_trees):
#     answer = 0
#     for i in skill_trees:
#         new_trees.append(list(filter(findskill, i)))
                         
#     for i in new_trees:


# 정답
        
# def solution(skill, skill_trees):
#     answer = 0
    
#     for i in skill_trees:
#         nPos = 0
#         for j in range(0, len(i)):            
#             if skill.find(i[j]) >= 0:
#                 if skill[nPos] == i[j]:
#                     nPos += 1
#                 else:
#                     break
#             if j == len(i)-1:
#                 answer += 1
    
#     return answer

# print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"]))


def solution(skill, skill_trees):
    answer = 0
    
    for i in skill_trees:
        nPos = 0
        for j in range(0, len(i)):            
            if skill.find(i[j]) >= 0:
                if skill[nPos] == i[j]:
                    nPos += 1
                else:
                    break
        else:
            answer += 1
    
    return answer

print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"]))