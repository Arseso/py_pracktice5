import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QTabWidget
from usr_form import AccountForm
from main import ScheduleWindow
from dynamic_obj import interface as DraggableWidget


class MainApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Main Application")

        self.tab_widget = QTabWidget()
        self.setCentralWidget(self.tab_widget)

        # Adding tabs for each window
        self.tab_account = AccountForm()
        self.tab_widget.addTab(self.tab_account, "Account Form")

        self.tab_schedule = ScheduleWindow()
        self.tab_widget.addTab(self.tab_schedule, "Schedule Window")

        self.tab_draggable = DraggableWidget()
        self.tab_widget.addTab(self.tab_draggable, "Draggable Widget")


def run_app():
    app = QApplication(sys.argv)
    main_app = MainApp()
    main_app.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    run_app()
