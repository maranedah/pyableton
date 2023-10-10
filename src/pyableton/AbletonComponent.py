from xml.etree import ElementTree


class AbletonComponent:
    def __init__(self, root: ElementTree.Element):
        for param_name, param_type in self.__annotations__.items():
            # breakpoint()
            name_in_xml = self.snake_to_camel(param_name)
            node = root.find(name_in_xml)
            if issubclass(param_type, AbletonComponent):
                element_value = node
            elif node is not None:  # node exists
                if "Value" in node.attrib:
                    element_value = node.attrib["Value"]
                elif "LomId" in node.attrib:
                    element_value = node.attrib["LomId"]
                # else: raise error?
            elif name_in_xml in root.attrib:  # exists as an attribute
                element_value = root.attrib[name_in_xml]

            # if param_type._name == "List":
            # else:
            casted_value = param_type(element_value)
            setattr(self, param_name, casted_value)

    def snake_to_camel(self, input_string):
        parts = input_string.split("_")
        camel_case = "".join([part.capitalize() for part in parts])
        return camel_case
