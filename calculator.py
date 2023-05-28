import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QHBoxLayout, QVBoxLayout, QPushButton

class Calculator(QWidget):
    def __init__(self):
        super(Calculator,self).__init__()
        self.vbox = QVBoxLayout(self)
        self.hbox_input = QHBoxLayout()
        self.hbox_first = QHBoxLayout()
        self.hbox_result = QHBoxLayout()

        self.vbox.addLayout(self.hbox_input)
        self.vbox.addLayout(self.hbox_first)
        self.vbox.addLayout(self.hbox_result)

        self.input = QLineEdit(self)
        self.hbox_input.addWidget(self.input)

        self.b_1 = QPushButton("1", self)
        self.hbox_first.addWidget(self.b_1)

        self.b_2 = QPushButton("2", self)
        self.hbox_first.addWidget(self.b_2)

        self.b_3 = QPushButton("3", self)
        self.hbox_first.addWidget(self.b_3)

        self.b_4 = QPushButton(".", self)
        self.hbox_first.addWidget(self.b_4)

        self.b_plus = QPushButton("+", self)
        self.hbox_first.addWidget(self.b_plus)

        self.b_minus = QPushButton("-", self)
        self.hbox_first.addWidget(self.b_minus)

        self.b_multy = QPushButton("*", self)
        self.hbox_first.addWidget(self.b_multy)

        self.b_divide = QPushButton("/", self)
        self.hbox_first.addWidget(self.b_divide)

        self.b_result = QPushButton("=", self)
        self.hbox_result.addWidget(self.b_result)

        '''def _actions(self, "act"):
            if self.b_plus.clicked:
                print(1)
                self.b_plus.clicked.connect(lambda: self._operation("+"))
                self.b_result.clicked.connect(self._result)
            if self.b_minus.clicked:
                print(2)
                self.b_minus.clicked.connect(lambda: self._operation("-"))
                self.b_result.clicked.connect(self._result)
            if self.b_multy.clicked:
                print(3)
                self.b_multy.clicked.connect(lambda: self._operation("*"))
                self.b_result.clicked.connect(self._result)
            if self.b_divide.clicked:
                print(4)
                self.b_divide.clicked.connect(lambda: self._operation("/"))
                self.b_result.clicked.connect(self._result)'''
        self.b_plus.clicked.connect(lambda: self._actions("+"))
        self.b_minus.clicked.connect(lambda: self._actions("-"))
        self.b_multy.clicked.connect(lambda: self._actions("*"))
        self.b_divide.clicked.connect(lambda: self._actions("/"))

        self.b_1.clicked.connect(lambda: self._button("1"))
        self.b_2.clicked.connect(lambda: self._button("2"))
        self.b_3.clicked.connect(lambda: self._button("3"))
        self.b_4.clicked.connect(lambda: self._button("."))

    def _actions(self, act):
        if act=="+":
            self._operation("+")
            return self.b_result.clicked.connect(self._result)
        if act=="-":
            print(2)
            self._operation("-")
            return self.b_result.clicked.connect(self._result)
        if act=="*":
            print(3)
            self._operation("*")
            return self.b_result.clicked.connect(self._result)
        if act=="/":
            print(4)
            self._operation("/")
            return self.b_result.clicked.connect(self._result)

    def _button(self, param):
        line = self.input.text()
        self.input.setText(line + param)

    def _operation(self, op):
        self.num_1 = float(self.input.text())
        self.op = op
        print(op)
        self.input.setText("")

    def _result(self):
        #try:
        #    self.num_1=self.num_2
        #except AttributeError:
        #    self.num_1=self.num_1
        print(10)
        self.num_2 = float(self.input.text())
        print(self.num_1)
        print(self.num_2)
        if self.op == "+":
            print(5)
            return self.input.setText(str(self.num_1 + self.num_2))
            #self.num_1=self.num_2=0
        if self.op =="-":
            print(6)
            return self.input.setText(str(self.num_1 - self.num_2))
            #self.num_1 =self.num_2=0
        if self.op =="*":
            print(7)
            return self.input.setText(str(self.num_1 * self.num_2))
            #self.num_1 =self.num_2=0
        if self.op =="/":
            print(8)
            return self.input.setText(str(self.num_1 / self.num_2))
            #self.num_1 =self.num_2=0
app = QApplication(sys.argv)

win = Calculator()
win.show()

sys.exit(app.exec_())