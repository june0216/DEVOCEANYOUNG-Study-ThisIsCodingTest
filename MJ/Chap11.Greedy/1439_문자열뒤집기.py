input = input()

def solution(input:str=input):
    
    curr = input[0]
    count = 1
    for a in input:
        if a != curr:
            curr = a
            count += 1
    return count // 2

print(solution())