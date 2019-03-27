import sys
import pandas as pd

import matplotlib.pyplot as plt

from PyQt5 import uic, QtWidgets

qtCreatorFile = "appandas.ui" 

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        
        
        self.Button1.clicked.connect(self.getCSV)
        self.Button2.clicked.connect(self.plot)
        
    def getCSV(self):
        filePath, _ = QtWidgets.QFileDialog.getOpenFileName(self, 'Open file', '/home/Desktop/Project')
        if filePath != "":
            print ("Direction",filePath) 
            self.df = pd.read_csv(str(filePath))
   
    def plot (self):
        x=self.df['col1']
        y=self.df['col2']
        plt.plot(x,y)
        plt.show()
        stat_st="statistics of col2: "+str(self.df['col1'].describe())
        self.Result.setText(stat_st)
   
    
if __name__ == "__main__":
    app =  QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    app.exec_()
    

