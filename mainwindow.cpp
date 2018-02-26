#include "mainwindow.h"
#include "ui_mainwindow.h"


MainWindow::MainWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MainWindow)
{
    ui->setupUi(this);
    {
    numbers.push_back(ui->label_01);
    numbers.push_back(ui->label_01);
    numbers.push_back(ui->label_02);
    numbers.push_back(ui->label_03);
    numbers.push_back(ui->label_04);
    numbers.push_back(ui->label_05);
    numbers.push_back(ui->label_06);
    numbers.push_back(ui->label_07);
    numbers.push_back(ui->label_08);
    numbers.push_back(ui->label_09);
    numbers.push_back(ui->label_10);
    numbers.push_back(ui->label_11);
    numbers.push_back(ui->label_12);
    numbers.push_back(ui->label_13);
    numbers.push_back(ui->label_14);
    numbers.push_back(ui->label_15);
    numbers.push_back(ui->label_16);
    numbers.push_back(ui->label_17);
    numbers.push_back(ui->label_18);
    numbers.push_back(ui->label_19);
    numbers.push_back(ui->label_20);
    numbers.push_back(ui->label_21);
    numbers.push_back(ui->label_22);
    numbers.push_back(ui->label_23);
    numbers.push_back(ui->label_24);
    numbers.push_back(ui->label_25);
    numbers.push_back(ui->label_26);
    numbers.push_back(ui->label_27);
    numbers.push_back(ui->label_28);
    numbers.push_back(ui->label_29);
    numbers.push_back(ui->label_30);
    numbers.push_back(ui->label_31);
    numbers.push_back(ui->label_32);
    numbers.push_back(ui->label_33);
    numbers.push_back(ui->label_34);
    numbers.push_back(ui->label_35);
    numbers.push_back(ui->label_36);
    numbers.push_back(ui->label_37);
    numbers.push_back(ui->label_38);
    numbers.push_back(ui->label_39);
    numbers.push_back(ui->label_40);
    numbers.push_back(ui->label_41);
    numbers.push_back(ui->label_42);
    numbers.push_back(ui->label_43);
    numbers.push_back(ui->label_44);
    numbers.push_back(ui->label_45);
    numbers.push_back(ui->label_46);
    numbers.push_back(ui->label_47);
    numbers.push_back(ui->label_48);
    numbers.push_back(ui->label_49);
    numbers.push_back(ui->label_50);
    numbers.push_back(ui->label_51);
    numbers.push_back(ui->label_52);
    numbers.push_back(ui->label_53);
    numbers.push_back(ui->label_54);
    numbers.push_back(ui->label_55);
    numbers.push_back(ui->label_56);
    numbers.push_back(ui->label_57);
    numbers.push_back(ui->label_58);
    numbers.push_back(ui->label_59);
    numbers.push_back(ui->label_60);
    numbers.push_back(ui->label_61);
    numbers.push_back(ui->label_62);
    numbers.push_back(ui->label_63);
    numbers.push_back(ui->label_64);
    numbers.push_back(ui->label_65);
    numbers.push_back(ui->label_66);
    numbers.push_back(ui->label_67);
    numbers.push_back(ui->label_68);
    numbers.push_back(ui->label_69);
    numbers.push_back(ui->label_70);
    numbers.push_back(ui->label_71);
    numbers.push_back(ui->label_72);
    numbers.push_back(ui->label_73);
    numbers.push_back(ui->label_74);
    numbers.push_back(ui->label_75);
    numbers.push_back(ui->label_76);
    numbers.push_back(ui->label_77);
    numbers.push_back(ui->label_78);
    numbers.push_back(ui->label_79);
    numbers.push_back(ui->label_80);
    numbers.push_back(ui->label_81);
    numbers.push_back(ui->label_82);
    numbers.push_back(ui->label_83);
    numbers.push_back(ui->label_84);
    numbers.push_back(ui->label_85);
    numbers.push_back(ui->label_86);
    numbers.push_back(ui->label_87);
    numbers.push_back(ui->label_88);
    numbers.push_back(ui->label_89);
    numbers.push_back(ui->label_90);
    }
    for(unsigned i = 0; i<numbers.size(); i++) {
        numbers[i]->setStyleSheet("QLabel { background-color : black; color : black; }");
    }
}

MainWindow::~MainWindow()
{
    delete ui;
}

void MainWindow::on_CantarBolilla_clicked()
{
    int bolilla = ui->bolilla->text().toInt();
    if (bolilla > 0 && bolilla < 91) {
        if (bingo.cantar(bolilla)) {
            numbers[bolilla]->setStyleSheet("QLabel { background-color : black; color : green; }");
        }
        bingo.estadistica();
        return;
    } else if (-bolilla > 0 && -bolilla < 91) {
        if (bingo.deshacer_cantar((unsigned )-bolilla)){
            numbers[(unsigned) -bolilla]->setStyleSheet("QLabel { background-color : black; color : black; }");
        }
        bingo.estadistica();
        return;
    }
}

void MainWindow::on_CargarCartones_clicked()
{
    bingo.cargar_cartones("/home/ppilotti/Bingo/cartones.txt");
}
