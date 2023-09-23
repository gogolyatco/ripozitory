from PyQt5.QtWidgets import  QApplication, QWidget, QLabel,  QMessageBox,QRadioButton

app = QApplication([])
win = QWidget()
win.setWindowTitle('Конкурс від Crazy People')
win.resize(600, 300)
question = QLabel(win)
question.setText('Якого року канал отримав золоту кнопу від ютуб?')
question.move(75, 15)

button1 = QRadioButton(win)
button1.setText('2020')
button1.move(150, 90)

button2 = QRadioButton(win)
button2.setText('2025')
button2.move(150, 180)

button3 = QRadioButton(win)
button3.setText('2005')
button3.move(450, 180)

button4 = QRadioButton(win)
button4.setText('2015')
button4.move(450, 90)

def show_win():
    win2 = QMessageBox()
    win2.setText('правильно! Ви виграли б-у-шну палbxку від морозива')
    win2.exec_()

button3.clicked.connect(show_win)
def show_lose():
    win2 = QMessageBox()
    win2.setText('Ні, в &^:* році. Ви виграли нічого')
    win2.exec_()
button2.clicked.connect(show_lose)
button4.clicked.connect(show_lose)
button1.clicked.connect(show_lose)

win.show()
app.exec_()