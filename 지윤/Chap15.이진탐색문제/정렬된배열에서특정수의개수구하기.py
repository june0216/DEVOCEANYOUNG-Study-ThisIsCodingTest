from bisect import bisect_left, bisect_right

def count_by_value(array, left_value, right_value):
    right_value = bisect_right(array, right_value) # 정렬된 순서를 유지하면서 리스트 a에 데이터 x를 삽입할 가장 오른쪽 인덱스
    left_value = bisect_left(array, left_value)
    return right_value - left_value

n,x  = map(int, input().split())
array = list(map(int, input().split()))

count = count_by_value(array, x, x)
if count == 0:
    print(-1)
else:
    print(count)
