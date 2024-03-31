direction = {
    "R": [1, 0],
    "L": [-1, 0],
    "U": [0, 1],
    "D": [0, -1],
}
N, Q = map(int, input().split())
coords = [[i + 1, 0] for i in range(N - 1, -1, -1)]

for _ in range(Q):
    q1, q2 = input().split()
    if int(q1) == 1:
        coords.append(
            [coords[-1][0] + direction[q2][0], coords[-1][1] + direction[q2][1]]
        )
    else:
        # 3のときは[-3]
        print(*coords[-int(q2)])
