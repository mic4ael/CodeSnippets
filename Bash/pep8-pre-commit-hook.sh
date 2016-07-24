#!/bin/sh

set -e;

if [[ `which pep8 > /dev/null` -ne 0 ]];
then
    echo "PEP8 not installed";
    echo "Skipping the check";
    exit 0;
fi;

for MODIFIED_FILE in `git status --porcelain | cut -d " " -f3`;
do
    if [[ `file $MODIFIED_FILE` = 'a python script text executable' ]]
    then
        exec pep8 --max-line-length=120 $MODIFIED_FILE;
    fi;
done;
