# data_op.py

data = [5, 3, 8, 5, 2, 8, 9, 1]


def remove_duplicates(data):
    return list(set(data))


def sort_data(data):
    return sorted(data)


def stats(data):
    return max(data), min(data), sum(data)/len(data)


if __name__ == "__main__":
    print("Original:", data)
    print("No Duplicates:", remove_duplicates(data))
    print("Sorted:", sort_data(data))
    print("Max, Min, Avg:", stats(data))
