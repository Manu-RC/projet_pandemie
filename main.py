from interface_graphique import Ui_Form
from universe import Universe 
import sys
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QApplication


        
        
def main():

    app = QtWidgets.QApplication(sys.argv)
    
    ui = Ui_Form()
    Form = Universe(500,500)
    ui.setupUi(Form)
    ui.graphicsView.setScene(Form.scene)
    Form.show()
    sys.exit(app.exec_())



if __name__ == "__main__":
    main()


