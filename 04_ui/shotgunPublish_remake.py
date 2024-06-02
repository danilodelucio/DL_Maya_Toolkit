# -----------------------------------------------------------------------------------
#  Shotgun Publish Remake
#  Version: v01.0
#  Author: Danilo de Lucio
#  Website: www.danilodelucio.com
# -----------------------------------------------------------------------------------

import os
import sys
import webbrowser

from Qt import QtWidgets, QtGui, QtCore, QtCompat
from PyQt5.QtGui import QIcon, QPixmap


#*******************************************************************
# VARIABLE
TITLE = os.path.splitext(os.path.basename(__file__))[0]
CURRENT_PATH = os.path.dirname(__file__)
IMG_PATH = CURRENT_PATH + "/imgs/{}.png"


#*******************************************************************
# CLASS
class SPR_UI():
    def __init__(self):
        # BUILD local ui path
        path_ui = ("/").join([os.path.dirname(__file__), TITLE + ".ui"])

        # LOAD ui with absolute path
        self.wgPublish = QtCompat.loadUi(path_ui)

        self.msg_button = "{} button has been pressed!"

        # Load icons/images
        self.wgPublish.setWindowIcon(QIcon(QPixmap(IMG_PATH.format("shotgun_logo"))))
        # self.wgPublish.label_logo.setScaledContents(True)
        self.wgPublish.label_logo.setPixmap(QPixmap(IMG_PATH.format("shotgun_logo")))
        self.wgPublish.label_rightArrow.setPixmap(QPixmap(IMG_PATH.format("rightArrow_icon")))
        self.wgPublish.label_publishIcon.setPixmap(QPixmap(IMG_PATH.format("publish_icon")))

        self.wgPublish.button_project.setIcon(QIcon(QPixmap(IMG_PATH.format("arrow_icon"))))
        self.wgPublish.button_folder.setIcon(QIcon(QPixmap(IMG_PATH.format("folder_icon"))))
        self.wgPublish.button_refresh.setIcon(QIcon(QPixmap(IMG_PATH.format("circled_arrow_icon"))))
        self.wgPublish.button_bin.setIcon(QIcon(QPixmap(IMG_PATH.format("bin_icon"))))
        self.wgPublish.button_expand.setIcon(QIcon(QPixmap(IMG_PATH.format("expand_icon"))))
        self.wgPublish.button_shrink.setIcon(QIcon(QPixmap(IMG_PATH.format("shrink_icon"))))
        self.wgPublish.button_help.setIcon(QIcon(QPixmap(IMG_PATH.format("help_icon"))))


        # Signals
        self.wgPublish.button_validate.clicked.connect(self.press_validate)
        self.wgPublish.button_publish.clicked.connect(self.press_publish)
        self.wgPublish.button_folder.clicked.connect(self.press_folder)
        self.wgPublish.button_refresh.clicked.connect(self.press_refresh)
        self.wgPublish.button_bin.clicked.connect(self.press_bin)
        self.wgPublish.button_expand.clicked.connect(self.press_expand)
        self.wgPublish.button_shrink.clicked.connect(self.press_shrink)
        self.wgPublish.button_help.clicked.connect(self.press_help)
        self.wgPublish.button_project.clicked.connect(self.press_project)

        # SHOW the UI
        self.wgPublish.show()



    #************************************************************
    # PRESS
    def press_validate(self):
        self.print_info()
        print("The shot has been validated!\n")

    def press_publish(self):
        msg = "The shot has been published!".upper()
        div = "*" * len(msg)
        print(div)
        print(msg)
        print(div)

    def print_info(self):
        time_range = self.wgPublish.comboBox.currentText()
        preRoll_frames = self.wgPublish.spinBox.value()
        quick_select_set = self.wgPublish.lineEdit.text()

        print(f"""\n- Time Range: {time_range}\n- Pre Roll Frames: {preRoll_frames}\n- Quick Select Set: {quick_select_set}\n""")
    
    def press_folder(self):
        print(self.msg_button.format("FOLDER"))

    def press_refresh(self):
        print(self.msg_button.format("REFRESH"))

    def press_bin(self):
        print(self.msg_button.format("BIN"))

    def press_expand(self):
        print(self.msg_button.format("EXPAND"))

    def press_shrink(self):
        print(self.msg_button.format("SHRINK"))

    def press_help(self):
        print(self.msg_button.format("HELP"))

    def press_project(self):
        print(self.msg_button.format("PROJECT"))


#*******************************************************************
# START
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    classVar = SPR_UI()
    app.exec_()

