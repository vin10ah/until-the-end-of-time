nk = input().split()
n, k = int(nk[0]), int(nk[1])

score = list(map(int, input().split()))
score.sort()
print(score[-k])