A, B, C, D = map(int, input().split())
# 1
answer = 0
for i in range(1, D + 1):
    answer += 2 * A + C * (i + 1) + C * (i - 1) + 2 * B
print(answer)
# 2
print(C * D * (D - 1) + 2 * D * (C + B + A))