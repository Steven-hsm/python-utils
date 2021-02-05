import fileUtils
import interface
import re

intefaces = interface.getinterface()

scan_path = "E:\hotfix\pharmaux"

fileArray = fileUtils.get_file_in_ptah(scan_path)
for file in fileArray:
    remote_api = []
    lines = fileUtils.readFileAsArray(file)
    for interface in intefaces:
        for line in lines:
            if interface in line:
                matchGroup = re.match(r"(.*)"+interface+" (.*);(.*)", line, re.M | re.I)
                if matchGroup:
                    remote_api.append(matchGroup.group(2))
    lines = fileUtils.readFileAsArray(file)
    for api in remote_api:
        for line in lines:
            if api in line:
                matchGroup = re.match(r"(.*)"+api+"\.(.*)", line, re.M | re.I)
                if matchGroup:
                    print(line)
