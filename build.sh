#!/bin/bash

for makefile in $(ls */Makefile); do
    echo "building $makefile"
    (cd $(dirname "$makefile") && make)
done
