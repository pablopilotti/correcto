#-------------------------------------------------
#
# Project created by QtCreator 2018-02-21T23:34:18
#
#-------------------------------------------------

QT       += core gui

greaterThan(QT_MAJOR_VERSION, 4): QT += widgets

TARGET = Bingo
TEMPLATE = subdirs
SUBDIRS = common gui controlbingo

gui.deppends = common
controlbingo.deppends = common
