# https://programmers.co.kr/learn/courses/30/lessons/42583

# 문제 설명
# 트럭 여러 대가 강을 가로지르는 일 차선 다리를 정해진 순으로 건너려 합니다. 모든 트럭이 다리를 건너려면 최소 몇 초가 걸리는지 알아내야 합니다. 트럭은 1초에 1만큼 움직이며, 다리 길이는 bridge_length이고 다리는 무게 weight까지 견딥니다.
# ※ 트럭이 다리에 완전히 오르지 않은 경우, 이 트럭의 무게는 고려하지 않습니다.

# 난이도 : Level2


def solution(bridge_length, weight, truck_weights):
    
    lBridge = []
    answer = 0    
    nSum = 0
    
    for i in range(bridge_length):
        lBridge.append(0)
        
    while(True):
        answer += 1
        lBridge.pop(0)
        if len(lBridge) == 0:
            break            
        elif len(truck_weights) == 0:
            continue
        if sum(lBridge) + truck_weights[0] < weight:
            lBridge.append(truck_weights[0])
            truck_weights.pop(0)
        else:
            lBridge.append(0)   
    
    return answer        

solution(100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10])