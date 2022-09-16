#!/bin/sh

INFILE=../ex01/hh.csv

head -n 1 $INFILE > hh_sorted.csv;
tail -n +2 $INFILE | sort -t, -k2 -k1 >> hh_sorted.csv;
