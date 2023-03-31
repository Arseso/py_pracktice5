from PyQt5.QtWidgets import QApplication, QLabel, QLineEdit, QPushButton, QCheckBox, QComboBox, QGridLayout, QWidget

class AccountForm(QWidget):
    def __init__(self):
        super().__init__()

        # Создание виджетов
        self.label_fio = QLabel('ФИО:')
        self.label_email = QLabel('Почта:')
        self.label_phone = QLabel('Телефон:')
        self.label_topics = QLabel('Интересы:')
        self.line_edit_fio = QLineEdit()
        self.line_edit_email = QLineEdit()
        self.line_edit_phone = QLineEdit()
        self.check_box_data_processing = QCheckBox('Я согласен на обработку персональных данных')
        self.check_box_newsletter = QCheckBox('Подписаться на новостную рассылку')
        self.combo_box_topics = QComboBox()
        self.combo_box_topics.addItems(['Тема 1', 'Тема 2', 'Тема 3', 'Тема 4'])

        # Создание кнопок
        self.button_check_input = QPushButton('Проверить ввод')
        self.button_check_input.clicked.connect(self.check_input)

        # Создание сетки для размещения виджетов
        grid = QGridLayout()
        grid.addWidget(self.label_fio, 0, 0)
        grid.addWidget(self.line_edit_fio, 0, 1)
        grid.addWidget(self.label_email, 1, 0)
        grid.addWidget(self.line_edit_email, 1, 1)
        grid.addWidget(self.label_phone, 2, 0)
        grid.addWidget(self.line_edit_phone, 2, 1)
        grid.addWidget(self.label_topics, 3, 0)
        grid.addWidget(self.combo_box_topics, 3, 1)
        grid.addWidget(self.check_box_data_processing, 4, 0, 1, 2)
        grid.addWidget(self.check_box_newsletter, 5, 0, 1, 2)
        grid.addWidget(self.button_check_input, 6, 0, 1, 2)

        # Установка сетки на форму
        self.setLayout(grid)

    def check_input(self):
        # валидация введенных данных
        fio = self.line_edit_fio.text()
        email = self.line_edit_email.text()
        phone = self.line_edit_phone.text()
        topics = self.combo_box_topics.currentText()

        if not fio or not email or not phone or not topics:
            print('Необходимо заполнить все поля')
            return

        if not self.check_box_data_processing.isChecked():
            print('Необходимо согласиться на обработку персональных данных')
            return

        if self.check_box_newsletter.isChecked():
            print('Подписка на рассылку оформлена')

        print(f'ФИО: {fio}')
        print(f'Почта: {email}')
        print(f'Телефон: {phone}')
        print(f'Темы: {topics}')

if __name__ == '__main__':
    app = QApplication([])
    account_form = AccountForm()
    account_form.show()
    app.exec_()
