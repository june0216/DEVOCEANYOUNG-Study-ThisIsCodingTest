i=0

count=0

group=0

N=int(input())

array=list(map(int,input().split()))

array.sort()
for i in array:

    count=count+1

    if count>=array[i]:

        group=group+1

        count=0

    

print(group)