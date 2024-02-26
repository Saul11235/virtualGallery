# create function get_skins.js 
import os
def get_artworks():
    try:
        directory="../artworks"
        entries = os.listdir(directory)
        dirs = [entry for entry in entries if os.path.isdir(os.path.join(directory, entry))]
        return dirs
    except Exception as e:
        return []

def writeFilepath(path, namefile, content):
    filepath = os.path.join(path, namefile)
    try:
        with open(filepath, 'w') as file:
            file.write(content)
        print(f"Content successfully written to {filepath}")
    except Exception as e:
        print(f"Error writing to file: {e}")

writeFilepath("../js","get_artworks.js",
"""// no code manually this file is generated
var array_artworks= ['""" + "','".join(get_artworks()) + """'];""")
print(">> Created get_artworks.js finished!")
