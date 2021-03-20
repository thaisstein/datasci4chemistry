import xml.etree.ElementTree as ET 
import pandas as pd 


xmlfile = "teste01.xml" # variável quye vai guardar o aquivo que vou usar, vai procurar o arquivo na mesma pasta
#ver sobre o caminho

tree = ET.parse(xmlfile)
root = tree.getroot() #reactionlist
reactions = 0


#ET.dump(tree) #mos o conteúdo do xml
# é como um dicionário
# <> são *tags* , que está dentro em thon é *text*, o que tá dentro da tag são os *attributes*
# comando root.findall - iterar pelo xml 
for element in root.findall("./"): # number of reactions
        reactions += 1

#print (root[801][1].text)

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
        csvname = "reactionnode" + str(count)
        df = pd.DataFrame(rows, columns=cols)
        df.to_csv(csvname) 
