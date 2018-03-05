#! /bin/bash
# Sorteo: 4892 Bolillas cantadas: 54 Ganadores: 3 Estadisticas: 0 1 1 20 128 525 1530 3121 5006 6127 5159 3319 1535 443 82 3 27000 Cartones: 35234 9818 18203

# bollillas cantadas
awk -v max=0 '{if($5>max){max=$5; want=$2}}END{print "Bolillas cantadas: Max: " max " en el sorteo: " want} ' $1
awk -v min=100000 '{if($5<min){min=$5; want=$2}}END{print "Bolillas cantadas: Min: " min " en el sorteo: " want} ' $1
awk '{delta = $5 - avg; avg += delta / NR; mean2 += delta * ($5 - avg); } END { print "Bolillas cantadas: pro: " avg " stdev:"sqrt(mean2 / NR); }' $1
# ganadores
awk -v max=0 '{if($7>max){max=$7; want=$2}}END{print "Ganadores: Max: " max " en el sorteo: " want} ' $1
awk '{delta = $7 - avg; avg += delta / NR; mean2 += delta * ($7 - avg); } END { print "Ganadores: pro: " avg " stdev:"sqrt(mean2 / NR); }' $1
#awk -v min=100000 '{if($5<min){min=$5; want=$2}}END{print "Min bolillas cantadas: " min " en el sorteo: " want} ' $1
