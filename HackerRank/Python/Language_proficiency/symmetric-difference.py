m = int(input())
a = set(map(int, input().split()))
n = int(input())
b = set(map(int, input().split()))
a.symmetric_difference_update(b)
print(*sorted(a), sep='\n')
