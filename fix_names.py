import os
from glob import glob

proj_dir = "C:\\Users\\trist\\OneDrive\\Pulpit\\togglesneak1710\\src\\main\\java\\deez\\togglesneak"

def findnth(string, substring, n):
    parts = string.split(substring, n + 1)
    if len(parts) <= n + 1:
        return -1
    return len(string) - len(parts[-1]) - len(substring)

def get_names(file):
    names = []
    name_file = open(file, 'r')
    for line in name_file.readlines()[1:]:
        searge = line[:line.find(",")]
        name = line[line.find(',')+1:findnth(line, ',', 2)-2]
        names.append({"searge": searge, "name": name})
    name_file.close()
    return names

files = []
fields = get_names('fields.csv')
methods = get_names('methods.csv')
params = get_names('params.csv')

for dir,_,_ in os.walk(proj_dir):
    files.extend(glob(os.path.join(dir, "*.java")))

for file in files:
    print("Working with: " + file[file.rfind("\\"):])
    f = open(file, 'r')
    content = f.read()
    f.close()
    occurrences = 0
    for field in fields:
        occurrences += content.count(field["searge"])
        content = content.replace(field["searge"], field["name"])
    for method in methods:
        occurrences += content.count(field["searge"])
        content = content.replace(method["searge"], method["name"])
    for param in params:
        occurrences += content.count(field["searge"])
        content = content.replace(param["searge"], param["name"])
        
    f = open(file, 'w')
    f.write(content)
    f.close()
    print("Done - Replaced {0} occurrences\n".format(occurrences))

