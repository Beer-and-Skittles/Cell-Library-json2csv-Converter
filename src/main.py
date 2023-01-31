import argparse
from json2csv import json2csv

parser = argparse.ArgumentParser(description='convert .json to .csv')
parser.add_argument('--cellname', type=str, default='ALL', help='cell-name for extracting individual cell information OR key in \'ALL\' to extract all at once')
parser.add_argument('--jsondir', type=str, default='./in/', help='directory path to input json file(s)')
parser.add_argument('--csvdir', type=str, default='./out/', help='directory path to output csv file(s)')
parser.add_argument('--display', type=str, default='', help='\'ON\': display on, all else: display off')
args = parser.parse_args()

json2csv(
    cell = args.cellname,
    input_path = args.jsondir,
    output_path = args.csvdir,
    display = (args.display=='ON')
)
