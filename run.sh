#!/bin/bash

# This script should run with no errors
python print_fires.py --file_name Agrofood_co2_emission.csv --country USA --country_column 0 --fires_column 3

# This script will return a file error (file_name misspelled)
python print_fires.py --file_name Agrofood_co2_emissions.csv --country USA --country_column 0 --fires_column 3

# This script will return a value error for the index of the country column
python print_fires.py --file_name Agrofood_co2_emissions.csv --country USA --country_column 0.1 --fires_column 3