#ifndef CARTON_H
#define CARTON_H
#include<vector>

class Carton
{
public:
    Carton();
    void clear();
    unsigned add(unsigned number);
    unsigned marked(unsigned);
    unsigned _id;
    std::vector<unsigned> _numbers;
private:


    unsigned _marked;
};

#endif // CARTON_H
