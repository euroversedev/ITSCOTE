''' [문제] 모험가 길드 '''

N = int(input())
array = list(map(int, input().split()))
array.sort()

i = 0
count = 0
while True:
    i = i + array[i]
    if N <= i: break
    count +=1
print(count)

''' [review]
최대한 많은 수의 그룹
=> 공포도가 큰 애는 마을에 그대로 남아 있어도 되므로,
=> 우선 공포도가 작은 애들끼리 최대한 그룹을 만들어볼까?
=> 공포도를 오름차순 정렬해서 그룹 만들면 되겠다.
=> O(N)

정렬을 위해 array = array.sort 라고 적었다.
sort에 괄호를 생략하면 오류난다.

sorted 함수는 원형을 변형하지 않고 정렬된 결과를 반환하므로
array = sorted(array)와 같이 사용하지만,
리스트의 내장함수인 sort()는 원형을 변형하므로 반환해서 사용하지 않는다.
'''