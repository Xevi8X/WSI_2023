import sys
from subprocess import Popen, PIPE
import PySide6
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QHBoxLayout
from PySide6.QtCore import QFile
from gui.stocker import Ui_MainWindow
from data_collector import collect_data2
from random import random
from gui.myChart import MyChart

class MainWindow(QMainWindow):

    run: bool = False

    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.trainButton.clicked.connect(self.trainNN)
        self.ui.predictingChooseNNButton.clicked.connect(self.browseFiles)
        self.ui.predictButton.clicked.connect(self.predict)

    def trainNN(self):
        if(self.run):
            return
        self.run = True
        stock_name = self.ui.trainingStockLineEdit.text()
        start = self.ui.trainingFromDateEdit.date().toString(format=PySide6.QtCore.Qt.DateFormat.ISODate)
        end = self.ui.trainingToDateEdit.date().toString(format=PySide6.QtCore.Qt.DateFormat.ISODate)
        epochNo = self.ui.trainEpochSpinBox.value()
        filename = collect_data2(stock_name, start, end, interval="1d")
        process = Popen(['python', 'train.py', filename, str(epochNo)], stdout=PIPE,bufsize=1, universal_newlines=True)
        for line in iter(process.stdout.readline, ''):
            self.ui.trainingTextBrowser.append(line[:-1])
            QApplication.processEvents()
        self.run = False
    
        
    def browseFiles(self):
        fname=QFileDialog.getOpenFileName(self,'Open file', '.', '(*.h5)')
        self.ui.predictingChosenNNLineEdit.setText(fname[0])

    def predict(self):
        stock_name = self.ui.predictingStockNameLineEdit.text()
        nn_file = self.ui.predictingChosenNNLineEdit.text()

        print(f"Predicting next days for {stock_name} based on model {nn_file}")
        # values = predict(nn_file,stock_name)
        values = [(random()-0.5)*1000.0 for _ in range(5)]

        #Todo, wstawianie do tabli


if __name__ == "__main__":
    app = QApplication(sys.argv)


    window = MainWindow()
    window.show()

    sys.exit(app.exec())