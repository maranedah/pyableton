import json
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

    # Optional per-class mapping from a snake_case annotation name to alternative
    # XML tag names, used to bridge schema renames across Ableton Live versions
    # (e.g. Live 11 "MasterTrack" vs Live 12 "MainTrack"). Declared without a type
    # annotation so it never appears in ``__annotations__`` / gets parsed as a field.
    _aliases: "dict[str, list[str]]" = {}

    def __init__(self, root: ElementTree.Element):
        """
        Initializes an AbletonComponent instance.

        Parameters
        ----------
        root : ElementTree.Element
            The root element of the XML representation of the Ableton component.
        """
        for annotation_param_name, annotation_param_type in self.__annotations__.items():
            initialized_value = self.init_python_object_from_annotation(
                root, annotation_param_name, annotation_param_type
            )
            setattr(self, annotation_param_name, initialized_value)

    def candidate_tags(self, annotation_param_name: str):
        """
        Returns the XML tag names to try for a given annotation, in priority order.

        The primary tag is the camelCase form of the annotation name; any entries in
        the class-level ``_aliases`` mapping are appended as fallbacks so a single code
        path can parse multiple Ableton Live schema versions.
        """
        names = [self.snake_to_camel(annotation_param_name)]
        for alternative in self._aliases.get(annotation_param_name, []):
            if alternative not in names:
                names.append(alternative)
        return names

    def init_python_object_from_annotation(
        self, root: ElementTree.Element, annotation_param_name: str, annotation_param_type: type
    ):
        """
        Initializes a Python object from an annotation in the XML.

        Missing nodes resolve to ``None`` (or ``[]`` for list-typed fields) instead of
        raising, so that a set authored in a different Ableton Live version (with renamed
        or absent tags) still parses. Only the fields that are actually present are
        populated; the rest stay ``None``.

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
        candidate_names = self.candidate_tags(annotation_param_name)

        # we look in the node attributes first
        for param_name in candidate_names:
            if param_name in root.attrib:
                try:
                    return annotation_param_type(root.attrib[param_name])
                except (ValueError, TypeError):
                    return None

        # we look in the nodes' children (first matching tag wins)
        node = None
        for param_name in candidate_names:
            node = root.find(param_name)
            if node is not None:
                break

        is_native_type = annotation_param_type in [int, str, float]
        is_bool = annotation_param_type == bool
        is_dict = annotation_param_type == dict
        is_list_type = hasattr(annotation_param_type, "__origin__") and issubclass(
            annotation_param_type.__origin__, list
        )
        is_ableton_component = isinstance(annotation_param_type, type) and issubclass(
            annotation_param_type, AbletonComponent
        )

        # list-typed fields: a missing container is an empty list, not an error
        if is_list_type:
            if node is None:
                return []
            ableton_component = annotation_param_type.__args__[0]
            return [ableton_component(child) for child in node.findall("./")]

        # scalar / component fields: a missing node yields None (version tolerance)
        if node is None:
            return None

        if is_native_type or is_bool or is_dict:
            attrib_values = list(node.attrib.values())
            if not attrib_values:
                return None
            raw_value = attrib_values[0]
            if is_bool:
                new_param_value = raw_value == "true"
            elif is_dict:
                new_param_value = json.loads(raw_value)
            else:
                new_param_value = raw_value
        elif is_ableton_component:
            new_param_value = node
        else:
            return None

        try:
            initialized_value = annotation_param_type(new_param_value)  # casts to python object
        except (ValueError, TypeError):
            error_message = (
                f"Parameter {candidate_names[0]} with value {new_param_value} "
                f"is not type {annotation_param_type}"
            )
            print(error_message)
            return None
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
