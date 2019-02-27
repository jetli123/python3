#!/bin/bash

for i in $@
do
    if [ "$i" -eq 12 ];then
        echo "success!"
        exit 10
    else
        echo "failed"
        exit 103
    fi
done
