import sys
from PySide6.QtCore import QPointF
from PySide6.QtGui import QPainter
from PySide6.QtWidgets import QWidget,QMainWindow, QApplication, QVBoxLayout
from PySide6.QtCharts import QChart, QChartView, QLineSeries


class MyChart(QChart):
    def __init__(self, title: str, xlabel: str, ylabel: str):
        super().__init__()
        self.title = title
        self.xlabel = xlabel
        self.ylabel = ylabel

    def addData(self, x: list[float] ,y: list[float], name: str):
        series = QLineSeries()
        if str:
            series.setName(name)
        assert(len(x) == len(y))
        for i in range(0,len(x)):
            series.append(x[i],y[i])
        self.addSeries(series)


    def toWidget(self):
        self.createDefaultAxes()
        self.setTitle(self.title)
        self.axisX().setTitleText(self.xlabel)
        self.axisY().setTitleText(self.ylabel)
    
        chart_view = QChartView(self)
        chart_view.setRenderHint(QPainter.Antialiasing)
        return chart_view

#Example
if __name__ == "__main__":
    app = QApplication(sys.argv)


    chart = MyChart("Mój pierwszy wykres", "X","Y")
    chart.addData([1,2,3,4],[2,1,3,7],'seria testowa')
    chart.addData([1,3,5,7],[1,4,1,0],'seria testowa2')

    # boilerplate
    window = QMainWindow()
    window.setCentralWidget(chart.toWidget())
    window.show()
    window.resize(440, 300)
    sys.exit(app.exec())