#ifndef BINGO_H
#define BINGO_H
#include <carton.h>
#include <map>
#include <string.h>

class Bingo
{
public:
    Bingo();
    ~Bingo();
    std::vector<Carton*> cartones;
    std::vector<unsigned> cantados;
    std::map<unsigned,std::vector<Carton*> > control;

    bool cantar(unsigned bolilla);
    bool deshacer_cantar(unsigned bolilla);
    bool cargar_cartones(char*);
    void estadistica();
    void estadistica2();
};

#endif // BINGO_H

