from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem


class ScheduleWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Расписание")
        self.setGeometry(100, 100, 500, 500)

        # Создание таблицы расписания
        self.schedule_table = QTableWidget(self)
        self.schedule_table.setGeometry(10, 10, 500, 500)
        self.schedule_table.setColumnCount(2)
        self.schedule_table.setRowCount(11)
        self.schedule_table.setHorizontalHeaderLabels(['Группа 1', 'Группа 2'])
        self.schedule_table.setVerticalHeaderLabels(['Понедельник','','','', 'Среда','','', 'Пятница','','',''])

        # Заполнение таблицы расписания
        self.schedule_table.setItem(0, 0, QTableWidgetItem('Теория алгоритмов'))
        self.schedule_table.setItem(0, 1, QTableWidgetItem('Теория вероятности'))
        self.schedule_table.setItem(1, 0, QTableWidgetItem('Теория алгоритмов'))
        self.schedule_table.setSpan(1, 0, 1, 2)
        self.schedule_table.setItem(2, 0, QTableWidgetItem('Дифференциальные уравнения'))
        self.schedule_table.setItem(2, 1, QTableWidgetItem('Теория алгоритмов'))
        self.schedule_table.setItem(3, 0, QTableWidgetItem('Теория вероятности'))
        self.schedule_table.setSpan(3, 0, 1, 2)

        self.schedule_table.setItem(4, 0, QTableWidgetItem('Компьютерные сети'))
        self.schedule_table.setSpan(4, 0, 1, 2)
        self.schedule_table.setItem(5, 0, QTableWidgetItem('Физкультура'))
        self.schedule_table.setSpan(5, 0, 1, 2)
        self.schedule_table.setItem(6, 0, QTableWidgetItem('Тестирование ПО'))
        self.schedule_table.setSpan(6, 0, 1, 2)

        self.schedule_table.setItem(7, 0, QTableWidgetItem(''))
        self.schedule_table.setItem(7, 1, QTableWidgetItem(''))
        self.schedule_table.setItem(8, 0, QTableWidgetItem('Физкультура'))
        self.schedule_table.setSpan(8, 0, 1, 2)
        self.schedule_table.setItem(9, 0, QTableWidgetItem('Языки и методы программирования'))
        self.schedule_table.setSpan(9, 0, 1, 2)
        self.schedule_table.setItem(10, 0, QTableWidgetItem('Языки и методы программирования'))
        self.schedule_table.setItem(10, 1, QTableWidgetItem(''))


if __name__ == '__main__':
    app = QApplication([])
    schedule_window = ScheduleWindow()
    schedule_window.show()
    app.exec_()

