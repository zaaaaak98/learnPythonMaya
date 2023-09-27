from maya import cmds

def get_selected_namespaces():
    """Get list of namespaces for selected rigs

        :return:
            list

    """
    selection = cmds.ls(selection=True)
    if len(selection) == 0:
        return []

    namespaces_list = []

    for ctrl in selection:
        #extract namespace from control
        namespace = ctrl.split(":")[0]

        #add namespace to list of namespaces

        if not namespace in namespaces_list:
            namespaces_list.append(namespace)

    return namespaces_list
