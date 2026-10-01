#!/bin/bash

test -e ssshtest || wget -q https://raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest
. ssshtest

run invalid_column python print_fires.py --country Sweden --country_column h --fires_column 3 --file_name raw_data_test.csv
assert_exit_code 2

run argument_missing python print_fires.py --country_column 0 --fires_column 3 --file_name raw_data_test.csv
assert_exit_code 2

run file_missing python print_fires.py --country Sweden --country_column 0 --fires_column 3 --file_name invalid_file_name.csv
assert_exit_code 1

run basic_test python print_fires.py --country Sweden --country_column 0 --fires_column 3 --file_name raw_data_test.csv
assert_exit_code 0
assert_in_stdout [
assert_in_stdout ]

run mean_test python print_fires.py --country Sweden --country_column 0 --fires_column 3 --file_name raw_data_test.csv --calculation mean
assert_exit_code 0
assert_stdout

run median_test python print_fires.py --country Sweden --country_column 0 --fires_column 3 --file_name raw_data_test.csv --calculation median
assert_exit_code 0
assert_stdout

run std_test python print_fires.py --country Sweden --country_column 0 --fires_column 3 --file_name raw_data_test.csv --calculation std
assert_exit_code 0
assert_stdout
