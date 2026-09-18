import pandas as pd


def get_column(file_name, query_column, query_value, result_column):
    output = []

    try:
        data = pd.read_csv(file_name)
    except (FileNotFoundError, OSError):
        print(f"Error: could not open '{file_name}'.")
        return []

    for _, row in data.iterrows():
        if row.iloc[query_column] == query_value:
            try:
                output.append(int(row.iloc[result_column]))
            except (ValueError, TypeError):
                print("Error: result could not be converted to an integer.")
                return []

    return output
