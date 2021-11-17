def more_than_50(number):
    if number % 2 == 1 and number > 50:
        return True
    else:
        return False


numbers = [0, 99, 100, 53, 44, 23, 4, 8, 16, 15, 77, 51]
print(list(filter(more_than_50, numbers)))