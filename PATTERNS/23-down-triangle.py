for x in range(5):          # range is 5
    #for y in range(x, 5):   # x is the start range
    for y in range(5 - x):  # this also works
        print("*", end=' ')
    print()