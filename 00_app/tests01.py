# DLMT().Duplicate_Faces()
# DLMT().Extract_Faces()
# DLMT().Combine_Objects()
# DLMT().Separate_Objects()

# DLMT().Outline_Renamer()
# DLMT().Check_Ngons()

# Entrar no modo de Compound
# Dar zoom

# def my_func(msg:list) -> str:
#     msg.

# import sys
# from Qt import QtWidgets

# app = QtWidgets.QApplication(sys.argv)
# button = QtWidgets.QPushButton("Hello World")
# button.show()
# app.exec_()

# from Qt import __binding__

# if __binding__ in ('PySide2', 'PyQt5'):
#     print('Qt5 binding available')
# elif __binding__ in ('PySide', 'PyQt4'):
#     print('Qt4 binding available.')
# else:
#     print('No Qt binding available.')

# import os
# print(os.path.dirname(__file__))
# print(os.getcwd())
# print("test")

# import os
# import sys
# import webbrowser

# try:
#     from PySide6.QtCore import QObject, Qt
#     print("PySide6")
# except ImportError:
#     from PySide2.QtCore import QObject, Qt
#     print("PySide2")

# from Qt import QtWidgets, QtGui, QtCore, QtCompat

# if __name__ == "__main__":
#     print(f"- Running the {__file__} file.")
#     # from dl_maya_toolkit_ui import DlMayaToolkit
#     from dl_maya_toolkit_ui import *
#     app = QtWidgets.QApplication(sys.argv)
#     dlmt_ui = DlMayaToolkit()
#     app.exec_()




###################################################################


# import sys
# import importlib

# app_module_path = 'D:\\Dropbox\\DEV\\DL_Maya_Toolkit\\00_app'
# if app_module_path not in sys.path:
#     sys.path.append(app_module_path)

# try:
#     from PySide6.QtCore import QObject, Qt
#     print("- PySide6")
# except ImportError:
#     from PySide2.QtCore import QObject, Qt
#     print("- PySide2")

# import maya.OpenMayaUI as omui
# import shiboken2
# from maya.app.general.mayaMixin import MayaQWidgetDockableMixin

# from Qt import QtWidgets

# def mayaMainWindow():
#     mainWindowPointer = omui.MQtUtil.mainWindow()
#     return shiboken2.wrapInstance(int(mainWindowPointer), QtWidgets.QWidget)

# class MyWindow(MayaQWidgetDockableMixin, QtWidgets.QDialog):
#     def __init__(self, parent=mayaMainWindow()):
#         super(MyWindow, self).__init__(parent)

#         # UI code

#         from dlmt import dl_maya_toolkit_ui
#         importlib.reload(dl_maya_toolkit_ui)
#         ui=dl_maya_toolkit_ui.DlMayaToolkit()
#         ui.dlmt_ui.show()

# myWindow = MyWindow()
# myWindow.show(dockable=True)

#######################

# import sys
# import importlib

# app_module_path = 'D:\\Dropbox\\DEV\\DL_Maya_Toolkit\\00_app'
# if app_module_path not in sys.path:
#     sys.path.append(app_module_path)

# from dlmt import dl_maya_toolkit_ui
# importlib.reload(dl_maya_toolkit_ui)
# ui=dl_maya_toolkit_ui.DlMayaToolkit()
# ui.dlmt_ui.show()





#######################################################################################


rename_str = "wood_####_bench"
print(rename_str)
hashtag = None
increment = 0

print(rename_str.find("#"))
print(rename_str.rfind("#"))

if "#" in rename_str:
    hashtag = rename_str[rename_str.find("#"):rename_str.rfind("#")+1]
    num_padding = len(hashtag)
    
    rename_split1 = rename_str[:rename_str.find("#")]
    rename_split2 = rename_str[rename_str.rfind("#")+1:]

    rename_str = rename_split1 + str(increment).zfill(num_padding) + rename_split2

print("- Hashtag: ", hashtag)
print("- Split1: ", rename_split1)
print("- Split2: ", rename_split2)
print("- Rename Str: ", rename_str)
