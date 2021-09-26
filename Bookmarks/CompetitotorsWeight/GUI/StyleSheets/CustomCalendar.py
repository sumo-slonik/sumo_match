from PySide2 import QtCore, QtGui, QtWidgets

class CustomCalendarWidget(QtWidgets.QCalendarWidget):
    def __init__(self, parent=None):
        super(CustomCalendarWidget, self).__init__(parent,
                                             verticalHeaderFormat=QtWidgets.QCalendarWidget.NoVerticalHeader,
                                             gridVisible=False)
        self.setVerticalHeaderFormat(QtWidgets.QCalendarWidget.NoVerticalHeader)
        for d in (QtCore.Qt.Saturday, QtCore.Qt.Sunday,):
            fmt = self.weekdayTextFormat(d)
            fmt.setForeground(QtCore.Qt.darkGray)
            self.setWeekdayTextFormat(d, fmt)

    def paintCell(self, painter, rect, date):
        if date == self.selectedDate():
            painter.save()
            painter.fillRect(rect, QtGui.QColor("#FEB886"))
            painter.setPen(QtCore.Qt.NoPen)
            painter.setBrush(QtGui.QColor("#F8A76D"))
            r = QtCore.QRect(QtCore.QPoint(), min(rect.width(), rect.height()) * QtCore.QSize(1, 1))
            r.moveCenter(rect.center())
            painter.drawEllipse(r)
            #selected date text color
            painter.setPen(QtGui.QPen(QtGui.QColor("gray")))
            painter.drawText(rect, QtCore.Qt.AlignCenter, str(date.day()))
            painter.restore()
        else:
            super(CustomCalendarWidget, self).paintCell(painter, rect, date)
