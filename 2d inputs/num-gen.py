import random

sizes = [5000, 10000, 15000, 20000, 25000, 30000, 35000]

for n in sizes:
    # Random numbers
    arr_random = [random.randint(-1000, 1000) for _ in range(n)]
    with open(f"random_{n}.txt", "w") as f:
        f.write(str(n) + " ")
        f.write(" ".join(map(str, arr_random)))

    # Ascending numbers
    arr_asc = sorted(random.randint(-1000, 1000) for _ in range(n))
    with open(f"ascending_{n}.txt", "w") as f:
        f.write(str(n) + " ")
        f.write(" ".join(map(str, arr_asc)))

    # Descending numbers
    arr_desc = sorted((random.randint(-1000, 1000) for _ in range(n)), reverse=True)
    with open(f"descending_{n}.txt", "w") as f:
        f.write(str(n) + " ")
        f.write(" ".join(map(str, arr_desc)))
