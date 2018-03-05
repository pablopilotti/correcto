#! /bin/bash

for l in $(ls $1/cartones*.txt)
do
   ./buscar_repetidos.py -f $l
done
