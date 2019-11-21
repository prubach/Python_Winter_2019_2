def sum_row(row):
    if row == 1:
        return 1
    else:
        return sum_row(row - 1) + row


print(sum_row(5))
print(sum_row(7))