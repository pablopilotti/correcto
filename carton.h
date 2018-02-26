#ifndef CARTON_H
#define CARTON_H
#include<vector>

class Carton
{
public:
    Carton(unsigned id);
    void clear();
    unsigned add(unsigned number);
    unsigned mark(unsigned);
    unsigned unmark(unsigned);
    std::vector<unsigned> _numbers;
    unsigned _marked;
    unsigned _id;
private:


};

#endif // CARTON_H
