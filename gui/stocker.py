# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'stocker.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QDoubleSpinBox,
    QGridLayout, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QSpinBox, QTabWidget, QTableWidget,
    QTableWidgetItem, QTextBrowser, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(497, 453)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.widget = QWidget()
        self.widget.setObjectName(u"widget")
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        font = QFont()
        font.setPointSize(20)
        self.label_2.setFont(font)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_2)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(-1, -1, 50, -1)
        self.label_14 = QLabel(self.widget)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_7.addWidget(self.label_14)

        self.trainingStockLineEdit = QLineEdit(self.widget)
        self.trainingStockLineEdit.setObjectName(u"trainingStockLineEdit")

        self.horizontalLayout_7.addWidget(self.trainingStockLineEdit)

        self.horizontalLayout_7.setStretch(0, 1)
        self.horizontalLayout_7.setStretch(1, 2)

        self.verticalLayout.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, -1, 50, -1)
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.label)

        self.trainingFromDateEdit = QDateEdit(self.widget)
        self.trainingFromDateEdit.setObjectName(u"trainingFromDateEdit")
        self.trainingFromDateEdit.setAlignment(Qt.AlignCenter)
        self.trainingFromDateEdit.setCalendarPopup(True)

        self.horizontalLayout_2.addWidget(self.trainingFromDateEdit)

        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 2)

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(-1, -1, 50, -1)
        self.label_15 = QLabel(self.widget)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_8.addWidget(self.label_15)

        self.trainingToDateEdit = QDateEdit(self.widget)
        self.trainingToDateEdit.setObjectName(u"trainingToDateEdit")
        self.trainingToDateEdit.setAlignment(Qt.AlignCenter)
        self.trainingToDateEdit.setCalendarPopup(True)

        self.horizontalLayout_8.addWidget(self.trainingToDateEdit)

        self.horizontalLayout_8.setStretch(0, 1)
        self.horizontalLayout_8.setStretch(1, 2)

        self.verticalLayout.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(-1, -1, 50, -1)
        self.label_16 = QLabel(self.widget)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_9.addWidget(self.label_16)

        self.trainEpochSpinBox = QSpinBox(self.widget)
        self.trainEpochSpinBox.setObjectName(u"trainEpochSpinBox")
        self.trainEpochSpinBox.setEnabled(True)
        self.trainEpochSpinBox.setAlignment(Qt.AlignCenter)
        self.trainEpochSpinBox.setMinimum(1)
        self.trainEpochSpinBox.setValue(30)

        self.horizontalLayout_9.addWidget(self.trainEpochSpinBox)

        self.horizontalLayout_9.setStretch(0, 1)
        self.horizontalLayout_9.setStretch(1, 2)

        self.verticalLayout.addLayout(self.horizontalLayout_9)

        self.trainButton = QPushButton(self.widget)
        self.trainButton.setObjectName(u"trainButton")
        self.trainButton.setMinimumSize(QSize(0, 35))
        self.trainButton.setFont(font)

        self.verticalLayout.addWidget(self.trainButton)

        self.trainingTextBrowser = QTextBrowser(self.widget)
        self.trainingTextBrowser.setObjectName(u"trainingTextBrowser")

        self.verticalLayout.addWidget(self.trainingTextBrowser)

        self.tabWidget.addTab(self.widget, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_3 = QVBoxLayout(self.tab_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)

        self.label_11 = QLabel(self.tab_2)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font)
        self.label_11.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_11)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_3)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(50, -1, 50, -1)
        self.predictingChooseNNButton = QPushButton(self.tab_2)
        self.predictingChooseNNButton.setObjectName(u"predictingChooseNNButton")

        self.gridLayout.addWidget(self.predictingChooseNNButton, 1, 0, 1, 1)

        self.label_3 = QLabel(self.tab_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)

        self.predictingStockNameLineEdit = QLineEdit(self.tab_2)
        self.predictingStockNameLineEdit.setObjectName(u"predictingStockNameLineEdit")

        self.gridLayout.addWidget(self.predictingStockNameLineEdit, 0, 1, 1, 1)

        self.predictingChosenNNLineEdit = QLineEdit(self.tab_2)
        self.predictingChosenNNLineEdit.setObjectName(u"predictingChosenNNLineEdit")

        self.gridLayout.addWidget(self.predictingChosenNNLineEdit, 1, 1, 1, 1)

        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setColumnStretch(1, 2)

        self.verticalLayout_3.addLayout(self.gridLayout)

        self.predictButton = QPushButton(self.tab_2)
        self.predictButton.setObjectName(u"predictButton")
        self.predictButton.setMinimumSize(QSize(0, 35))
        self.predictButton.setFont(font)

        self.verticalLayout_3.addWidget(self.predictButton)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.tabela = QTableWidget(self.tab_2)
        if (self.tabela.columnCount() < 3):
            self.tabela.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.tabela.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tabela.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tabela.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        if (self.tabela.rowCount() < 2):
            self.tabela.setRowCount(2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tabela.setVerticalHeaderItem(0, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tabela.setVerticalHeaderItem(1, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setTextAlignment(Qt.AlignJustify|Qt.AlignVCenter);
        self.tabela.setItem(0, 0, __qtablewidgetitem5)
        self.tabela.setObjectName(u"tabela")
        self.tabela.horizontalHeader().setCascadingSectionResizes(False)

        self.verticalLayout_3.addWidget(self.tabela)

        self.predictingWidget = QWidget(self.tab_2)
        self.predictingWidget.setObjectName(u"predictingWidget")

        self.verticalLayout_3.addWidget(self.predictingWidget)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.verticalLayout_4 = QVBoxLayout(self.tab_3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_13 = QLabel(self.tab_3)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font)
        self.label_13.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_13)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(50, -1, 50, -1)
        self.simulationChosenNNLineEdit = QLineEdit(self.tab_3)
        self.simulationChosenNNLineEdit.setObjectName(u"simulationChosenNNLineEdit")

        self.gridLayout_2.addWidget(self.simulationChosenNNLineEdit, 1, 1, 1, 1)

        self.simulationChooseNNButton = QPushButton(self.tab_3)
        self.simulationChooseNNButton.setObjectName(u"simulationChooseNNButton")

        self.gridLayout_2.addWidget(self.simulationChooseNNButton, 1, 0, 1, 1)

        self.label_4 = QLabel(self.tab_3)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_4, 0, 0, 1, 1)

        self.label_5 = QLabel(self.tab_3)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_5, 2, 0, 1, 1)

        self.simulationStockNameLineEdit = QLineEdit(self.tab_3)
        self.simulationStockNameLineEdit.setObjectName(u"simulationStockNameLineEdit")

        self.gridLayout_2.addWidget(self.simulationStockNameLineEdit, 0, 1, 1, 1)

        self.simulationTaxSpinBox = QDoubleSpinBox(self.tab_3)
        self.simulationTaxSpinBox.setObjectName(u"simulationTaxSpinBox")
        self.simulationTaxSpinBox.setMaximum(1.000000000000000)
        self.simulationTaxSpinBox.setSingleStep(0.010000000000000)

        self.gridLayout_2.addWidget(self.simulationTaxSpinBox, 3, 1, 1, 1)

        self.label_6 = QLabel(self.tab_3)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_6, 3, 0, 1, 1)

        self.simulationStartMoney = QDoubleSpinBox(self.tab_3)
        self.simulationStartMoney.setObjectName(u"simulationStartMoney")
        self.simulationStartMoney.setMaximum(999999999.000000000000000)
        self.simulationStartMoney.setSingleStep(1000.000000000000000)
        self.simulationStartMoney.setValue(10000.000000000000000)

        self.gridLayout_2.addWidget(self.simulationStartMoney, 2, 1, 1, 1)

        self.label_7 = QLabel(self.tab_3)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_7, 4, 0, 1, 1)

        self.simulationActivationFuncComboBoxz = QComboBox(self.tab_3)
        self.simulationActivationFuncComboBoxz.addItem("")
        self.simulationActivationFuncComboBoxz.addItem("")
        self.simulationActivationFuncComboBoxz.addItem("")
        self.simulationActivationFuncComboBoxz.addItem("")
        self.simulationActivationFuncComboBoxz.addItem("")
        self.simulationActivationFuncComboBoxz.setObjectName(u"simulationActivationFuncComboBoxz")

        self.gridLayout_2.addWidget(self.simulationActivationFuncComboBoxz, 4, 1, 1, 1)

        self.gridLayout_2.setColumnStretch(0, 1)

        self.verticalLayout_4.addLayout(self.gridLayout_2)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(50, -1, 50, -1)
        self.label_18 = QLabel(self.tab_3)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_11.addWidget(self.label_18)

        self.simulationFromDateEdit = QDateEdit(self.tab_3)
        self.simulationFromDateEdit.setObjectName(u"simulationFromDateEdit")

        self.horizontalLayout_11.addWidget(self.simulationFromDateEdit)

        self.horizontalLayout_11.setStretch(0, 1)
        self.horizontalLayout_11.setStretch(1, 2)

        self.verticalLayout_4.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(50, -1, 50, -1)
        self.label_19 = QLabel(self.tab_3)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_12.addWidget(self.label_19)

        self.simulationToDateEdit = QDateEdit(self.tab_3)
        self.simulationToDateEdit.setObjectName(u"simulationToDateEdit")
        self.simulationToDateEdit.setEnabled(True)

        self.horizontalLayout_12.addWidget(self.simulationToDateEdit)

        self.horizontalLayout_12.setStretch(0, 1)
        self.horizontalLayout_12.setStretch(1, 2)

        self.verticalLayout_4.addLayout(self.horizontalLayout_12)

        self.startSimulationButton = QPushButton(self.tab_3)
        self.startSimulationButton.setObjectName(u"startSimulationButton")

        self.verticalLayout_4.addWidget(self.startSimulationButton)

        self.simulationWidget = QWidget(self.tab_3)
        self.simulationWidget.setObjectName(u"simulationWidget")

        self.verticalLayout_4.addWidget(self.simulationWidget)

        self.tabWidget.addTab(self.tab_3, "")

        self.horizontalLayout.addWidget(self.tabWidget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Training Neural Network", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Stock name:", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"From:", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"To:", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Epoch:", None))
        self.trainButton.setText(QCoreApplication.translate("MainWindow", u"Train", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.widget), QCoreApplication.translate("MainWindow", u"Training", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Predicting value for the next days", None))
        self.predictingChooseNNButton.setText(QCoreApplication.translate("MainWindow", u"Choose NN", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Stock name:", None))
        self.predictButton.setText(QCoreApplication.translate("MainWindow", u"Predict", None))
        ___qtablewidgetitem = self.tabela.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Yesterday", None));
        ___qtablewidgetitem1 = self.tabela.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Today", None));
        ___qtablewidgetitem2 = self.tabela.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Next day", None));
        ___qtablewidgetitem3 = self.tabela.verticalHeaderItem(0)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Dates", None));
        ___qtablewidgetitem4 = self.tabela.verticalHeaderItem(1)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Values", None));

        __sortingEnabled = self.tabela.isSortingEnabled()
        self.tabela.setSortingEnabled(False)
        self.tabela.setSortingEnabled(__sortingEnabled)

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Predicting", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Trading simulation", None))
        self.simulationChooseNNButton.setText(QCoreApplication.translate("MainWindow", u"Choose NN", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Stock name:", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Start money:", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Tax", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Activation function", None))
        self.simulationActivationFuncComboBoxz.setItemText(0, QCoreApplication.translate("MainWindow", u"Binary", None))
        self.simulationActivationFuncComboBoxz.setItemText(1, QCoreApplication.translate("MainWindow", u"Tanh", None))
        self.simulationActivationFuncComboBoxz.setItemText(2, QCoreApplication.translate("MainWindow", u"Sigmoid", None))
        self.simulationActivationFuncComboBoxz.setItemText(3, QCoreApplication.translate("MainWindow", u"Modified Tanh", None))
        self.simulationActivationFuncComboBoxz.setItemText(4, QCoreApplication.translate("MainWindow", u"Random", None))

        self.label_18.setText(QCoreApplication.translate("MainWindow", u"From:", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"To:", None))
        self.startSimulationButton.setText(QCoreApplication.translate("MainWindow", u"Start simulation", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Simulation", None))
    # retranslateUi

