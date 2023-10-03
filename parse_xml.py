import xml.etree.ElementTree as ET
from box import Box
from box.box_list import BoxList

"""
# Parse the XML file
tree = ET.parse("test.xml")
root = tree.getroot()

def xml_to_dict(element):
    if len(element) == 0:
        return element.text
    result = {}
    for child in element:
        child_data = xml_to_dict(child)
        if child.tag in result:
            if type(result[child.tag]) is list:
                breakpoint()
                result[child.tag].append(child_data)
            else:
                breakpoint()
                result[child.tag] = [result[child.tag], child_data]
        else:
            result[child.tag] = child_data
    return result
"""



import xmltodict

xml_data = open("test.xml", "r").read()
data = xmltodict.parse(xml_data)
breakpoint()
#data = Box(data)
# childs = node.items()


def recursive_dict_iter(dictionary, parent_key=None):
    for key, value in dictionary.items():
        if isinstance(value, list):
            # Perform your action here for lists
            print(f"Found a list at key '{key}': {value}")
            dictionary[parent_key] = [f"{key}_{elem}" for elem in value]
            del dictionary[key]
            print(dictionary)
        elif isinstance(value, dict):
            # If the value is a dictionary, recursively iterate over it
            recursive_dict_iter(value, parent_key=key)



new_dict = recursive_dict_iter(data)
breakpoint()
# Create a Python dictionary to represent the object-like structure
data_object = {}

# Convert XML data to an object-like structure
for element in root:
    data_object[element.tag] = element.text