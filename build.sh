#!/bin/bash

for makefile in $(find . -name "Makefile"); do
    echo "makefile $makefile"
    (cd $(dirname "$makefile") && make)
done
