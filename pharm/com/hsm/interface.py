import fileUtils
import re

# 获取接口名
def getinterface():
    intefaces = []
    lines = fileUtils.readFileAsArray(
        "E:\\hotfix\\pharmaux\\windranger-pharmaux-web\\src\\main\\resources\\dubbo\\dubbo-config.xml")
    for line in lines:
        matchGroup = re.match(r"(.*)<dubbo:reference interface=\"(.*)\"(.*)", line, re.M | re.I)
        if matchGroup:
            className = matchGroup.group(2)
            str = className.split(".")
            intefaces.append(str[len(str) - 1])
    return intefaces


