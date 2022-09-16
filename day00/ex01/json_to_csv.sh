#!/bin/sh

CONVERT=../ex00/hh.json
JQP="/Users/galfyn/goinfre/homebrew/Cellar/jq/1.6/bin/jq"

$JQP -rf filter.jq $CONVERT > hh.csv

