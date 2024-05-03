import maya.cmds as cmds


class DLMT():
    def __init__(self) -> None:
        self.TOOL_NAME = "DL_Maya_Toolkit"
        self.TOOL_VERSION = "v1.0"

    def dialog_message(self, msg:str) -> None:
        cmds.confirmDialog(title=self.TOOL_NAME, message=msg, icon="information", button="OK")

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

                group_name = DLMT().group_name()
                cmds.select(group_name)
                cmds.ungroup()

    def Combine_Objects(self):
        objs = self.selected_objects()

        if objs:
            if len(objs) > 1:
                # Check if selected object is inside of a Group
                group_name = self.group_name()

                cmds.CombinePolygons()
                self.clear_history()

                if group_name:
                    # If the Group exists, move the Combined object back to it
                    if cmds.objExists(group_name):
                        cmds.parent(cmds.ls(selection=True), group_name)

                    # If not, create a Group with the same name
                    else:
                        cmds.group(name=group_name)
            else:
                self.dialog_message("Please select two or more objects to Combine!")

    def Separate_Objects(self):
        selected_object = self.selected_objects()

        if selected_object:
            obj_name = selected_object[0]

            try:
                # It will Separate the objects inside of a Group
                cmds.polySeparate()
                self.clear_history()

                self.rename_objects(obj_name)

                # Select the Group (will be the same name as the selected object), and Ungroup it
                cmds.select(obj_name)
                cmds.ungroup()
                cmds.CenterPivot()
            except:
                self.dialog_message("Please select a combined object to Separate!")

    def Outline_Renamer(self):
        outliner_layers = cmds.ls(selection=True)
        
        seq = 1
        if outliner_layers:
            for layer in outliner_layers:
                cmds.rename(layer, f"building_00{seq}_proxy")
                seq += 1
        else:
            self.dialog_message("Please select one or more layers in Outliner!")

    def Check_Ngons(self):
        selected_objects = self.selected_objects()

        if selected_objects:
            for obj in selected_objects:
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
                    self.dialog_message(f"{len(ngon_list)} Ngons has been found!")

                elif len(ngon_list) > 1:
                    cmds.select(ngon_list)
                    self.dialog_message(f"{len(ngon_list)} Ngons have been found!")
