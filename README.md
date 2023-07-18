# JWS2CSV

### Note : This is made for JASCO V-630 spectrophotometer. It may work with other models but I have not tested it.

## Description
This is a copy of the original JWS2CSV tool by [jftran](https://github.com/jzftran/jws2txt) with a few modifications to make it work with python 3.6 or higher.

A simple tool to convert (Jasco) JWS files to CSV files.


The JWS file format is used by the Jasco V series spectrophotometer. The data is saved in a OLE2 file format. This tool extracts the data and saves it in a CSV file. You can then use the CSV file in your favorite data analysis tool.

Each JWS file is divided into 14 blocks the most important ones are:
- Block 4: Contains the sample information
- Block 5: Contains the information about the measurement e.g. wavelength range, range of the x-axis, channel number, etc.
- Block 6: Contains the y data

If you want to have a look at the data in the JWS file, you can use a olefile viewer. For example [mvole](https://mvole.sourceforge.net/). or using the python library olefile.

If you use mvole you can extract a perticular block by typing in
```
mvole -e <filename> <block number> -f <JWS file>
```

Then you can use any hex editor to view the data. For example [HxD](https://mh-nexus.de/en/hxd/).

The y data is saved as a 32 bit signed float. The x data is calculated from the information in block 5.

As it is not necessary to save the x-data it is not saved in the file, the x-data is calculated from the information in block 5.

## Requirements
- Python 3.6 or higher
- olefile

## Usage
Just create 2 folders, one called "JWS" for the JWS files and one called "CSV" for the CSV files. Then put the JWS files in the JWS folder and run the script. The CSV files will be saved in the CSV folder.

One the files have been copied then run the main.py script. 

```
python main.py
```

The script will then convert all the JWS files in the JWS folder to CSV files and save them in the CSV folder.

The script will add 5 header lines to the CSV file. The header lines contain the following information:
- Sample name
- Comment
- Filename
- X axis label and Y axis label
- X axis units and Y axis units
