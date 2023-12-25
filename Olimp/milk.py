file = open(r'G:\1Проекты\ОМГТУ\Practika_Omgtu\Olimp\Упаковки молока\input10.txt', mode='r')
n = int(file.readline())
a = [1000, 1000]
for i in range(1, n + 1):
    x1, y1, z1, x2, y2, z2, c1, c2 = map(float, file.readline().split())
    V1 = x1 * y1 * z1 / 1000
    V2 = x2 * y2 * z2 / 1000
    S1 = 2 * (x1 * y1 + x1 * z1 + y1 * z1)
    S2 = 2 * (x2 * y2 + x2 * z2 + y2 * z2)
    M = round(abs((S2 * c1 / S1 - c2) / (S2 * V1 / S1 - V2)), 2)
    if a[1] > M:
        a = [i, M]
print(*a)
file.close()