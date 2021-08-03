import glob
import sys
import xml.etree.ElementTree as ET
import pandas as pd
sys.setrecursionlimit(8000)
import itertools

# Query through a list of xml folder to look for a certain element
path = 'Enter Path here'

# Use the function to get the name of the files
def getFile(path):
    name = []
    for fname in glob.glob(path):
        name.append(fname)
    return name

all_files = getFile(path)


# Get the values from the elements in the xml tags
def get_tags(path):
    tags = []
    xmlTree = ET.parse(path)
    for elem in xmlTree.iter():
        if elem.tag == 'KEYWORD':
            tags.append(elem.text)
    return tags

# Run the get_tags function for all of the files in the folder
allEl_tags = list(map(get_tags,all_files))
allEl_tags = list(itertools.chain.from_iterable(allEl_tags))
df = pd.DataFrame(set(allEl_tags),columns=['tags'])