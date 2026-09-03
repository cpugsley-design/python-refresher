def get_column(file_name, query_column, query_value, result_column = 1):
    from pandas import read_csv
    
    output = []
    data = read_csv(file_name)
    for idx, line in data.iterrows():
        if type(query_column) == int:
            if line.iloc[query_column] == query_value:
                if type(result_column) == int:
                    output.append(line.iloc[result_column])
                else:
                    output.append(line[result_column])
        else:
            if line[query_column] == query_value:
                if type(result_column) == int:
                    output.append(line.iloc[result_column])
                else:
                    output.append(line[result_column])

    return output