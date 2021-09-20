import glob
import json
from datetime import datetime

jsonFile = "./webern_*.json"

# find json file and load json
for fileName in glob.glob(jsonFile):
    with open(fileName) as f:
        file = json.load(f)

# Get current date to append to file name
now = datetime.today().strftime('%Y%m%d')

with open("webern_" + now + "_plantuml.txt", 'w') as textFile:
    textFile.write("@startjson")
    textFile.write("\n")
    textFile.write(json.dumps(file, indent=4))
    textFile.write("\n")
    textFile.write("@endjson")
