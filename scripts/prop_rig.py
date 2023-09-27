from maya import cmds


def createProp(prop_type):
    ctrl_name = "control"
    geo_name = "prop"

    ctrl = cmds.circle(name=ctrl_name, radius=2, normal=[0, 1, 0])
    ctrl_node = ctrl[0]

    if prop_type == "cube":
        prop = cmds.polyCube(name=geo_name)
    elif prop_type == "sphere":
        prop = cmds.polySphere(name=geo_name)
    elif prop_type == "cone":
        prop = cmds.polyCone(name=geo_name)
    else:
        cmds.warning("Invalid prop_type option. Using cube as default")
        prop = cmds.polyCube(name=geo_name)

    prop_node = prop[0]

    cmds.parent(prop_node, ctrl_node)
    cmds.select(ctrl_node)


    return ctrl_node
