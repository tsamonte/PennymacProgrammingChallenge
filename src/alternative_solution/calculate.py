def _read_relevant_data(filename: str) -> []:
    """
    Reads a file, filters out any unnecessary lines, and returns a tokenized matrix of data
    :param filename: file location
    :return: matrix array representing relevant data from the file
    """
    try:
        with open(filename) as raw_data:
            data = raw_data.readlines()

        # .replace() will target removing the ' - ' between the 'F' and 'A' columns in soccer.dat to avoid index issues
        return [line.strip().replace(' - ', '').split() for line in data if not line.isspace()]

    except FileNotFoundError as fnf:
        print(fnf)
        raise # ideally would do some other error handling in a larger application, but will just re-raise since it is a simple app

def _find_column_indexes(data: [], id_column_name: str, value_column_name_1: str, value_column_name_2: str) -> ():
    """
    Finds and returns the index of each column we are searching for.
    Removes some assumptions from the straightforward solution, such as assuming columns will always be in the same position
    :param data: matrix array of relevant data
    :param id_column_name: Column header name of values uniquely identfiying a row ('Dy' or 'Team' for our case)
    :param value_column_name_1: Column header name of first value ('MxT' or 'F' for our case)
    :param value_column_name_2: Column header name of the second value ('MnT' or 'A' for our case)
    :return: 3-tuple of int values, representing the index position of each column we want to look at
    """
    for line in data:
        if line[0] == id_column_name:
            return (line.index(id_column_name), line.index(value_column_name_1), line.index(value_column_name_2))

    return ()

def _find_min_difference(data: [], indexes: (), offset=0) -> (str, int):
    """

    :param data: matrix array of relevant data
    :param indexes: 3-tuple of int values, representing the index position of each column of interest in the data
    :param offset: int value representing how much to offset the index, used if there are leading columns with no header
    :return: 2-tuple; first value being the identifier of the row with min difference, and the second being the min difference
    """
    min_id = ''
    min_difference = float('inf')

    for line in data:
        # Only considers lines with relevant data
        # Handles both data layouts: For soccer.dat, the first column with list number isn't needed and also doesn't have a column header, so we'd need to offset by 1
        if len(line) > 0 and line[0].strip('.').isdigit():
            val1 = int(line[indexes[1]+offset].strip('*'))
            val2 = int(line[indexes[2]+offset].strip('*'))
            difference = abs(val1 - val2)
            if difference < min_difference:
                min_id = line[indexes[0]+offset]
                min_difference = difference

    return (min_id, min_difference)

def calculate_minimum_weather_spread(filename: str) -> None:
    """
    Reads a specific file containing daily weather data and find the smallest
    temperature spread
    :param filename: file location
    """
    data = _read_relevant_data(filename)
    indexes = _find_column_indexes(data, 'Dy', 'MxT', 'MnT')
    results = _find_min_difference(data, indexes)
    print(f'Day with minimum temperature spread: {results[0]} (Spread of {results[1]})')

def calculate_minimum_score_difference(filename: str) -> None:
    """
    Reads the specified file containing English Premiere League data and find the
    minimum difference between "for" and "against" goals
    :param filename: file location
    """
    data = _read_relevant_data(filename)
    indexes = _find_column_indexes(data, 'Team', 'F', 'A')
    results = _find_min_difference(data, indexes, offset=1)
    print(f'Team with minimum score difference: {results[0]} (Difference of {results[1]})')
