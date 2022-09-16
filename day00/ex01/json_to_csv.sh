#!/bin/sh

CONVERT=../ex00/hh.json

jq -rf filter.jq $CONVERT > hh.csv

