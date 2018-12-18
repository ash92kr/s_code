pool = [i for i in range(1, 46)]

import random
# lotto = random.sample(pool, 6)

lotto = []
for i in range(6):
    a = random.choice(pool)
    


print(lotto)

for i in range(len(lotto)):
    for j in range(len(lotto)+i):
        if lotto[i] == lotto[j]:
            lotto.remove(j)

print(lotto)