import random
sizes=[5000,8000,10000,13000,15000,18000,20000,23000,25000,28000,30000,35000]
for n in sizes:
    arr_random=[random.randint(-10000,10000)for _ in range(n)]
    k_random=random.choice(arr_random)
    with open(f"random_{n}.txt","w")as f:
        f.write(str(n)+" ")
        f.write(" ".join(str(x)for x in arr_random)+" ")
        f.write(str(k_random))
    arr_asc=list(range(1,n+1))
    k_asc=random.choice(arr_asc)
    with open(f"ascending_{n}.txt","w")as f:
        f.write(str(n)+" ")
        f.write(" ".join(str(x)for x in arr_asc)+" ")
        f.write(str(k_asc))
    arr_desc=list(range(n,0,-1))
    k_desc=random.choice(arr_desc)
    with open(f"descending_{n}.txt","w")as f:
        f.write(str(n)+" ")
        f.write(" ".join(str(x)for x in arr_desc)+" ")
        f.write(str(k_desc))

