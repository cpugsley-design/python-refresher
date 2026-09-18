import argparse
from my_utils import get_column

parser = argparse.ArgumentParser(
                description='Print fire counts for a specified country.',
                prog='print_fires')

parser.add_argument('--country',
                    type=str,
                    help='Name of the country',
                    required=True)

parser.add_argument('--country_column',
                    type=int,
                    help='Index of the country column (0)',
                    required=True)

parser.add_argument('--fires_column',
                    type=int,
                    help='Index of the fires column (2 or 3)',
                    required=True)

parser.add_argument('--file_name',
                    type=str,
                    help='Name of the file (Agrofood_co2_emission.csv)',
                    required=True)

args = parser.parse_args()

def main():
    country='United States of America'
    country_column = args.country_column
    fires_column = args.fires_column
    file_name = args.file_name
    fires = get_column(file_name = file_name, 
                       query_column = country_column, 
                       query_value = country, 
                       result_column = fires_column)
    print(fires)

if __name__ == "__main__":
    main()
