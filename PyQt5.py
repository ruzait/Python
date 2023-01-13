# Basic PyQt5 Window
import PyQt5.QtWidgets as qt

class my_win(qt.QWidget):
    def __init__(self):
        super().__init__()

        self.show()

app = qt.QApplication([])
ru = my_win()

app.exec()'''

'''# Basic PyQt5 Window
import PyQt5.QtWidgets as qt

class my_win(qt.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Wel come")
        self.setGeometry(450, 200, 300, 400)


        self.setLayout(qt.QVBoxLayout())
        mylab = qt.QLabel("asdfghjkl")

        self.layout().addWidget(mylab)

        self.show()

app = qt.QApplication([])
ru = my_win()


app.exec()'''

'''import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg  # for desaing


class Mainwindow(qtw.QWidget):
    def __init__(self):
        super().__init__()
        # add a title
        self.setWindowTitle("Hello World")

        # set V=Vertical(QVBox) layout
        self.setLayout(qtw.QVBoxLayout())

        # creat a lable
        my_label = qtw.QLabel("Ruzait")

        # Change font size of lable
        my_label.setFont(qtg.QFont('Helvetica', 18))
        self.layout().addWidget(my_label)

        # Creat an entry..
        my_entry = qtw.QLineEdit()
        my_entry.setObjectName("neme_field")
        my_entry.setText("")
        self.layout().addWidget(my_entry)

        # creat a button
        my_butt = qtw.QPushButton('Click Me!', clicked=lambda: press_it())
        self.layout().addWidget(my_butt)

        # show tha app
        self.show()

        def press_it():
            # add name to label
            my_label.setText(f'hello {my_entry.text()}')
            # clear the entry box
            my_entry.setText("")


app = qtw.QApplication([])
mw = Mainwindow()

# run app
app.exec()