#include "bingo.h"
#include <fstream>
#include <sstream>
#include <string>
#include <iostream>

Bingo::Bingo()
{

}

Bingo::~Bingo()
{
    for( std::vector<Carton*>::iterator it = cartones.begin();
         it != cartones.end();
         it++) {
        delete *it;
    }
}

bool Bingo::cantar(unsigned bolilla)
{
    for(std::vector<unsigned>::iterator it = cantados.begin();
        it < cantados.end(); ++it) {
        if (*it == (unsigned) bolilla) {
            std::cout<<"Ya fue cantado: "<<bolilla<<std::endl;
            return false;
        }
    }
    for( std::vector<Carton*>::iterator it = control[bolilla].begin(); it != control[bolilla].end(); it++) {
        (*it)->mark(bolilla);
    }
    cantados.push_back(bolilla);
    return true;
}

bool Bingo::deshacer_cantar(unsigned bolilla)
{
    for(std::vector<unsigned>::iterator num_it = cantados.begin();
        num_it < cantados.end(); ++num_it) {
        if (*num_it == bolilla) {
            for( std::vector<Carton*>::iterator it = control[bolilla].begin(); it != control[bolilla].end(); it++) {
                (*it)->unmark(bolilla);
            }
            cantados.erase(num_it);
            return true;
        }
    }
    std::cout<<"No fue cantado: "<<bolilla<<std::endl;
    return false;
}

bool Bingo::cargar_cartones(char * path)
{
    std::ifstream infile(path);

    if(!infile.is_open()) {
      std::cout << "Cannot open input file."<<std::endl;
      return false;
    }

    std::string line;
    unsigned id = 0;

    while (std::getline(infile, line))
    {
        std::istringstream iss(line);
        unsigned n1, n2, n3, n4, n5,
            n6, n7, n8, n9, nA,
            nB, nC, nD, nE, nF;
        if (!(iss >> n1 >> n2 >> n3 >> n4 >> n5 >>
              n6 >> n7 >> n8 >> n9 >> nA >>
              nB >> nC >> nD >> nE >> nF))
        {
            std::cout<<"problema"<<std::endl;
            break; } // error

        Carton* carton = new Carton(++id);
        carton->add(n1);
        control[n1].push_back(carton);

        carton->add(n2);
        control[n2].push_back(carton);

        carton->add(n3);
        control[n3].push_back(carton);

        carton->add(n4);
        control[n4].push_back(carton);

        carton->add(n5);
        control[n5].push_back(carton);

        carton->add(n6);
        control[n6].push_back(carton);

        carton->add(n7);
        control[n7].push_back(carton);

        carton->add(n8);
        control[n8].push_back(carton);

        carton->add(n9);
        control[n9].push_back(carton);

        carton->add(nA);
        control[nA].push_back(carton);

        carton->add(nB);
        control[nB].push_back(carton);

        carton->add(nC);
        control[nC].push_back(carton);

        carton->add(nD);
        control[nD].push_back(carton);

        carton->add(nE);
        control[nE].push_back(carton);

        carton->add(nF);
        control[nF].push_back(carton);

        cartones.push_back(carton);

    }
    std::cout<<"Cartones cargados:"<<id<<std::endl;
//    estadistica2();
    return true;

}
void Bingo::estadistica2()
{
    int contador[91][91];
    for(int i = 0; i<91; i++) {
        for(int j = 0; j<91; j++) {
            contador[i][j]=0;
        }
    }
    for( std::vector<Carton*>::iterator it = cartones.begin();
         it != cartones.end();
         it++) {
            for( int i =0; i < 15; i++)
                for(int j=i+1; j < 15; j++) {
                    int n = (*it)->_numbers[i];
                    int m = (*it)->_numbers[j];
//                    std::cout<<n<<" "<<m<<std::endl;
                    contador[n][m]++;
                    contador[m][n]++;
                }
    }
    float  sum = 0;
    for( int i = 1; i < 91; i++) {
        for( int j=1; j < 91; j++) {
            std::cout<<contador[i][j]<<", ";
            sum+= (contador[i][j]/2.0);
        }
        std::cout<<std::endl;
    }
    std::cout<<sum<<std::endl;
//    for(int i = 0; i<16; i++) {
//        std::cout<<contador[i]<<" ";
//        sum+=contador[i];
//    }
//    std::cout<<sum<<std::endl;
}
void Bingo::estadistica()
{
    int contador[16];
    for(int i = 0; i<16; i++) {
        contador[i]=0;
    }


    for( std::vector<Carton*>::iterator it = cartones.begin();
         it != cartones.end();
         it++) {
        contador[(*it)->_marked]++;
    }
    int sum = 0;
    for(int i = 0; i<16; i++) {
        std::cout<<contador[i]<<" ";
        sum+=contador[i];
    }
    std::cout<<sum<<std::endl;
}
