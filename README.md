# json2csv

The goal of this Python project is to extract process, voltage, temperature, and timing information from cell libraries in .json format, and write it to a .csv file.

Namely, and strictly:
* 'nom_voltage',
* 'nom_temperature',
* 'nom_process',
* 'related_pin',
* 'timing_type',
* 'index1' (output_load),
* 'index2' (input_slope),
* 'values' (value),
* and cell archs of types 'cell_rise', 'rise_transition', 'cell_fall', 'fall_transition'.

Any cells with formats that violate such format will fail to output  the .csv file. For example, in ./in/:
> ANTENNA_RVT, BUSKP_RVT, CLOAD1_RVT, DCAP_RVT, DFFSSRX1_RVT, DFFSSRX2_RVT, DHFILLH2_RVT, DHFILLHLHLS11_RVT, NMT1_RVT, NMT2_RVT, NMT3_RVT, PMT1_RVT, PMT2_RVT, PMT3_RVT, SDFFSSRRX1_RVT, SDFFSSRX2_RVT, SHFILL128_RVT, SHFILL1_RVT, SHFILL2_RVT, SHFILL3_RVT, SHFILL64_RVT, TIEH_RVT, TIEL_RVT

## Usage
```
usage: main.py [-h] [-cellname CELLNAME] [--jsondir JSONDIR] [--csvdir CSVDIR] [--display DISPLAY]

convert cell library .json to .csv

optional arguments:
    -h, --help          show this hellp message and exit
    --cellname CELLNAME cell-name to extracting information OR key in 'ALL' to extract all at once
    --jsondir  JSONDIR  directory path to input json file(s)
    --csvdir   CSVDIR   directory path to output csv file(s)
    --display  DISPLAY  \'ON\': display on, all else: display off
```