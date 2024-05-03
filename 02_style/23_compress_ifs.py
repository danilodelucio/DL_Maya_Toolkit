# STYLE ***************************************************************************
# content = assignment (Python Advanced)
#
# date    = 2022-01-07
# email   = contact@alexanderrichtertd.com
#**********************************************************************************


# COMMENT --------------------------------------------------
# Not optimal
def set_color(ctrlList=None, color=None):

    def mc_setAttr(color_id) -> None:
        mc.setAttr(ctrlName + 'Shape.overrideEnabled', color_id)
        return
    
    for ctrlName in ctrlList:
        try:
            mc_setAttr(1)
        except:
            pass

        try:
            # Storing the options (as key) and the colors ID (as values) inside of a dict
            # Example: {OPTION:COLOR ID}
            color_dict = {1:4, 2:13, 3:25, 4:17, 5:17, 6:15, 7:6, 8:16}

            for option, color_id in color_dict.items():
                if color == option:
                    mc_setAttr(color_id)
        except:
            pass

# EXAMPLE
# set_color(['circle','circle1'], 8)