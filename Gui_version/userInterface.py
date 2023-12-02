import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg

class MainWindow(qtw.QWidget):
    def __init__(self) -> None:
        super().__init__()

        # setting the main page title
        self.setWindowTitle("Pyelp")

        #setting the layout
        # a vertical layout
        self.setLayout(qtw.QVBoxLayout())

        #creating the lable 
        my_label = qtw.QLabel("Log in:")
        self.layout().addWidget(my_label)
        #changing the font size here
        my_label.setFont(qtg.QFont('Helvetica',18))

        #creating an entry box (for input)
        my_entry = qtw.QLineEdit()
        # a name to be used for refrence later
        my_entry.setObjectName("user_id_input")
        # place holder text
        my_entry.setText("your user_id ...")
        # adding the input line box to layout
        self.layout().addWidget(my_entry)


        #creating a button
        my_button = qtw.QPushButton("sign in",clicked= lambda: onClick())
        # adding the button to layout
        self.layout().addWidget(my_button)

        # show the window
        self.show()

        def onClick():
            my_label.setText("HMMM")

app = qtw.QApplication([])
mainWindow = MainWindow()
app.exec_()