def get_column(file_name, query_column, query_value, result_column):
    from pandas import read_csv
    
    output = []
    data = read_csv(file_name)
    for idx, line in data.iterrows():
        if line[query_column] == query_value:
            output.append(line[result_column])

    return output