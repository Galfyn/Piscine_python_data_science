#!/bin/sh

JQP="/Users/galfyn/goinfre/homebrew/Cellar/jq/1.6/bin/jq"
PROF="${1/ /+}"


curl -k -H 'Content-Type:application/json' -G "https://api.hh.ru/vacancies/?text=$PROF&per_page=20" | $JQP > hh.json
