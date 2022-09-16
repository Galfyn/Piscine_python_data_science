#!/bin/sh

INFILE=../ex02/hh_sorted.csv
OUTFILE=hh_positions.csv

head -1 $INFILE > $OUTFILE
tail -20 $INFILE | \
awk 'BEGIN { FS = OFS = "," }
	{
		STR = ""
		if (index(tolower($3), "junior"))
			STR = STR"Junior/"
		else if (index(tolower($3), "middle"))
			STR = STR"Middle/"
		else if (index(tolower($3), "senior"))
			STR = STR"Senior/"
		else
			STR = "-"
		gsub(/[\/ ]*$/, "", STR)
		$3 = "\""STR"\""
		print
	}' >> $OUTFILE
