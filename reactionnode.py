import xml.etree.ElementTree as ET 
import pandas as pd 


xmlfile = "teste01.xml" # variable that keeps the file i'm using, will search for it in the same folder

tree = ET.parse(xmlfile)
root = tree.getroot() #reactionlist
count = 0
solvent = catalyst = ""

for reaction in root: #each one of the reactions i the file
        count += 1
        cols = ["id", "description", "solvent", "catalyst"] 
        rows = [] 
        for child in reaction:
                if (child.tag == "{http://bitbucket.org/dan2097}source"):
                        description = child[1].text
                if (child.tag == "{http://bitbucket.org/dan2097}reactionSmiles"):
                        id = child.text
                if (child.tag == "{http://www.xml-cml.org/schema}spectatorList"):
                        for spectator in child:
                                if (spectator.attrib == "{'role': 'solvent'}"):
                                        solvent = spectator.attrib
                                if (spectator.attrib == "{'role': 'catalyst'}"):
                                        catalyst = spectator.attrib
        rows.append({"id": id, 
                "description": description, 
                "solvent": solvent, 
                "catalyst": catalyst}) 
        csvname = "reactionnode" + str(count)  #reactionnode#
        df = pd.DataFrame(rows, columns=cols)
        df.to_csv(csvname) 
