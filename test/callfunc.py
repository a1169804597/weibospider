from greenGiant.tasks import add
import time


t1 = time.time()

r1 = add.delay(1, 2)
r2 = add.delay(2, 5)
r3 = add.delay(4, 25)
r4 = add.delay(1, 2)
r5 = add.delay(11, 21)


r_list = [r1, r2, r3, r4, r5]

print("start tasks")

for r in r_list:
    while not r.ready():
        pass
    print(r.result)

t2 = time.time()
print(f"共耗时：{int(t2 - t1)}")
