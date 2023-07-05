def fib(num1: int, num2: int, terms: int):
    """Contents will take time to appear if ran in backed up folder e.i. onedrive.
    For immediate results, run elsewhere e.g. C:/"""
    temp1 = num1
    temp2 = num2
    with open("fibonacci.txt", "w") as f:
        f.write(str(num1) + ", " + str(num2) + ", ")
        for x in range(terms):
            term = temp1 + temp2
            if x < terms -1:
                f.write(str(term) + ", ")
            else:
                f.write(str(term))
            temp1 = temp2
            temp2 = term


fib(0, 1, 10)
