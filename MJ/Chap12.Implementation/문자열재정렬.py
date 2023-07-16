input = map(str, input())

def solution(input:str=input):

    temp = []
    temp_sum = 0
    for a in input:
        try:
            if int(a) in range(1, 10):
                temp_sum += int(a)
        except:
            temp.append(a)
    
    return ''.join(sorted(temp)) + str(temp_sum)


print(solution())