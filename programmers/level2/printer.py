# https://programmers.co.kr/learn/courses/30/lessons/42587

def solution(priorities, location):
    nNowPos = location
    answer = 1
    
    while True:
        nTemp = priorities.pop(0)
        if len(priorities) == 0:
            break
            
        if nTemp >= max(priorities):
            if nNowPos == 0:
                break
            else:
                nNowPos -= 1
                if nNowPos < 0:
                    nNowPos = len(priorities)
            answer += 1
        else:
            priorities.append(nTemp)  
            nNowPos -= 1
            if nNowPos < 0:
                nNowPos = len(priorities)-1
    
    return answer

solution([2, 1, 3, 2],2)    


# from collections import deque

# def solution(priorities, location):
#     dpriorities = deque(priorities)
#     nNowPos = location
#     answer = 1
    
#     while True:
#         nTemp = dpriorities.popleft()
#         if len(dpriorities) == 0:
#             break
            
#         if nTemp >= max(dpriorities):
#             if nNowPos == 0:
#                 break
#             else:
#                 nNowPos -= 1
#                 if nNowPos < 0:
#                     nNowPos = len(dpriorities)
#             answer += 1
#         else:
#             dpriorities.append(nTemp)  
#             nNowPos -= 1
#             if nNowPos < 0:
#                 nNowPos = len(dpriorities)-1
    
#     return answer