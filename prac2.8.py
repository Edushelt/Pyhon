# Multiplicaion table from 1 to n (1, n+1)
for i in range(1, 11):
    for j in range(1, 11):
        print(f"{i * j:4}", end='')
    print() # Newline after each row