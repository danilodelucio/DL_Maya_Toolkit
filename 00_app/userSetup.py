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

import sys
import importlib
import maya.cmds as cmds


DLMT_NAME = "DL_Maya_Toolkit"
DLMT_TOOL = "put\\your\\file\\path\\here\\DL_Maya_Toolkit"
DLMT_ICON = DLMT_TOOL + "\\dlmt\\img\\dl_maya_toolkit_icon_shelf.png"
DLMT_CMD = """import sys
if 'dl_maya_toolkit_ui' not in sys.modules:
    import importlib
    from dlmt import dl_maya_toolkit_ui
    importlib.reload(dl_maya_toolkit_ui)
ui = dl_maya_toolkit_ui.DlMayaToolkit()
ui.show()
"""
DLMT_INIT = """\n// DL Maya Toolkit v01.0, built in June 2024.
// Copyright (c) 2024 Danilo de Lucio. All Rights Reserved. | www.danilodelucio.com
"""


# Add the module path to the Maya's environment
if DLMT_TOOL not in sys.path:
    sys.path.append(DLMT_TOOL)
    print(f"- The module path has been added: {DLMT_TOOL}")

try:
    from dlmt import dl_maya_toolkit_ui
    importlib.reload(dl_maya_toolkit_ui)
    print("- Module imported and reloaded successfully!")

except ImportError as e:
    print(f"Error importing module: {e}")


def create_dlmt_shelf():
    # Check if the shelf exists, if not create it
    if not cmds.shelfLayout(DLMT_NAME, exists=True):
        cmds.shelfLayout(DLMT_NAME, parent="ShelfLayout")
        cmds.shelfButton(label=DLMT_NAME, command=DLMT_CMD, image=DLMT_ICON, parent=DLMT_NAME)

        print(f"- The shelf {DLMT_NAME} has been created!")
        print(DLMT_INIT)

    else:
        print(DLMT_INIT)

cmds.evalDeferred(create_dlmt_shelf)
####################################### END OF DL_MAYA_TOOLKIT #######################################