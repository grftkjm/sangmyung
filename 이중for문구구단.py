for i in range(1,10):
    if i == 1:
        for j in range(2, 10):
            print("# ",j,"단 #", end="\t")
        print()

    for j in range(2,10):
        print(j, "X", i, "=", j*i, end="\t")
    print()