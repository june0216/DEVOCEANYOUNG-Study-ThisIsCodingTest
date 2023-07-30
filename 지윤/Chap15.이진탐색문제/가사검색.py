from bisect import bisect_left,bisect_right
def count_by_range(a, left_value, right_value):
    right_value = bisect_right(a, right_value)
    left_value = bisect_left(a, left_value)
    return right_value - left_value
array = [[] for _ in range(10001)]
reversed_array = [[]for _ in range(10001)]

def solution(words, queries):
    answer = []
    for word in words:
        array[len(word)].append(word)
        reversed_array[len(word)].append(word[::-1]) #단어를 뒤집어서 삽입
    for i in range(10001): #이진 탐색을 위한 단어 정렬
        array[i].sort()
        reversed_array[i].sort()
    for q in queries:
        if q[0] != '?': #접미사에 붙은 경우
            res = count_by_range(array[len(q)], q.replace('?', 'a'), q.replace('?', 'z'))
        else:
            res = count_by_range(reversed_array[len(q)], q[::-1].replace('?', 'a'), q[::-1].replace('?', 'z'))
        answer.append(res)

    return answer