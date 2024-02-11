import json


def addRoutePath(list_files, file_paths):
    with open(list_files, "w") as token:
        token.write(json.dumps(file_paths))


def getRoutePath(list_files):
    with open(list_files) as f:
        list_files = json.loads(f.read())
    return list_files
