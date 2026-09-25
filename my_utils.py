import pandas as pd
import sys


def get_column(file_name, query_column, query_value, result_column):
    output = []

    try:
        data = pd.read_csv(file_name)
    except (FileNotFoundError, OSError):
        print(f"Error: could not open '{file_name}'.")
        sys.exit(1)

    for _, row in data.iterrows():
        if row.iloc[query_column] == query_value:
            try:
                output.append(int(row.iloc[result_column]))
            except (ValueError, TypeError):
                print("Error: result could not be converted to an integer.")
                sys.exit(1)

    return output


def mean(array):
    for i in range(len(array)):
        if not isinstance(array[i], (float, int)):
            print("The array contains non-numeric entries.")
            sys.exit(1)
    if len(array) == 0:
        print("This array is empty")
        sys.exit(1)
    else:
        return sum(array) / len(array)


def median(array):
    for i in range(len(array)):
        if not isinstance(array[i], (float, int)):
            print("The array contains non-numeric entries.")
            sys.exit(1)
    if len(array) == 0:
        print("This array is empty")
        sys.exit(1)
    else:
        midpoint = len(array) // 2
        if len(array) % 2 == 1:
            return sorted(array)[midpoint]
        else:
            return (sorted(array)[midpoint-1] + sorted(array)[midpoint]) / 2


def std(array):
    for i in range(len(array)):
        if not isinstance(array[i], (float, int)):
            print("The array contains non-numeric entries.")
            sys.exit(1)
    if len(array) == 0:
        print("This array is empty")
        sys.exit(1)
    else:
        return (sum([(value - mean(array)) ** 2 for value in array])
                / len(array)) ** 0.5
