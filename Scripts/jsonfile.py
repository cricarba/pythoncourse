import json 
with open('sample-json-file.json') as fi :
    fileJson = json.load(fi)
    print(json.dumps(fileJson, indent=2))

    