import json
from xml.etree import ElementTree


class AbletonComponent:
    def __init__(self, root: ElementTree.Element):
        for annotation_param_name, annotation_param_type in self.__annotations__.items():
            initialized_value = self.init_python_object_from_annotation(
                root, annotation_param_name, annotation_param_type
            )
            setattr(self, annotation_param_name, initialized_value)

    def init_python_object_from_annotation(
        self, root: ElementTree.Element, annotation_param_name: str, annotation_param_type
    ):
        param_name = self.snake_to_camel(annotation_param_name)

        # we look in the node attributes first
        if param_name in root.attrib:
            return annotation_param_type(root.attrib[param_name])

        # we look in the nodes' children

        node = root.find(param_name)

        is_native_type = annotation_param_type in [int, str]
        is_bool = annotation_param_type == bool
        is_dict = annotation_param_type == dict
        is_list_type = hasattr(annotation_param_type, "__origin__") and issubclass(
            annotation_param_type.__origin__, list
        )
        is_ableton_component = issubclass(annotation_param_type, AbletonComponent)

        if is_native_type:
            new_param_value = list(node.attrib.values())[0]

        elif is_bool:
            new_param_value = list(node.attrib.values())[0] == "true"

        elif is_dict:
            new_param_value = json.loads(list(node.attrib.values())[0])

        elif is_list_type:
            ableton_component = annotation_param_type.__args__[0]
            new_param_value = [
                ableton_component(node) for node in root.find(param_name).findall("./")
            ]
            annotation_param_type = list

        elif is_ableton_component:
            new_param_value = node

        else:
            return None

        initialized_value = annotation_param_type(new_param_value)  # casts to python object
        return initialized_value

    def snake_to_camel(self, input_string):
        parts = input_string.split("_")
        camel_case = "".join(
            [part.capitalize() if part.upper() != part else part for part in parts]
        )
        return camel_case
