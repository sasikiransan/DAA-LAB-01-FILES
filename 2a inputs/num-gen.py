import random
for n in [5000,8000,10000,13000,15000,18000,20000,23000,25000,28000,30000,35000]:
    arr=[random.randint(-10000,10000)for _ in range(n)]
    with open(f"random_{n}.txt","w")as f:
        f.write(str(n)+" ")
        f.write(" ".join(str(x)for x in arr))
