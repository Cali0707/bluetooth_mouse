def average(L):
    """Returns the mean of a list."""
    total = 0
    for i in L:
        total += i
    return total / len(L)


if __name__ == '__main__':
    my_list = [10000, 5342, 12, 378, 542]
    print(average(my_list))
