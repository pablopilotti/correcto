#! /bin/sh
for i in 27000 28000 29000 30000
do
    for j in 02 03
    do
        for k in 00 01 02 03 04 05
        do
            ./generar_cartones.py -c $i -m $j    > cartones-$i-m$j-clasico-$k.txt
            ./generar_cartones.py -c $i -m $j -n > cartones-$i-m$j-noclasico-$k.txt
        done
    done
done
exit



