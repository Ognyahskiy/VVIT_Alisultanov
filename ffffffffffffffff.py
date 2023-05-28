import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QHBoxLayout, QVBoxLayout, QPushButton

class Calculator(QWidget):
    def __init__(self):
        super(Calculator, self).__init__()

        self.vbox = QVBoxLayout(self)
        self.hbox_input = QHBoxLayout()
        self.hbox_first = QHBoxLayout()
        self.hbox_second=QHBoxLayout()
        self.hbox_third=QHBoxLayout()
        self.hbox_result = QHBoxLayout()

        self.vbox.addLayout(self.hbox_input)
        self.vbox.addLayout(self.hbox_first)
        self.vbox.addLayout(self.hbox_second)
        self.vbox.addLayout(self.hbox_third)
        self.vbox.addLayout(self.hbox_result)

        self.input = QLineEdit(self)
        self.hbox_input.addWidget(self.input)

        self.b_1 = QPushButton("1", self)
        self.hbox_first.addWidget(self.b_1)

        self.b_2 = QPushButton("2", self)
        self.hbox_first.addWidget(self.b_2)

        self.b_3 = QPushButton("3", self)
        self.hbox_first.addWidget(self.b_3)

        self.b_plus = QPushButton("+", self)
        self.hbox_first.addWidget(self.b_plus)

        self.b_4 = QPushButton("4", self)
        self.hbox_second.addWidget(self.b_4)

        self.b_5 = QPushButton("5", self)
        self.hbox_second.addWidget(self.b_5)

        self.b_6 = QPushButton("6", self)
        self.hbox_second.addWidget(self.b_6)

        self.b_minus = QPushButton("-", self)
        self.hbox_second.addWidget(self.b_minus)

        self.b_7 = QPushButton("7", self)
        self.hbox_third.addWidget(self.b_7)

        self.b_8 = QPushButton("8", self)
        self.hbox_third.addWidget(self.b_8)

        self.b_9 = QPushButton("9", self)
        self.hbox_third.addWidget(self.b_9)

        self.b_multy = QPushButton("*", self)
        self.hbox_third.addWidget(self.b_multy)

        self.b_zero = QPushButton("0", self)
        self.hbox_result.addWidget(self.b_zero)

        self.b_float = QPushButton(".", self)
        self.hbox_result.addWidget(self.b_float)

        self.b_result = QPushButton("=", self)
        self.hbox_result.addWidget(self.b_result)

        self.b_divide = QPushButton("/", self)
        self.hbox_result.addWidget(self.b_divide)



        self.b_result.clicked.connect(self._result)


        self.b_1.clicked.connect(lambda: self._button("1"))
        self.b_2.clicked.connect(lambda: self._button("2"))
        self.b_3.clicked.connect(lambda: self._button("3"))
        self.b_4.clicked.connect(lambda: self._button("4"))
        self.b_5.clicked.connect(lambda: self._button("5"))
        self.b_6.clicked.connect(lambda: self._button("6"))
        self.b_7.clicked.connect(lambda: self._button("7"))
        self.b_8.clicked.connect(lambda: self._button("8"))
        self.b_9.clicked.connect(lambda: self._button("9"))
        self.b_zero.clicked.connect(lambda: self._button("0"))
        self.b_float.clicked.connect(lambda: self._button("."))
        self.b_plus.clicked.connect(lambda: self._button("+"))
        self.b_minus.clicked.connect(lambda: self._button("-"))
        self.b_multy.clicked.connect(lambda: self._button("*"))
        self.b_divide.clicked.connect(lambda: self._button("/"))

    def _button(self, param):
        global line
        line = self.input.text()
        self.input.setText(line + param)
        line=line+param

    def _operation(self, op):
        self.num_1 = float(self.input.text())
        self.op = op
        self.input.setText("")

    def _result(self):
        D=[]
        a=""
        for i in range(len(line)):
            if line[i]!="+" and line[i]!="-" and line[i]!="*" and line[i]!="/":
                a+=line[i]
            else:
                D.append(a)
                D.append(line[i])
                D.append(line[i+1:len(line)+1])
        D.append(a)
        if D[1]=="+":
            ans=float(D[0])+float(D[2])
        elif D[1]=="-":
            ans=float(D[0])-float(D[2])
        elif D[1]=="*":
            ans=float(D[0])*float(D[2])
        elif D[1]=="/":
            if D[2]=="0":
                return self.input.setText(str("ZERO ERROR"))
            ans=float(D[0])/float(D[2])
        self.ans=float(ans)
        return self.input.setText(str(self.ans))
        print(ans)

app = QApplication(sys.argv)

win = Calculator()
win.show()

sys.exit(app.exec_())