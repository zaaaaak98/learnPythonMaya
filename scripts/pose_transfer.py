from maya import cmds

def get_selected_namespaces():
    """Get list of namespaces for selected rigs

        :return:
            list

    """
    selection = cmds.ls(selection=True)
    if not selection:
        return []

    namespaces_list = []

    for ctrl in selection:
        #extract namespace from control
        namespace = ctrl.split(":")[0]

        #add namespace to list of namespaces

        if namespace not in namespaces_list:
            namespaces_list.append(namespace)

    return namespaces_list

def get_attrs_from_node(ctrl_node):
    """Get attribute names from single node

    :param
        ctrl_node(str):  Name of the node

    :return:
        list: List of short attribute names
    """
    attributes = cmds.listAnimatable(ctrl_node)
    if not attributes:
        return []

    attr_names = []

    for full_attr in attributes:
        attr_name = full_attr.split(".")[-1]
        attr_names.append(attr_name)

    print(attr_names)