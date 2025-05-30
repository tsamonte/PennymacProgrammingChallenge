import sys
from straightforward_solution import weather, soccer
from alternative_solution import calculate

def main():
    # if 'alt' arg passed in, run alternative solution
    if len(sys.argv) >= 2 and sys.argv[1] == 'alt':
        print("Running alternative solution:")
        calculate.calculate_minimum_weather_spread('./data/w_data.dat')
        calculate.calculate_minimum_score_difference('./data/soccer.dat')

    # else run straightforward solution
    else:
        print("Running straightforward solution")
        weather.read_weather_data()
        soccer.read_soccer_data()


if __name__ == '__main__':
    main()
