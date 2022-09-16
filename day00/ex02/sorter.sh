#!/bin/sh

INFILE=../ex01/hh.csv

head -1 $INFILE > hh_sorted.csv;
tail -20 $INFILE | sort -t"," -k2 -k1  >> hh_sorted.csv;
