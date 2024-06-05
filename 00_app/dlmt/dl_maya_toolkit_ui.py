# -----------------------------------------------------------------------------------
#  DL_Maya_Toolkit
#  Version: v01.0
#  Author: Danilo de Lucio
#  Website: www.danilodelucio.com
# -----------------------------------------------------------------------------------

# -----------------------------------------------------------------------------------
#  [Summary]
#  This tool is a collection of features to help Maya users speed up their workflows.
#
# -----------------------------------------------------------------------------------

import os
import sys
import webbrowser

print("- Initializing DL Maya Toolkit...")

try:
    from PySide6.QtCore import QObject, Qt
    print("- PySide6")
except ImportError:
    from PySide2.QtCore import QObject, Qt
    print("- PySide2")

from Qt import QtWidgets, QtGui, QtCore, QtCompat
import maya.cmds as cmds


# VARIABLES
TITLE = os.path.splitext(os.path.basename(__file__))[0]
SCRIPT_PATH = os.path.dirname(os.path.abspath(__file__))
IMG_PATH = SCRIPT_PATH + "/img/{}.png"
TOOL_NAME = "DL Maya Toolkit"


# CLASS
class DlMayaToolkit(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(DlMayaToolkit, self).__init__(parent)

        # Load UI file
        path_ui = SCRIPT_PATH + f"/{TITLE}.ui"
        self.dlmt_ui = QtCompat.loadUi(path_ui)

        self.setWindowTitle(TOOL_NAME)

        # Print button pressed
        self.button_pressed = "- {} button has been pressed!"
        
        # Load icons/images
        self.dlmt_ui.setWindowIcon(QtGui.QPixmap(IMG_PATH.format("dlmt_icon")))
        
        # Signals
        self.dlmt_ui.label_logo.setPixmap(QtGui.QPixmap(IMG_PATH.format("dlmt_logo_white")))
        self.dlmt_ui.button_duplicateFaces.clicked.connect(self.press_DuplicateFaces)
        self.dlmt_ui.button_extractFaces.clicked.connect(self.press_ExtractFaces)
        self.dlmt_ui.button_combineObjects.clicked.connect(self.press_CombineObjects)
        self.dlmt_ui.button_separateObjects.clicked.connect(self.press_SeparateObjects)
        self.dlmt_ui.button_checkNgons.clicked.connect(self.press_CheckNgons)
        self.dlmt_ui.button_outlineRenamer.clicked.connect(self.press_OutlineRenamer)
        self.dlmt_ui.button_website.clicked.connect(self.press_website)

	
    #####################################################################################
    # SIGNALS
    def press_DuplicateFaces(self):
        print(self.button_pressed.format("DUPLICATE FACES"))
        self.Duplicate_Faces()
        self.dlmt_ui.show()
	
    def press_ExtractFaces(self):
        print(self.button_pressed.format("EXTRACT FACES"))
        self.Extract_Faces()

    def press_CombineObjects(self):
        print(self.button_pressed.format("COMBINE OBJECTS"))
        self.Combine_Objects()

    def press_SeparateObjects(self):
        print(self.button_pressed.format("SEPARATE OBJECTS"))
        self.Separate_Objects()

    def press_OutlineRenamer(self):
        print(self.button_pressed.format("OUTLINER RENAMER"))
        self.Outline_Renamer()

    def press_CheckNgons(self):
        print(self.button_pressed.format("CHECK NGONS"))
        self.Check_Ngons()

    def press_website(self):
        print(self.button_pressed.format("WEBSITE"))
        webbrowser.open("https://danilodelucio.com")

    def show(self):
        self.dlmt_ui.show()

    #####################################################################################
    # DEFAULT METHODS
    def dialog_message(self, msg:str) -> None:
        cmds.confirmDialog(title=TOOL_NAME, message=msg, icon="information", button="OK")

    def selected_objects(self) -> list:
        obj_list = [obj for obj in cmds.ls(selection=True)]
        
        if len(obj_list) == 0:
            self.dialog_message("Please select an object!")
            return
        else:
            return obj_list

    def selected_faces(self) -> list:
        if self.selected_objects():
            faces_list = [face for face in cmds.ls(selection=True, flatten=True)]

            for face in faces_list:
                if "." in face: # Example: selected_object.f[4]
                    return faces_list
                else:
                    self.dialog_message("Please select one or more Faces!")

    def clear_history(self) -> None:
        cmds.delete(constructionHistory=True)

    def group_name(self) -> str:
        # Check if the selected object belongs to a group and returns the group name.
        selected_objs = cmds.ls(selection=True, type='transform', long=True)

        if len(selected_objs) == 0:
            return False
            
        first_selected_obj = str(selected_objs[0])
        count_pipe = first_selected_obj.count("|")

        if count_pipe > 1:
            # Slicing the Outliner hierarchy, like "|group|subgroup" without the obj_name
            outliner_hierarchy = first_selected_obj[first_selected_obj.find("|"):first_selected_obj.rfind("|")]

            return outliner_hierarchy
        else:
            return False

    def rename_objects(self, obj_name:str) -> None:
        count = 1
        for obj in cmds.ls(selection=True):
            cmds.rename(obj, f"{obj_name}_{count}")
            count += 1

    #####################################################################################
    # BUTTON METHODS
    def Duplicate_Faces(self):
        # The duplicated faces will be in the same group
        selected_obj = self.selected_objects()
        
        if selected_obj:
            obj_name = str(selected_obj[0]).split(".")[0]

            if self.selected_faces():
                cmds.DuplicateFace()
                self.clear_history()

                self.rename_objects(obj_name)
                
                cmds.select(obj_name)
                cmds.ungroup()
                cmds.CenterPivot()
                cmds.viewFit()

    def Extract_Faces(self):
        # The extracted faces will be in the same group
        selected_obj = self.selected_objects()

        if selected_obj:
            obj_name = str(selected_obj[0]).split(".")[0]

            if self.selected_faces():
                cmds.ExtractFace()
                self.clear_history()

                self.rename_objects(obj_name)
                cmds.CenterPivot()

                group_name = self.group_name()
                cmds.select(group_name)
                cmds.ungroup()
                cmds.viewFit()

    def Combine_Objects(self):
        try:
            objs = self.selected_objects()

            if objs:
                if len(objs) > 1:
                    # Check if selected object is inside of a Group
                    groupName = self.group_name()

                    cmds.CombinePolygons()
                    self.clear_history()
                    cmds.viewFit()

                    if groupName:
                        # If the Group exists, move the Combined object back to it
                        if cmds.objExists(groupName):
                            cmds.parent(cmds.ls(selection=True), groupName)

                        # If not, create a Group with the same name
                        else:
                            cmds.group(name=groupName)
                else:
                    self.dialog_message("Please select two or more objects to Combine!")

        except Exception as error:
            self.dialog_message(error)

    def Separate_Objects(self):
        selected_object = self.selected_objects()

        if selected_object:
            obj_name = selected_object[0]

            try:
                # It will Separate the objects inside of a Group
                cmds.polySeparate()
                self.clear_history()

                self.rename_objects(obj_name)

                # Select the Group (it will be the same name as the selected object), and Ungroup it
                cmds.select(obj_name)
                cmds.ungroup()
                cmds.CenterPivot()
                cmds.viewFit()
            except:
                self.dialog_message("Please select a combined object to Separate!")

    def Outline_Renamer(self):
        outliner_layers = cmds.ls(selection=True)
        
        if outliner_layers:
            ui = OutlinerRenamer()
            ui.exec_()
        else:
            self.dialog_message("Please select one or more items in the Outliner panel!")

    def Check_Ngons(self):
        selected_objs = self.selected_objects()

        if selected_objs:
            
            for obj in selected_objs:
                faces = cmds.polyListComponentConversion(obj, toFace=True)
                face_list = cmds.ls(faces, flatten=True)
                
                ngon_list = list()

                # Looping all faces from the selected object
                for face in face_list:
                    vertices = cmds.polyListComponentConversion(face, toVertex=True)
                    vtx_list = cmds.ls(vertices, flatten=True)

                    count_vtx = list()

                    # Couting the vertices and appending to the list
                    for vtx in vtx_list:
                        count_vtx.append(vtx)

                    if len(count_vtx) > 4:
                        ngon_list.append(face)

                if len(ngon_list) == 0:
                    self.dialog_message("Ngons not found!")
                    
                elif len(ngon_list) == 1:
                    cmds.select(ngon_list)
                    cmds.viewFit()
                    self.dialog_message(f"{len(ngon_list)} Ngons has been found!")

                elif len(ngon_list) > 1:
                    cmds.select(ngon_list)
                    cmds.viewFit()
                    self.dialog_message(f"{len(ngon_list)} Ngons have been found!")


class OutlinerRenamer(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(OutlinerRenamer, self).__init__(parent)

        # Load UI file
        path_ui = SCRIPT_PATH + "/dlmt_outliner_renamer_ui.ui"
        self.outliner_ui = QtCompat.loadUi(path_ui, self)

        self.setWindowTitle(TOOL_NAME + " - Outliner Renamer")

        # Print button pressed
        self.button_pressed = "- {} button has been pressed!"

        self.outliner_ui.button_rename.clicked.connect(self.press_Rename)
    
    def press_Rename(self):
        print(self.button_pressed.format("RENAME"))

        rename_str = str(self.outliner_ui.lineEdit_newName.text())
        hashtag = None

        outliner_layers = cmds.ls(selection=True)
        increment_value = self.outliner_ui.spinBox_increment.value()
        
        increment_num = increment_value
        seq = 1
        for layer in outliner_layers:
            if "#" in rename_str:
                hashtag = rename_str[rename_str.find("#"):rename_str.rfind("#")+1]
                # num_padding = hashtag.replace("#", "0")
                num_padding = str(increment_num).zfill(len(hashtag))
                rename_split1 = rename_str[:rename_str.find("#")]
                rename_split2 = rename_str[rename_str.rfind("#")+1:]

                new_rename_str = rename_split1 + num_padding + rename_split2
            else:
                new_rename_str = rename_str

            cmds.rename(layer, f"{new_rename_str}_{seq}")
            seq += 1
            increment_num += increment_value

        print(rename_str)
        self.outliner_ui.close()