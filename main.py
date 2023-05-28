import psycopg2
import sys

from PyQt5.QtWidgets import (QApplication, QWidget,
                             QTabWidget, QAbstractScrollArea,
                             QVBoxLayout, QHBoxLayout,
                             QTableWidget, QGroupBox,
                         QTableWidgetItem, QPushButton, QMessageBox)

class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()

        self._connect_to_db()

        self.setWindowTitle("Shedule")

        self.vbox = QVBoxLayout(self)

        self.tabs = QTabWidget(self)
        self.vbox.addWidget(self.tabs)

        self._create_week1_tab()
        self._create_week2_tab()
        self._create_teachers_tab()
        self._create_subjects_tab()

    def _connect_to_db(self):
        self.conn = psycopg2.connect(database='postgres',
                                user='postgres',
                                password='postgres',
                                host='localhost',
                                port='5432')
        self.cursor = self.conn.cursor()

    def _create_week1_tab(self):
        self.shedule_tab = QWidget()
        self.tabs.addTab(self.shedule_tab, "Week1")

        self.monday_gbox1 = QGroupBox("Monday")
        self.tuesday_gbox1 = QGroupBox("Tuesday")
        self.wednesday_gbox1 = QGroupBox("Wednesday")
        self.thursday_gbox1 = QGroupBox("Thursday")
        self.friday_gbox1 = QGroupBox("Friday")
        self.saturday_gbox1 = QGroupBox("Saturday")

        self.svbox = QVBoxLayout()
        self.shbox1 = QHBoxLayout()
        self.shbox2 = QHBoxLayout()
        self.shbox3 = QHBoxLayout()
        self.shbox4 = QHBoxLayout()

        self.svbox.addLayout(self.shbox1)
        self.svbox.addLayout(self.shbox2)
        self.svbox.addLayout(self.shbox3)
        self.svbox.addLayout(self.shbox4)

        self.shbox1.addWidget(self.monday_gbox1)
        self.shbox1.addWidget(self.tuesday_gbox1)
        self.shbox2.addWidget(self.wednesday_gbox1)
        self.shbox2.addWidget(self.thursday_gbox1)
        self.shbox3.addWidget(self.friday_gbox1)
        self.shbox3.addWidget(self.saturday_gbox1)

        self._create_monday1_table(self.monday_gbox1,1,1)
        self._create_tuesday1_table(self.tuesday_gbox1,2,1)
        self._create_wednesday1_table(self.wednesday_gbox1,3,1)
        self._create_thursday1_table(self.thursday_gbox1,4,1)
        self._create_friday1_table(self.friday_gbox1,5,1)
        self._create_saturday1_table(self.saturday_gbox1,6,1)

        self.update_shedule1_button = QPushButton("Update1")
        self.shbox4.addWidget(self.update_shedule1_button)
        self.update_shedule1_button.clicked.connect(self._update_shedule1)

        self.shedule_tab.setLayout(self.svbox)
    def _create_week2_tab(self):
        self.shedule_tab = QWidget()
        self.tabs.addTab(self.shedule_tab, "Week2")

        self.monday_gbox2 = QGroupBox("Monday")
        self.tuesday_gbox2 = QGroupBox("Tuesday")
        self.wednesday_gbox2 = QGroupBox("Wednesday")
        self.thursday_gbox2 = QGroupBox("Thursday")
        self.friday_gbox2 = QGroupBox("Friday")
        self.saturday_gbox2 = QGroupBox("Saturday")

        self.svbox = QVBoxLayout()
        self.shbox1 = QHBoxLayout()
        self.shbox2 = QHBoxLayout()
        self.shbox3 = QHBoxLayout()
        self.shbox4 = QHBoxLayout()

        self.svbox.addLayout(self.shbox1)
        self.svbox.addLayout(self.shbox2)
        self.svbox.addLayout(self.shbox3)
        self.svbox.addLayout(self.shbox4)

        self.shbox1.addWidget(self.monday_gbox2)
        self.shbox1.addWidget(self.tuesday_gbox2)
        self.shbox2.addWidget(self.wednesday_gbox2)
        self.shbox2.addWidget(self.thursday_gbox2)
        self.shbox3.addWidget(self.friday_gbox2)
        self.shbox3.addWidget(self.saturday_gbox2)

        self._create_monday2_table(self.monday_gbox2,1,2)
        self._create_tuesday2_table(self.tuesday_gbox2,2,2)
        self._create_wednesday2_table(self.wednesday_gbox2,3,2)
        self._create_thursday2_table(self.thursday_gbox2,4,2)
        self._create_friday2_table(self.friday_gbox2,5,2)
        self._create_saturday2_table(self.saturday_gbox2,6,2)

        self.update_shedule2_button = QPushButton("Update2")
        self.shbox4.addWidget(self.update_shedule2_button)
        self.update_shedule2_button.clicked.connect(self._update_shedule2)

        self.shedule_tab.setLayout(self.svbox)
    def _create_monday1_table(self,gbox,day,week):
        self.monday1_table = QTableWidget()
        self.monday1_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.monday1_table.setColumnCount(5)
        self.monday1_table.setHorizontalHeaderLabels(["Subject", "Time", "Room", "",""])

        self._update_day_table(self.monday1_table,day,week)

        self.mvbox = QVBoxLayout()
        self.mvbox.addWidget(self.monday1_table)
        gbox.setLayout(self.mvbox)
    def _create_monday2_table(self,gbox,day,week):
        self.monday2_table = QTableWidget()
        self.monday2_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.monday2_table.setColumnCount(5)
        self.monday2_table.setHorizontalHeaderLabels(["Subject", "Time", "Room", "",""])

        self._update_day_table(self.monday2_table,day,week)

        self.mvbox = QVBoxLayout()
        self.mvbox.addWidget(self.monday2_table)
        gbox.setLayout(self.mvbox)
    def _create_tuesday1_table(self,gbox,day,week):
        self.tuesday1_table = QTableWidget()
        self.tuesday1_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.tuesday1_table.setColumnCount(5)
        self.tuesday1_table.setHorizontalHeaderLabels(["Subject", "Time", "Room", "",""])

        self._update_day_table(self.tuesday1_table,day,week)

        self.tsbox = QVBoxLayout()
        self.tsbox.addWidget(self.tuesday1_table)
        gbox.setLayout(self.tsbox)
    def _create_tuesday2_table(self,gbox,day,week):
        self.tuesday2_table = QTableWidget()
        self.tuesday2_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.tuesday2_table.setColumnCount(5)
        self.tuesday2_table.setHorizontalHeaderLabels(["Subject", "Time", "Room", "",""])

        self._update_day_table(self.tuesday2_table,day,week)

        self.tsbox = QVBoxLayout()
        self.tsbox.addWidget(self.tuesday2_table)
        gbox.setLayout(self.tsbox)
    def _create_wednesday1_table(self,gbox,day,week):
        self.wednesday1_table = QTableWidget()
        self.wednesday1_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.wednesday1_table.setColumnCount(5)
        self.wednesday1_table.setHorizontalHeaderLabels(["Subject", "Time", "Room", "",""])

        self._update_day_table(self.wednesday1_table,day,week)

        self.wdbox = QVBoxLayout()
        self.wdbox.addWidget(self.wednesday1_table)
        gbox.setLayout(self.wdbox)
    def _create_wednesday2_table(self,gbox,day,week):
        self.wednesday2_table = QTableWidget()
        self.wednesday2_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.wednesday2_table.setColumnCount(5)
        self.wednesday2_table.setHorizontalHeaderLabels(["Subject", "Time", "Room", "",""])

        self._update_day_table(self.wednesday2_table,day,week)

        self.wdbox = QVBoxLayout()
        self.wdbox.addWidget(self.wednesday2_table)
        gbox.setLayout(self.wdbox)
    def _create_thursday1_table(self,gbox,day,week):
        self.thursday1_table = QTableWidget()
        self.thursday1_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.thursday1_table.setColumnCount(5)
        self.thursday1_table.setHorizontalHeaderLabels(["Subject", "Time", "Room", "",""])

        self._update_day_table(self.thursday1_table,day,week)

        self.thbox = QVBoxLayout()
        self.thbox.addWidget(self.thursday1_table)
        gbox.setLayout(self.thbox)
    def _create_thursday2_table(self,gbox,day,week):
        self.thursday2_table = QTableWidget()
        self.thursday2_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.thursday2_table.setColumnCount(5)
        self.thursday2_table.setHorizontalHeaderLabels(["Subject", "Time", "Room", "",""])

        self._update_day_table(self.thursday2_table,day,week)

        self.thbox = QVBoxLayout()
        self.thbox.addWidget(self.thursday2_table)
        gbox.setLayout(self.thbox)
    def _create_friday1_table(self,gbox,day,week):
        self.friday1_table = QTableWidget()
        self.friday1_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.friday1_table.setColumnCount(5)
        self.friday1_table.setHorizontalHeaderLabels(["Subject", "Time", "Room", "",""])

        self._update_day_table(self.friday1_table,day,week)

        self.fdbox = QVBoxLayout()
        self.fdbox.addWidget(self.friday1_table)
        gbox.setLayout(self.fdbox)
    def _create_friday2_table(self,gbox,day,week):
        self.friday2_table = QTableWidget()
        self.friday2_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.friday2_table.setColumnCount(5)
        self.friday2_table.setHorizontalHeaderLabels(["Subject", "Time", "Room", "",""])

        self._update_day_table(self.friday2_table,day,week)

        self.fdbox = QVBoxLayout()
        self.fdbox.addWidget(self.friday2_table)
        gbox.setLayout(self.fdbox)
    def _create_saturday2_table(self,gbox,day,week):
        self.saturday2_table = QTableWidget()
        self.saturday2_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.saturday2_table.setColumnCount(5)
        self.saturday2_table.setHorizontalHeaderLabels(["Subject", "Time", "Room", "",""])

        self._update_day_table(self.saturday2_table,day,week)

        self.stbox = QVBoxLayout()
        self.stbox.addWidget(self.saturday2_table)
        gbox.setLayout(self.stbox)
    def _create_saturday1_table(self,gbox,day,week):
        self.saturday1_table = QTableWidget()
        self.saturday1_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.saturday1_table.setColumnCount(5)
        self.saturday1_table.setHorizontalHeaderLabels(["Subject", "Time", "Room", "",""])

        self._update_day_table(self.saturday1_table,day,week)

        self.stbox = QVBoxLayout()
        self.stbox.addWidget(self.saturday1_table)
        gbox.setLayout(self.stbox)
    def _update_day_table(self,table,day,week):
        self.cursor.execute(f"SELECT * FROM timetable WHERE id_days='{day}_{week}'")
        day_table=table
        records = list(self.cursor.fetchall())

        day_table.setRowCount(len(records) + 1)
        AddButton = QPushButton("Add")
        for i, r in enumerate(records):
            r = list(r)
            joinButton = QPushButton("Join")
            DeleteButton = QPushButton("Delete")
            day_table.setItem(i, 0,
                                      QTableWidgetItem(str(r[2])))
            day_table.setItem(i, 1,
                                      QTableWidgetItem(str(r[4])))
            day_table.setItem(i, 2,
                                      QTableWidgetItem(str(r[3])))
            day_table.setCellWidget(i, 3, joinButton)
            joinButton.clicked.connect(lambda ch, num=i: self._change_day_from_table(day_table,num,day,week))
            day_table.setCellWidget(i, 4, DeleteButton)
            DeleteButton.clicked.connect(lambda ch, num=i: self._delete_class_from_table(day_table, num, day, week))
        day_table.setCellWidget(len(records),3, AddButton)
        AddButton.clicked.connect(lambda ch, num=len(records): self._add_class_(day_table,num,day,week))
        day_table.resizeRowsToContents()
    def _change_day_from_table(self,table,rowNum,day,week):
        self.cursor.execute(f"SELECT * FROM timetable where id_days='{day}_{week}'")
        records = list(self.cursor.fetchall())
        row = list()
        day_table=table
        for i in range(day_table.columnCount()):
            try:
                row.append(day_table.item(rowNum, i).text())
            except:
                row.append(None)
            print(row)

        self.cursor.execute(f"UPDATE timetable SET subject='{row[0]}', start_time='{row[1]}', room='{row[2]}' WHERE id_days='{day}_{week}' AND id='{records[rowNum][0]}'")
        self.conn.commit()
    def _add_class_(self, table,rowNum,day,week):
        day_table=table
        self.cursor.execute(f"SELECT * FROM timetable")
        records = list(self.cursor.fetchall())
        id=len(records) + 1
        row = list()
        for i in range(day_table.columnCount()):
            try:
                row.append(day_table.item(rowNum, i).text())
            except:
                row.append(None)
            print(row)
            print(row[0])
        #try:
        self.cursor.execute(f"INSERT INTO timetable (id,id_days, subject,start_time, room) VALUES ('{id}','{day}_{week}','{row[0]}','{row[1]}', '{row[2]}')")
        self.conn.commit()
    def _delete_class_from_table(self,table,rowNum,day,week):
        print(1)
        self.cursor.execute(f"SELECT * FROM timetable where id_days='{day}_{week}'")
        records = list(self.cursor.fetchall())
        day_table=table
        row = list()
        for i in range(day_table.columnCount()):
            try:
                row.append(day_table.item(rowNum, i).text())
            except:
                row.append(None)
        print(row)
        self.cursor.execute(f"DELETE FROM timetable WHERE id='{records[rowNum][0]}'")
        self.conn.commit()
    def _update_shedule1(self):
        self._update_day_table(self.monday1_table,1,1)
        self._update_day_table(self.tuesday1_table, 2, 1)
        self._update_day_table(self.wednesday1_table, 3, 1)
        self._update_day_table(self.thursday1_table, 4, 1)
        self._update_day_table(self.friday1_table, 5, 1)
        self._update_day_table(self.saturday1_table, 6, 1)
    def _update_shedule2(self):
        self._update_day_table(self.monday2_table,1,2)
        self._update_day_table(self.tuesday2_table, 2, 2)
        self._update_day_table(self.wednesday2_table, 3, 2)
        self._update_day_table(self.thursday2_table, 4, 2)
        self._update_day_table(self.friday2_table, 5, 2)
        self._update_day_table(self.saturday2_table, 6, 2)



    def _create_teachers_tab(self):
        self.shedule_tab = QWidget()
        self.tabs.addTab(self.shedule_tab, "Teachers")

        self.teacher_gbox = QGroupBox("Teacher")

        self.svbox = QVBoxLayout()
        self.shbox1 = QHBoxLayout()
        self.shbox2 = QHBoxLayout()

        self.svbox.addLayout(self.shbox1)
        self.svbox.addLayout(self.shbox2)

        self.shbox1.addWidget(self.teacher_gbox)

        self._create_teachers_table(self.teacher_gbox)

        self.update_teachers_button = QPushButton("Update")
        self.shbox2.addWidget(self.update_teachers_button)
        self.update_teachers_button.clicked.connect(self._update_teachers_list)

        self.shedule_tab.setLayout(self.svbox)
    def _create_teachers_table(self,gbox):
        self.teacher_table = QTableWidget()
        self.teacher_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.teacher_table.setColumnCount(4)
        self.teacher_table.setHorizontalHeaderLabels(["Full_name", "Subject",""])

        self._update_teacher_table()

        self.mvbox = QVBoxLayout()
        self.mvbox.addWidget(self.teacher_table)
        gbox.setLayout(self.mvbox)
    def _update_teacher_table(self):
        self.cursor.execute(f"SELECT * FROM teacher")
        records = list(self.cursor.fetchall())

        self.teacher_table.setRowCount(len(records) + 1)
        AddButton = QPushButton("Add")
        for i, r in enumerate(records):
            r = list(r)
            DeleteButton = QPushButton("Delete")
            joinButton = QPushButton("Join")
            self.teacher_table.setItem(i, 0,
                                      QTableWidgetItem(str(r[1])))
            self.teacher_table.setItem(i, 1,
                                      QTableWidgetItem(str(r[2])))
            self.teacher_table.setCellWidget(i, 2, joinButton)
            self.teacher_table.setCellWidget(i, 3, DeleteButton)
            joinButton.clicked.connect(lambda ch, num=i: self._change_teacher_list(num))
            DeleteButton.clicked.connect(lambda ch, num=i: self._delete_from_teacher_list(num))
        self.teacher_table.setCellWidget(len(records),2, AddButton)
        AddButton.clicked.connect(lambda ch, num=len(records): self._add_to_teacher_list(num))
        self.teacher_table.resizeRowsToContents()
    def _change_teacher_list(self, rowNum):
        row = list()
        for i in range(self.teacher_table.columnCount()):
            try:
                row.append(self.teacher_table.item(rowNum, i).text())
            except:
                row.append(None)
        self.cursor.execute(f"UPDATE teacher SET full_name='{row[0]}', subject='{row[1]}' WHERE id_teacher={rowNum}")
        self.conn.commit()
    def _add_to_teacher_list(self, rowNum):
        self.cursor.execute(f"SELECT * FROM teacher")
        records = list(self.cursor.fetchall())
        id_teacher=len(records) + 1
        print(id_teacher)
        row = list()
        for i in range(self.teacher_table.columnCount()):
            try:
                row.append(self.teacher_table.item(rowNum, i).text())
            except:
                row.append(None)
            print(row)
            print(row[0])
        #try:
        self.cursor.execute(f"INSERT INTO teacher (id_teacher, full_name, subject) VALUES ('{id_teacher}','{row[0]}','{row[1]}')")
        self.conn.commit()
        id_teacher+=1
        #except psycopg2.errors.SyntaxError:
        #    QMessageBox.about(self, "Error", "Enter all fields")
    def _delete_from_teacher_list(self, rowNum):
        row = list()
        for i in range(self.teacher_table.columnCount()):
            try:
                row.append(self.teacher_table.item(rowNum, i).text())
            except:
                row.append(None)
        print(row)
        self.cursor.execute(f"DELETE from teacher WHERE full_name='{row[0]}' and subject='{row[1]}'")
        self.conn.commit()
    def _update_teachers_list(self):
        self._update_teacher_table()


    def _create_subjects_tab(self):
        self.shedule_tab = QWidget()
        self.tabs.addTab(self.shedule_tab, "Subjects")

        self.subject_gbox = QGroupBox("Subject")

        self.svbox = QVBoxLayout()
        self.shbox1 = QHBoxLayout()
        self.shbox2 = QHBoxLayout()

        self.svbox.addLayout(self.shbox1)
        self.svbox.addLayout(self.shbox2)

        self.shbox1.addWidget(self.subject_gbox)

        self._create_subjects_table(self.subject_gbox)

        self.update_subjects_button = QPushButton("Update")
        self.shbox2.addWidget(self.update_subjects_button)
        self.update_subjects_button.clicked.connect(self._update_subjects_list)

        self.shedule_tab.setLayout(self.svbox)
    def _create_subjects_table(self,gbox):
        self.subject_table = QTableWidget()
        self.subject_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.subject_table.setColumnCount(3)
        self.subject_table.setHorizontalHeaderLabels(["Subject","",""])

        self._update_subject_table()

        self.mvbox = QVBoxLayout()
        self.mvbox.addWidget(self.subject_table)
        gbox.setLayout(self.mvbox)
    def _update_subject_table(self):
        self.cursor.execute(f"SELECT * FROM subject")
        records = list(self.cursor.fetchall())

        self.subject_table.setRowCount(len(records) + 1)
        AddButton = QPushButton("Add")
        for i, r in enumerate(records):
            r = list(r)
            DeleteButton=QPushButton("Delete")
            joinButton = QPushButton("Join")
            self.subject_table.setItem(i, 0,
                                      QTableWidgetItem(str(r[0])))
            self.subject_table.setCellWidget(i, 1, joinButton)
            self.subject_table.setCellWidget(i,2,DeleteButton)
            joinButton.clicked.connect(lambda ch, num=i: self._change_subject_list(num))
            DeleteButton.clicked.connect(lambda ch, num=i: self._delete_from_subject_list(num))
        self.subject_table.setCellWidget(len(records),1, AddButton)
        AddButton.clicked.connect(lambda ch, num=len(records): self._add_to_subject_list(num))
        self.subject_table.resizeRowsToContents()
    def _change_subject_list(self, rowNum):
        row = list()
        for i in range(self.subject_table.columnCount()):
            try:
                row.append(self.subject_table.item(rowNum, i).text())
            except:
                row.append(None)
            print(row)
            print(row[0])
        self.cursor.execute(f"UPDATE subject SET subject='{row[0]}' where id='{rowNum}'")
        self.conn.commit()
    def _add_to_subject_list(self, rowNum):
        self.cursor.execute(f"SELECT * FROM subject")
        records = list(self.cursor.fetchall())
        id_subject=len(records) + 1
        print(id_subject)
        row = list()
        for i in range(self.subject_table.columnCount()):
            try:
                row.append(self.subject_table.item(rowNum, i).text())
            except:
                row.append(None)
            print(row)
            print(row[0])
        #try:
        self.cursor.execute(f"INSERT INTO subject (subject) VALUES ('{row[0]}')")
        self.conn.commit()
        id_subject+=1
    def _delete_from_subject_list(self, rowNum):
        row = list()
        for i in range(self.subject_table.columnCount()):
            try:
                row.append(self.subject_table.item(rowNum, i).text())
            except:
                row.append(None)
        print(row)
        self.cursor.execute(f"DELETE from subject WHERE subject='{row[0]}'")
        self.conn.commit()
    def _update_subjects_list(self):
        self._update_subject_table()


app = QApplication(sys.argv)
win = MainWindow()
win.show()
sys.exit(app.exec_())
