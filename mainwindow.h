#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>
#include <QLabel>
#include <carton.h>
#include <map>

namespace Ui {
class MainWindow;
}

class MainWindow : public QMainWindow
{
    Q_OBJECT

public:
    explicit MainWindow(QWidget *parent = 0);
    ~MainWindow();

private slots:
    void on_CantarBolilla_clicked();

    void on_CargarCartones_clicked();

private:
    Ui::MainWindow *ui;
    std::vector<QLabel*> numbers;
    std::vector<Carton> cartones;
    std::map<unsigned,std::vector<Carton*> > control;
};

#endif // MAINWINDOW_H
