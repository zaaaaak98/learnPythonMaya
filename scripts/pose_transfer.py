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

    return attr_names

def get_pose_dict(namespace):
    """

    :param namespace(str): Filter selection by namespace
    :return:
        dict: Dictionary of controls with attributes and their values
    """
    #get selection
    selection = cmds.ls(selection=True)
    if not selection:
        print("bug")
        return {}
    pose_dict = {}
    for ctrl in selection:
        # filter out the selection by the namespace
        if not ctrl.startswith(namespace):
            continue
        # get attributes
        animatable_attrs = get_attrs_from_node(ctrl)
        if not animatable_attrs:
            print("ping")
            continue
        #build dictionary
        for attr in animatable_attrs:
            ctrl_name = ctrl.split(':')[-1]
            full_attr = '{}.{}'.format(ctrl_name, attr)
            attr_value = '{}.{}'.format(ctrl, attr)
            value = cmds.getAttr(attr_value)
            # {'ctrl.attr' : attr_value}
            pose_dict[full_attr] = value


        #put together selection with attributes we've got
        #build dictionary
    return pose_dict