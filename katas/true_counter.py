def count_true_values(array):
    count = 0
    for value in array:
        if value is True:
            count+=1
    return count

    return 0


if __name__ == '__main__':
    sample_array = [True, False, True, True, False]
    true_count = count_true_values(sample_array)
    print(true_count)  # 3 should be printed