# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fenetre_graphique.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Pandemie(object):
    def setupUi(self, Pandemie):
        Pandemie.setObjectName("Pandemie")
        Pandemie.resize(1057, 777)
        Pandemie.setMinimumSize(QtCore.QSize(0, 0))
        self.widget = QtWidgets.QWidget(Pandemie)
        self.widget.setGeometry(QtCore.QRect(9, 50, 1035, 670))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.Titre = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.Titre.setFont(font)
        self.Titre.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Titre.setAlignment(QtCore.Qt.AlignCenter)
        self.Titre.setObjectName("Titre")
        self.gridLayout.addWidget(self.Titre, 0, 0, 1, 1)
        self.graphicsView = QtWidgets.QGraphicsView(self.widget)
        self.graphicsView.setMinimumSize(QtCore.QSize(800, 600))
        self.graphicsView.setMaximumSize(QtCore.QSize(900, 700))
        self.graphicsView.setStyleSheet("")
        self.graphicsView.setObjectName("graphicsView")
        self.gridLayout.addWidget(self.graphicsView, 1, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.Population_totale = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Population_totale.setFont(font)
        self.Population_totale.setObjectName("Population_totale")
        self.verticalLayout.addWidget(self.Population_totale)
        self.Compteur_population_totale = QtWidgets.QLCDNumber(self.widget)
        self.Compteur_population_totale.setMinimumSize(QtCore.QSize(0, 70))
        self.Compteur_population_totale.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"")
        self.Compteur_population_totale.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Compteur_population_totale.setFrameShadow(QtWidgets.QFrame.Plain)
        self.Compteur_population_totale.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.Compteur_population_totale.setObjectName("Compteur_population_totale")
        self.verticalLayout.addWidget(self.Compteur_population_totale)
        self.Population_saine = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Population_saine.setFont(font)
        self.Population_saine.setObjectName("Population_saine")
        self.verticalLayout.addWidget(self.Population_saine)
        self.Compteur_sains = QtWidgets.QLCDNumber(self.widget)
        self.Compteur_sains.setMinimumSize(QtCore.QSize(0, 70))
        self.Compteur_sains.setStyleSheet("background-color: rgb(0, 170, 0);")
        self.Compteur_sains.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Compteur_sains.setFrameShadow(QtWidgets.QFrame.Plain)
        self.Compteur_sains.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.Compteur_sains.setObjectName("Compteur_sains")
        self.verticalLayout.addWidget(self.Compteur_sains)
        self.Population_immunisee = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Population_immunisee.setFont(font)
        self.Population_immunisee.setObjectName("Population_immunisee")
        self.verticalLayout.addWidget(self.Population_immunisee)
        self.Compteur_immunises = QtWidgets.QLCDNumber(self.widget)
        self.Compteur_immunises.setMinimumSize(QtCore.QSize(0, 70))
        self.Compteur_immunises.setStyleSheet("background-color: rgb(255, 255, 0);")
        self.Compteur_immunises.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Compteur_immunises.setFrameShadow(QtWidgets.QFrame.Plain)
        self.Compteur_immunises.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.Compteur_immunises.setObjectName("Compteur_immunises")
        self.verticalLayout.addWidget(self.Compteur_immunises)
        self.Population_infectee = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Population_infectee.setFont(font)
        self.Population_infectee.setObjectName("Population_infectee")
        self.verticalLayout.addWidget(self.Population_infectee)
        self.Compteur_infectes = QtWidgets.QLCDNumber(self.widget)
        self.Compteur_infectes.setMinimumSize(QtCore.QSize(0, 70))
        self.Compteur_infectes.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.Compteur_infectes.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Compteur_infectes.setFrameShadow(QtWidgets.QFrame.Plain)
        self.Compteur_infectes.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.Compteur_infectes.setObjectName("Compteur_infectes")
        self.verticalLayout.addWidget(self.Compteur_infectes)
        self.Morts = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Morts.setFont(font)
        self.Morts.setObjectName("Morts")
        self.verticalLayout.addWidget(self.Morts)
        self.Compteur_Morts = QtWidgets.QLCDNumber(self.widget)
        self.Compteur_Morts.setMinimumSize(QtCore.QSize(0, 70))
        self.Compteur_Morts.setStyleSheet("background-color: rgb(170, 170, 255);\n"
"\n"
"")
        self.Compteur_Morts.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Compteur_Morts.setFrameShadow(QtWidgets.QFrame.Plain)
        self.Compteur_Morts.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.Compteur_Morts.setObjectName("Compteur_Morts")
        self.verticalLayout.addWidget(self.Compteur_Morts)
        self.gridLayout.addLayout(self.verticalLayout, 1, 1, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Date_SpinBox = QtWidgets.QSpinBox(self.widget)
        self.Date_SpinBox.setObjectName("Date_SpinBox")
        self.horizontalLayout.addWidget(self.Date_SpinBox)
        self.StartButton = QtWidgets.QPushButton(self.widget)
        self.StartButton.setObjectName("StartButton")
        self.horizontalLayout.addWidget(self.StartButton)
        self.StopButton = QtWidgets.QPushButton(self.widget)
        self.StopButton.setObjectName("StopButton")
        self.horizontalLayout.addWidget(self.StopButton)
        self.x2 = QtWidgets.QPushButton(self.widget)
        self.x2.setObjectName("x2")
        self.horizontalLayout.addWidget(self.x2)
        self.x4 = QtWidgets.QPushButton(self.widget)
        self.x4.setObjectName("x4")
        self.horizontalLayout.addWidget(self.x4)
        self.Confinement_checkBox = QtWidgets.QCheckBox(self.widget)
        self.Confinement_checkBox.setTristate(False)
        self.Confinement_checkBox.setObjectName("Confinement_checkBox")
        self.horizontalLayout.addWidget(self.Confinement_checkBox)
        self.Couvrefeu_checkBox = QtWidgets.QCheckBox(self.widget)
        self.Couvrefeu_checkBox.setTristate(False)
        self.Couvrefeu_checkBox.setObjectName("Couvrefeu_checkBox")
        self.horizontalLayout.addWidget(self.Couvrefeu_checkBox)
        self.gridLayout.addLayout(self.horizontalLayout, 2, 0, 1, 1)

        self.retranslateUi(Pandemie)
        QtCore.QMetaObject.connectSlotsByName(Pandemie)

    def retranslateUi(self, Pandemie):
        _translate = QtCore.QCoreApplication.translate
        Pandemie.setWindowTitle(_translate("Pandemie", "Form"))
        self.Titre.setText(_translate("Pandemie", "SIMULATION PANDEMIE"))
        self.Population_totale.setText(_translate("Pandemie", "Population totale"))
        self.Population_saine.setText(_translate("Pandemie", "Population saine"))
        self.Population_immunisee.setText(_translate("Pandemie", "Population immunisée"))
        self.Population_infectee.setText(_translate("Pandemie", "Population infectée"))
        self.Morts.setText(_translate("Pandemie", "Morts"))
        self.StartButton.setText(_translate("Pandemie", "START"))
        self.StopButton.setText(_translate("Pandemie", "STOP"))
        self.x2.setText(_translate("Pandemie", ">"))
        self.x4.setText(_translate("Pandemie", ">>"))
        self.Confinement_checkBox.setText(_translate("Pandemie", "CONFINEMENT"))
        self.Couvrefeu_checkBox.setText(_translate("Pandemie", "COUVRE-FEU"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Pandemie = QtWidgets.QWidget()
    ui = Ui_Pandemie()
    ui.setupUi(Pandemie)
    Pandemie.show()
    sys.exit(app.exec_())
