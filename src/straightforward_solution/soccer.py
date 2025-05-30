def read_soccer_data() -> None:
    """
    Script function to read a specific file containing English Premiere League data and find the
    minimum difference between "for" and "against" goals
    """
    try:
        min_team = ''
        min_difference = float('inf')

        with open('./data/soccer.dat') as raw_soccer_data:
            data = raw_soccer_data.readlines()

        # Filter out non-data lines
        # ASSUMPTION: For data that matters in this problem, data is formatted consistently and correctly
        #   Col 1 is a list number; Team Name, 'F' and 'A' columns are always in the same position
        for line in data:
            tokens = line.strip().split()

            if len(tokens) > 0 and tokens[0].strip('.').isdigit():
                for_score = int(tokens[6])
                against_score = int(tokens[8])
                difference = abs(for_score - against_score)
                if difference < min_difference:
                    min_team = tokens[1]
                    min_difference = difference

        print(f'Team with minimum score difference: {min_team} (Difference of {min_difference})')

    except FileNotFoundError as fnf:
        print('fnf')
        raise # ideally would do some other error handling in a larger application, but will just re-raise since it is a simple app
