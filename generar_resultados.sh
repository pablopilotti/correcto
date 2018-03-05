#! /bin/bash
# ./build/controlbingo/controlbingo -bingos /home/ppilotti/Bingo/cartones/cartones-30000-m03-noclasico-00.txt -sorteo /home/ppilotti/Bingo/sorteos.txt

BINGO_HOME=/home/ppilotti/Bingo/ 

for l in $(ls $1/cartones*.txt)
do
   filename=$(basename "$l")
   $BINGO_HOME/build/controlbingo/controlbingo -bingos $l -sorteo $BINGO_HOME/sorteos.txt > resultado-$filename
done

