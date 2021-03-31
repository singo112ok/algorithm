# https://programmers.co.kr/learn/courses/30/lessons/60058
# 괄호 변환
# level2 # 2020 KAKAO BLIND RECRUITMENT


def swap(p):
    resultStr = ""
    for i in range(0, len(p)):   
        if p[i] == '(':
            resultStr += ')'
        else:
            resultStr += '('
    return resultStr

def right(p):
    nLCnt = 0
    nRCnt = 0     
    for i in range(0, len(p)):         
        if p[i] == '(':
            nLCnt += 1
        else:
            nRCnt += 1
        if nLCnt < nRCnt:
            return -1
    else:
        return 0
                


def solution(p):
    answer = ''
    if p == '':
        return answer
    
    nLCnt = 0
    nRCnt = 0   
    
    for i in range(0, len(p)):         
        if p[i] == '(':
            nLCnt += 1
        else:
            nRCnt += 1

        if nLCnt == nRCnt:
            u = p[:i+1]
            v = p[i+1:len(p)]
            
            if right(u) == 0:
                answer = answer+u
                answer = answer+solution(v)   
            else:
                temp = '(' + solution(v) + ')' 
                u = u[1:len(u)-1]
                answer = answer+temp+str(swap(u))    
            break            
        
    return answer


# print(solution('(()())()'))
# print(solution(')('))
print(solution('()))((()'))
# "(()())()"	"(()())()"
# ")("	"()"
# "()))((()"	"()(())()"