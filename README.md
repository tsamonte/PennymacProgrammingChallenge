#    PennymacProgrammingChallenge

## The challenge:
1. In the attached file (w_data.dat), you’ll find daily weather data. Download this text file, then write a program to output the day number (column one) with the smallest temperature spread (the maximum temperature is the second column, the minimum the third column).
2. The attached soccer.dat file contains the results from the English Premier League. The columns labeled ‘F’ and ‘A’ contain the total number of goals scored for and against each team in that season (so Arsenal scored 79 goals against opponents, and had 36 goals scored against them). Write a program to print the name of the team with the smallest difference in ‘for’ and ‘against’ goals

## About My Solution
With the proposed challenge, I initially implemented a program that takes a [straightforward approach](https://github.com/tsamonte/PennymacProgrammingChallenge/tree/master/src/straightforward_solution), writing a single function for each question that handles everything: the file reading, the data filtering, the calculations, etc. All with assumptions that the data will always be given as presented in the provided files. 


While this approach gives the expected solution, I also wanted to provide an [alternative solution](https://github.com/tsamonte/PennymacProgrammingChallenge/tree/master/src/alternative_solution) for a few reasons:
1. The problems are very similar, with a lot of repeating code, so I wanted to make reusable functions that work for both problems, and could handle other problems with similar structures
2. I believe breaking down functionality into separate functions is better practice than everything being implemented within one large function, as it allows for better readability and easier debugging
3. I wanted to minimize the amount of assumptions I made with the implementation, having functionality that considered things like columns being in a different order or if we wanted to compare different columns than the ones requested

Each approach has it's tradeoffs
- The straghtforward approach of packing everything into one function is not best practice, but it only iterates through the lines exactly once
- The alternative approach of splitting into multiple functions results in having to iterate through the data multiple times. Although time complexity is still linear, this is technically a bit slower
- However, the alternative solution also has better readability and more closely follows best practices. The separate functions are implemented with reusability in mind, and can likely be used with other problems/data of similar structure.
  
## Running My Solution

#### Prerequisites
This program requires Python 3 to run. Optionally, "make" can be utilized as well to run through the provided makefile

#### Installation
    git clone https://github.com/tsamonte/PriceDropChecker

## Usage
This project runs directly on the command line.

#### Straightforward solution
A makefile is provided for easy setup. To create a virtual environment and run the straightforward solution of the project, run the following command:
  
    make run
    
  If not using make, run with the Python command from the root of the project:
    
    python src/main.py
    
#### Alternative solution
Alternatively, to run using the alternative solution, run one of the following commands:

    make run-alt
  
  Or

    python src/main.py alt
