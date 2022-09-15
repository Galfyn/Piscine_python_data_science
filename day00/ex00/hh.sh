#!/bin/sh

JQP="/Users/galfyn/goinfre/homebrew/Cellar/jq/1.6/bin/jq"

curl -k -H 'Content-Type:application/json' -G "https://api.hh.ru/vacancies/?text=data%20scientist&page=1&per_page=20" | $JQP > hh.json
