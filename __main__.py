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
from ai.predictSingle import *
from gui.results import *
import money_functions as mf

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
        self.ui.startSimulationButton.clicked.connect(self.simulation)

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
        dates.append(str(datetime.datetime.now()).split(" ")[0])

        value.append(predict_single(filename,nn_file)[0])
        for i in range(0,3):
            self.ui.tabela.setItem(0, i, QTableWidgetItem(str(dates[i])))
            self.ui.tabela.setItem(1, i, QTableWidgetItem(str(value[i])))


        # for i in range(0, 1):
        #     self.ui.tabela.setHorizontalHeaderItem(i, QTableWidgetItem(str(today.day)+'/'+str(today.month)+'/'+str(today.year)))
        #     today = today + datetime.timedelta(days=1)

        # for i in range(0, 1):
        #     self.ui.tabela.setItem(0, i, QTableWidgetItem(str(values[i])))



    def simulation(self):
        stock_name = self.ui.simulationStockNameLineEdit.text()
        nn_file = self.ui.simulationChosenNNLineEdit.text()

        start = self.ui.simulationFromDateEdit.date().addDays(-70).toString(format=PySide6.QtCore.Qt.DateFormat.ISODate)
        end = self.ui.simulationToDateEdit.date().toString(format=PySide6.QtCore.Qt.DateFormat.ISODate)
        filename = collect_data2(stock_name, start, end, interval="1d")

        activation = self.ui.simulationActivationFuncComboBoxz.currentText()

        podatek = self.ui.simulationTaxSpinBox.value()
        netto = 1.0 - podatek

        class ResultDlg(QDialog):
            def __init__(self,value,change: int,w1,w2, parent=None):
                super().__init__(parent)
                # Create an instance of the GUI
                self.ui = Ui_Dialog()
                # Run the .setupUi() method to show the GUI
                self.ui.setupUi(self)

                self.ui.result1Label.setText(f"Total money: {value}")
                self.ui.result2Label.setText(f"Change: {change}%")
                l1 = QHBoxLayout()
                l1.addWidget(w1)
                self.ui.widget1.setLayout(l1)
                l2 = QHBoxLayout()
                l2.addWidget(w2)
                self.ui.widget_2.setLayout(l2)


        real, predict_val = predict(filename, nn_file, int(self.ui.simulationFromDateEdit.date().daysTo(self.ui.simulationToDateEdit.date())*5/7))


        money = [0] * len(real)
        actions = [0] * len(real)
        total = [0] * len(real)

        money[0] = self.ui.simulationStartMoney.value()

        match activation:
            case "Binary":
                fun = mf.binary
            case "Sigmoid":
                fun = mf.sigmoid
            case "Tanh":
                fun = mf.tanh
            case "Modified Tanh":
                fun = mf.optimal
            case "Random":
                fun = mf.randomBinary

        for i in range(1, len(real)):
            change = (predict_val[i]-real[i - 1])/real[i - 1]
            if(change> 0):
                # kupuj
                ammount_to_by = int(abs(fun(change) * money[i - 1] / real[i - 1]))
                money[i] =  money[i - 1] - ammount_to_by*real[i - 1]
                actions[i] = actions[i - 1] + ammount_to_by
            else:
                # sprzedawaj
                ammount_to_sell = int(abs(fun(change) * actions[i - 1]))
                money[i] = money[i - 1] + ammount_to_sell * real[i - 1]
                actions[i] = actions[i - 1] - ammount_to_sell
            
            total[i] = money[i] + actions[i] * real[i]

        final_money = money[-1] + actions[-1]*real[-1]
        print(f"Final money: {final_money}")
        c1 = MyChart("Money","Day","Money")
        c1.addData(range(0,len(real)),money,"Money")
        c1.addData(range(0,len(real)),total,"Total wallet")
        c2 = MyChart("Actions","Day","Ammount")
        c2.addData(range(0,len(real)),actions,"Stocks")
        w1 = c1.toWidget()
        w2 = c2.toWidget()
        dialog = ResultDlg(final_money,int(100.0*(netto*final_money-money[0])/money[0]),w1,w2)
        dialog.show()

        



if __name__ == "__main__":
    app = QApplication(sys.argv)


    window = MainWindow()
    window.show()

    sys.exit(app.exec())