import json
from typing import get_args, get_origin, get_type_hints
from xml.etree import ElementTree


class AbletonComponent:
    """
    AbletonComponent Class

    Base class for representing components in an Ableton Live project.

    Methods
    -------
    __init__(root: ElementTree.Element)
        Initializes an AbletonComponent instance.
    init_python_object_from_annotation(
        root: ElementTree.Element, annotation_param_name: str, annotation_param_type: type
        )
        Initializes a Python object from an annotation in the XML.
    snake_to_camel(input_string: str)
        Converts a snake_case string to camelCase.

    """

    def __init__(self, root: ElementTree.Element):
        """
        Initializes an AbletonComponent instance.

        Parameters
        ----------
        root : ElementTree.Element
            The root element of the XML representation of the Ableton component.
        """
        for annotation_param_name, annotation_param_type in get_type_hints(
            self.__class__
        ).items():
            initialized_value = self.init_python_object_from_annotation(
                root, annotation_param_name, annotation_param_type
            )
            setattr(self, annotation_param_name, initialized_value)

    def init_python_object_from_annotation(
        self, root: ElementTree.Element, annotation_param_name: str, annotation_param_type: type
    ):
        """
        Initializes a Python object from an annotation in the XML.

        Parameters
        ----------
        root : ElementTree.Element
            The root element of the XML representation of the Ableton component.
        annotation_param_name : str
            The name of the annotation parameter.
        annotation_param_type : type
            The type of the annotation parameter.

        Returns
        -------
        The initialized Python object.
        """
        param_name = self.snake_to_camel(annotation_param_name)

        # we look in the node attributes first
        if param_name in root.attrib:
            return annotation_param_type(root.attrib[param_name])

        # we look in the nodes' children

        node = root.find(param_name)
        origin = get_origin(annotation_param_type)
        annotation_args = get_args(annotation_param_type)

        is_native_type = annotation_param_type in [int, str, float]
        is_bool = annotation_param_type == bool
        is_dict = annotation_param_type == dict
        is_list_type = origin is list
        is_ableton_component = isinstance(annotation_param_type, type) and issubclass(
            annotation_param_type, AbletonComponent
        )

        if is_native_type:
            new_param_value = list(node.attrib.values())[0]

        elif is_bool:
            new_param_value = list(node.attrib.values())[0] == "true"

        elif is_dict:
            new_param_value = json.loads(list(node.attrib.values())[0])

        elif is_list_type:
            ableton_component = annotation_args[0]
            new_param_value = [ableton_component(child) for child in node.findall("./")]
            annotation_param_type = list

        elif is_ableton_component:
            new_param_value = node

        else:
            return None
        try:
            initialized_value = annotation_param_type(new_param_value)  # casts to python object
        except ValueError:
            error_message = (
                f"Parameter {param_name} with value {new_param_value} "
                f"is not type {annotation_param_type}"
            )
            print(error_message)
        return initialized_value

    def snake_to_camel(self, input_string):
        """
        Converts a snake_case string to camelCase.

        Parameters
        ----------
        input_string : str
            The input string in snake_case.

        Returns
        -------
        str
            The input string converted to camelCase.
        """
        parts = input_string.split("_")
        camel_case = "".join(
            [part.capitalize() if part.upper() != part else part for part in parts]
        )
        return camel_case
