from __future__ import unicode_literals


data = []
for _ in range(6):
    row = raw_input()
    data.append([int(c) for c in row.split()])


sums = []
for i in range(4):
    for j in range(4):
        hourglass_sum = sum(data[i][j:j + 3])
        hourglass_sum += data[i + 1][j + 1]
        hourglass_sum += sum(data[i + 2][j:j + 3])
        sums.append(hourglass_sum)

print max(sums)
