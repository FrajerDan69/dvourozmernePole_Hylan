arraya=[
    [1,69,43],
    [2,70,44],
    [3,71,46]
]
for row in arraya:
    print(row)

arraya[1][1] = 105

new_row = [4, 72, 47, 100]
for i in range(len(arraya)):
    arraya[i].append(100)
arraya.append(new_row)

for row in arraya:
    print(row)
