import argparse
from json2csv import json2csv

parser = argparse.ArgumentParser(description='convert cell library .json to .csv')
parser.add_argument('--cellname', type=str, default='AND2X1_RVT', help='cell-name to extracting information OR key in \'ALL\' to extract all at once')
parser.add_argument('--jsondir', type=str, default='./in/', help='directory path to input json file(s)')
parser.add_argument('--csvdir', type=str, default='./out/', help='directory path to output csv file(s)')
parser.add_argument('--display', type=str, default='ON', help='\'ON\': display on, all else: display off')
parser.add_argument('--iterations', type=int, default=0, help='iterations of data augmentation')
args = parser.parse_args()

json2csv(
    cell = args.cellname,
    input_path = args.jsondir,
    output_path = args.csvdir,
    display = args.display,
    iterations = args.iterations
)
