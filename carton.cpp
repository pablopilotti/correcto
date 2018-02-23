#include "carton.h"
#include <assert.h>
#include <iostream>

Carton::Carton()
{
    clear();
}

void Carton::clear()
{
    _numbers.clear();
    _id = 0;
    _marked = 0;
}

unsigned Carton::add(unsigned number)
{
    _numbers.push_back(number);
    return _numbers.size();
}

unsigned Carton::marked(unsigned number)
{
    for (std::vector<unsigned>::iterator it = _numbers.begin();
         it != _numbers.end(); ++it) {
        if (*it == number) {
            _marked++;
//            std::cout<<"Carton "<<_id<< "marcados: "<< _marked<<std::endl;
            return _marked;
        }
    }
    assert(0);
}
