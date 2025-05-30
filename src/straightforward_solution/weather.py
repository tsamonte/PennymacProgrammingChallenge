def read_weather_data() -> None:
    """
    Script function to read a specific file containing daily weather data and find the smallest
    temperature spread
    """
    try:
        min_day = ''
        min_spread = float('inf')

        with open('./data/w_data.dat') as raw_weather_data:
            data = raw_weather_data.readlines()

        # Filter out non-data lines
        # ASSUMPTION: For data that matters in this problem, col 1 is always a number, col 2 is always MxT, and col 3 is always MnT
        for line in data:
            tokens = line.strip().split()

            if len(tokens) > 0 and tokens[0].isdigit():
                days_max = int(tokens[1].strip('*'))
                days_min = int(tokens[2].strip('*'))
                spread = days_max - days_min
                if spread < min_spread:
                    min_day = tokens[0]
                    min_spread = spread

        print(f'Day with minimum temperature spread: {min_day} (Spread of {min_spread})')

    except FileNotFoundError as fnf:
        print(fnf)
        raise  # ideally would do some other error handling in a larger application, but will just re-raise since it is a simple app
