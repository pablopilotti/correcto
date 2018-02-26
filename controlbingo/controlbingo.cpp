#include <stdio.h>
#include <bingo.h>
#include <fstream>
#include <sstream>
#include <string>
#include <iostream>
#include <QFile>

static void printHelp(const char *app)
{
    printf("Usage: %s [OPTIONS]\n\n"
        "  -bingos <FILE.TXT>  Connect to this main board\n"
        "  -sorteo <FILE.TXT>  Dual-connect using this as target mobility board. Must be used together with -connect flag\n"
        "  -h                  Run this Python script\n"
        "\n",
        app);
}

int main(int argc, char ** argv)
{
    QString bingosfileName;
    QString sorteofileName;

    if (argc ==1) {
        printHelp(argv[0]);
        exit(0);
    }

    for (int i = 1; i < argc; i++) {
        if (strcmp(argv[i], "-h") == 0) {
            printHelp(argv[0]);
            exit(0);
        } else if (strcmp(argv[i], "-bingos") == 0) {
            if (argc > i + 1) {
                bingosfileName = argv[i + 1];
                if (!QFile(bingosfileName).exists()) {
                    printf("%s doesn't exist!\n", argv[i + 1]);
                    bingosfileName = QString();
                    exit(0);
                }
                i++;
            } else {
                printf("-bingos specified without a file name!\n");
                exit(0);
            }
        } else if (strcmp(argv[i], "-sorteo") == 0) {
            if (argc > i + 1) {
                sorteofileName = argv[i + 1];
                if (!QFile(sorteofileName).exists()) {
                    printf("%s doesn't exist!\n", argv[i + 1]);
                    sorteofileName = QString();
                    exit(0);
                }
                i++;
            } else {
                printf("-sorteo specified without a file name!\n");
                exit(0);
            }
        }
        else {
            printf("missing arguments!\n");
            exit(0);
        }
    }



    std::ifstream infile(sorteofileName.toLatin1().data());

    if(!infile.is_open()) {
        std::cout << "Cannot open input file."<<std::endl;
        exit(1);
    }

    std::string line;

    while (std::getline(infile, line))
    {
        Bingo* bingo = new Bingo;
        if(!bingo->cargar_cartones(bingosfileName.toLatin1().data()))
        {
            std::cout << "Cannot open input file."<<std::endl;
            exit(1);
        }
        std::istringstream iss(line);
        std::vector<unsigned> vect;
        unsigned n1;
        for(int i =0; i<90; i++)
        {
            if (!(iss >> n1)) {
                std::cout<<"problema"<<std::endl;
                exit(1);
            }

            vect.push_back(n1);
        }
        bingo->sortear(vect);
        delete bingo;
    }

    printf("abriendo '%s'\n", sorteofileName.toLatin1().data());
}



//    static const unsigned arr[] = {22, 84, 23, 69, 83, 2, 70, 42, 24, 44, 21, 46, 55, 61, 5, 19, 26, 60, 90, 3, 64, 15, 76, 49, 68, 18, 72, 67, 51,
//                                   12, 74, 48, 52, 65, 59, 1, 40, 10, 75, 66, 30, 63, 28, 29, 58, 73, 4, 41, 45, 57, 82, 20, 34, 32, 36};
//    std::vector<unsigned> vec (arr, arr + sizeof(arr) / sizeof(arr[0]) );


//}
//void MainWindow::on_CantarBolilla_clicked()
//{
//    int bolilla = ui->bolilla->text().toInt();
//    if (bolilla > 0 && bolilla < 91) {
//        if (bingo.cantar(bolilla)) {
//            numbers[bolilla]->setStyleSheet("QLabel { background-color : black; color : green; }");
//        }
//        bingo.estadistica();
//        return;
//    } else if (-bolilla > 0 && -bolilla < 91) {
//        if (bingo.deshacer_cantar((unsigned )-bolilla)){
//            numbers[(unsigned) -bolilla]->setStyleSheet("QLabel { background-color : black; color : black; }");
//        }
//        bingo.estadistica();
//        return;
//    }
//}

//void MainWindow::on_CargarCartones_clicked()
//{
//    bingo.cargar_cartones("/home/ppilotti/Bingo/cartones.txt");
//}
