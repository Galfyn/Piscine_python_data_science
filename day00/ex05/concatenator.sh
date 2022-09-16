#!/bin/sh

OUTFILE=hh_concatenator.csv

echo "\"id\",\"created_at\",\"name\",\"has_test\",\"alternate_url\"" > $OUTFILE

cat 20*.csv | sed -En '/^"id\",\"created_at\",\"name\",\"has_test\",\"alternate_url\"$/!p' >> $OUTFILE
