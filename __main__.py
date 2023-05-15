import sys
from subprocess import Popen, PIPE
import PySide6
import datetime
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QHeaderView, QHBoxLayout, QTableWidgetItem
from PySide6.QtCore import QFile
from gui.stocker import Ui_MainWindow
from data_collector import *
from random import random
from gui.myChart import MyChart
from ai.constants import *
from ai.predictSingle import predict_single

class MainWindow(QMainWindow):

    run: bool = False

    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setUpTable()
        self.ui.trainButton.clicked.connect(self.trainNN)
        self.ui.predictingChooseNNButton.clicked.connect(lambda: self.browseFiles(self.ui.predictingChosenNNLineEdit))
        self.ui.predictButton.clicked.connect(self.predict)
        self.ui.simulationChooseNNButton.clicked.connect(lambda: self.browseFiles(self.ui.simulationChosenNNLineEdit))

    def trainNN(self):
        if(self.run):
            return
        self.run = True
        stock_name = self.ui.trainingStockLineEdit.text()
        start = self.ui.trainingFromDateEdit.date().toString(format=PySide6.QtCore.Qt.DateFormat.ISODate)
        end = self.ui.trainingToDateEdit.date().toString(format=PySide6.QtCore.Qt.DateFormat.ISODate)
        epochNo = self.ui.trainEpochSpinBox.value()
        filename = collect_data2(stock_name, start, end, interval="1d")
        process = Popen(['python3', 'ai/trainSpecial.py', filename, str(epochNo), str(BATCH_SIZE), f"{stock_name}_{start}_{end}.h5"], stdout=PIPE,bufsize=1, universal_newlines=True)
        for line in iter(process.stdout.readline, ''):
            self.ui.trainingTextBrowser.append(line[:-1])
            QApplication.processEvents()
        self.ui.trainingTextBrowser.append("DONE!")
        self.run = False
    
        
    def browseFiles(self, lineEdit):
        fname=QFileDialog.getOpenFileName(self,'Open file', '.', '(*.h5)')
        lineEdit.setText(fname[0])

    def setUpTable(self):
        self.ui.tabela.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.tabela.horizontalHeader().setStretchLastSection(True)
        width = int(self.ui.tabela.width() * 0.14)

        for i in range(0, 5):
            self.ui.tabela.setColumnWidth(i, width)



    def predict(self):
        stock_name = self.ui.predictingStockNameLineEdit.text()
        nn_file = self.ui.predictingChosenNNLineEdit.text()

        filename,historicalData = collect_data3(stock_name, datetime.datetime.now() - datetime.timedelta(days=70), datetime.datetime.now(), interval="1d")

        print(f"Predicting next day for {filename} based on model {nn_file}")
        value = []
        value.append(historicalData.Close[-2])
        value.append(historicalData.Close[-1])
        dates = []
        dates.append(str(historicalData.index[-2]).split(" ")[0])
        dates.append(str(historicalData.index[-1]).split(" ")[0])
        dates.append(str(datetime.datetime.now()))

        value.append(predict_single(filename,nn_file))
        for i in range(0,3):
            self.ui.tabela.setItem(0, i, QTableWidgetItem(str(dates[i])))
            self.ui.tabela.setItem(1, i, QTableWidgetItem(str(value[i])))

        # for i in range(0, 1):
        #     self.ui.tabela.setHorizontalHeaderItem(i, QTableWidgetItem(str(today.day)+'/'+str(today.month)+'/'+str(today.year)))
        #     today = today + datetime.timedelta(days=1)

        # for i in range(0, 1):
        #     self.ui.tabela.setItem(0, i, QTableWidgetItem(str(values[i])))


if __name__ == "__main__":
    app = QApplication(sys.argv)


    window = MainWindow()
    window.show()

    sys.exit(app.exec())