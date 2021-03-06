import os
import sys
import insert
import cv2
import datetime
import mtcnn
import first
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import QPalette, QBrush, QPixmap, QIcon
# from mtcnn_facenet.face_recognize import ddd, return_name
import matplotlib.pyplot as plt

import init_
import pymysql

show = ''

# 打开数据库连接
conn = pymysql.connect(host="rm-bp15cnp93v67pbl3u7o.mysql.rds.aliyuncs.com",
                       user="sa",
                       passwd="dq@Zcz5@KK2finh",
                       db="punched_card",
                       charset="utf8")
cursor = conn.cursor()

face_detector = mtcnn.MTCNN()
confidence_t = 0.99


def get_face(img, box):
    x1, y1, width, height = box
    x1, y1 = abs(x1), abs(y1)
    x2, y2 = x1 + width, y1 + height
    face = img[y1:y2, x1:x2]
    return face, (x1, y1), (x2, y2)


class WinInsert(QMainWindow, insert.Ui_insert):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("编辑信息")
        self.setWindowIcon(QIcon(r'img\insert_on.png'))
        self.xx = 0
        # self.setWindowIcon()
        self.cap = cv2.VideoCapture(0)
        self.pushButton.setVisible(False)
        self.pushButton.clicked.connect(self.ookk)
        self.pushButton_2.setVisible(False)
        self.pushButton_2.clicked.connect(self.cancel)
        self.timer_camera = QtCore.QTimer()
        self.timer_camera.timeout.connect(self.show_camera)
        self.photograph.clicked.connect(self.shoot)
        self.out.clicked.connect(self.toinit)
        self.gather.clicked.connect(self.add_info)
        self.update.clicked.connect(self.del_info)
        ##########################################################
        flag = self.cap.open(0)
        if not flag:
            msg = QtWidgets.QMessageBox.warning(self, u"Warning", u"请检测相机与电脑是否连接正确",
                                                buttons=QtWidgets.QMessageBox.Ok,
                                                defaultButton=QtWidgets.QMessageBox.Ok)
        else:
            self.timer_camera.start(30)

    def show_camera(self):
        ret, self.image = self.cap.read()
        # show = cv2.resize(self.image, (780, 500))
        self.image = cv2.flip(self.image, 1)
        self.image = cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB)
        results = face_detector.detect_faces(self.image)
        for res in results:
            if res['confidence'] < confidence_t:
                continue
            face, pt_1, pt_2 = get_face(self.image, res['box'])
            cv2.rectangle(self.image, pt_1, pt_2, (0, 0, 255), 2)
        showImage = QtGui.QImage(self.image.data, self.image.shape[1], self.image.shape[0], QtGui.QImage.Format_RGB888)
        self.camera.setPixmap(QtGui.QPixmap.fromImage(showImage))

    def shoot(self):
        self.timer_camera.stop()
        ret, self.image = self.cap.read()
        # show = cv2.resize(self.image, (780, 500))
        self.image = cv2.flip(self.image, 1)
        self.image = cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB)
        # date_str = datetime.datetime.strftime(datetime.datetime.now(), '%Y_%m_%d_%H_%M_%S')
        # date_str = date_str + '.jpg'
        # path = os.path.join('images_save', date_str)
        # plt.imsave(path, show)
        # plt.imshow(show)
        # plt.show()
        # self.cap.release()
        self.photograph.setEnabled(False)
        self.gather.setVisible(False)
        self.update.setVisible(False)
        self.pushButton.setVisible(True)
        self.pushButton_2.setVisible(True)

    def ookk(self):
        global show
        show = self.image
        self.xx = 1
        self.cap.release()
        self.pushButton.setVisible(False)
        self.pushButton_2.setVisible(False)
        self.gather.setVisible(True)
        self.update.setVisible(True)

    def cancel(self):
        self.xx = 0
        self.pushButton.setVisible(False)
        self.pushButton_2.setVisible(False)
        self.gather.setVisible(True)
        self.update.setVisible(True)
        self.photograph.setEnabled(True)
        self.timer_camera.start(30)

    def del_info(self):
        snum = self.num_text.text()
        sname = self.name_text.text()
        sql_find = "SELECT * FROM `punched_card`.`student` WHERE `sno` = '{}' AND `name` = '{}' ORDER BY `sno` DESC".format(
            snum, sname)
        cursor.execute(sql_find)
        lines = cursor.fetchall()
        if lines:
            sql_delete = 'DELETE FROM `punched_card`.`student` WHERE `sno`=' + snum
            cursor.execute(sql_delete)
            conn.commit()
            name = sname + ".jpg"
            path = os.path.join('mtcnn_facenet/face_dataset', name)
            os.remove(path)
            # first.update_face_embeddings()
            QtWidgets.QMessageBox.information(self, u"Warning", u"删除成功！！",
                                              buttons=QtWidgets.QMessageBox.Ok,
                                              defaultButton=QtWidgets.QMessageBox.Ok)
        else:
            QtWidgets.QMessageBox.warning(self, u"Warning", u"请输入正确的学号和姓名！",
                                          buttons=QtWidgets.QMessageBox.Ok,
                                          defaultButton=QtWidgets.QMessageBox.Ok)

    def add_info(self):
        if self.xx == 0:
            QtWidgets.QMessageBox.warning(self, u"Warning", u"请先拍照！",
                                          buttons=QtWidgets.QMessageBox.Ok,
                                          defaultButton=QtWidgets.QMessageBox.Ok)
        else:
            snum = self.num_text.text()
            sname = self.name_text.text()

            # 判断是否是已经录入的信息
            sql_find = "SELECT * FROM `punched_card`.`student` WHERE `sno` = {} ORDER BY `sno` DESC".format(
                snum)
            cursor.execute(sql_find)
            lines = cursor.fetchall()
            if lines or sname == '' or snum == '':
                QtWidgets.QMessageBox.warning(self, u"Warning", u"请输入正确的学号和姓名",
                                              buttons=QtWidgets.QMessageBox.Ok,
                                              defaultButton=QtWidgets.QMessageBox.Ok)
            else:
                sql_insert = "INSERT INTO student(sno, name, picture) VALUES ('{}', '{}', %s)".format(snum, sname)
                cursor.execute(sql_insert, (pymysql.Binary(show)))
                # plt.imshow(show)
                # plt.show()
                conn.commit()
                name = sname + ".jpg"
                path = os.path.join('mtcnn_facenet/face_dataset', name)
                plt.imsave(path, show)
                # first.update_face_embeddings()
                QtWidgets.QMessageBox.information(self, u"Warning", u"录入成功！",
                                                  buttons=QtWidgets.QMessageBox.Ok,
                                                  defaultButton=QtWidgets.QMessageBox.Ok)

    def toinit(self):
        global init
        init = init_.initshow()
        self.cap.release()
        self.close()
        init.show()
        first.update_face_embeddings()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = WinInsert()
    win.show()
    sys.exit(app.exec_())
