#!/bin/sh

INFILE=../ex03/hh_positions.csv
OUTFILE=hh_uniq_positions.csv


echo "\"name\"","\"count\"" > $OUTFILE
(tail -20 $INFILE | \
awk 'BEGIN { FS = OFS = "," }
	{
		if (index($3, "Junior"))
			J++
		if (index($3, "Middle"))
			M++
		if (index($3, "Senior"))
			S++
	}
	END { print "\"Junior\"", J \
		"\n\"Middle\"", M \
		"\n\"Senior\"", S} ') | \
	sort -t',' -nk2 >> $OUTFILE 
