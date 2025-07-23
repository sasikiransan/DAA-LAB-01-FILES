import random
import string

sizes=[5000,10000,15000,20000,25000,30000,35000]
letters=list(string.ascii_uppercase+string.ascii_lowercase)  # A-Z then a-z
for n in sizes:
    # Random letters
    arr_random=[random.choice(letters) for _ in range(n)]
    with open(f"random_{n}.txt","w")as f:
        f.write(str(n)+" ")
        f.write(" ".join(arr_random))

    # Ascending letters (A-Z a-z repeated)
    arr_asc=(letters*((n//len(letters))+1))[:n]
    with open(f"ascending_{n}.txt","w")as f:
        f.write(str(n)+" ")
        f.write(" ".join(arr_asc))

    # Descending letters (z-a Z-A repeated)
    arr_desc=(letters[::-1]*((n//len(letters))+1))[:n]
    with open(f"descending_{n}.txt","w")as f:
        f.write(str(n)+" ")
        f.write(" ".join(arr_desc))
