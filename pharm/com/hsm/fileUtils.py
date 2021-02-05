import os


def readFileAsStr(fileName):
    data = ''
    with open(fileName, 'r', encoding='utf-8') as f:
        for line in f.readlines():
            line = line.strip()
            data += line
            data += '\n'
    return data


def readFileAsArray(fileName):
    data = []
    with open(fileName, 'r', encoding='utf-8') as f:
        for line in f.readlines():
            line = line.strip()
            data.append(line)
    return data


def readFileAsOriginalStr(fileName):
    data = ''
    with open(fileName, 'r', encoding='utf-8') as f:
        for line in f.readlines():
            data += line
    return data


def writeToFile(fileName, str):
    with open(fileName, 'a', encoding='utf-8') as f:
        f.write(str)


# 获取目录下的所有文件
def get_file_in_ptah(path):
    file_array = []
    for  dirpath, dirnames, filenames in os.walk(path):
        if len(dirnames) == 0 and len(filenames) > 0:
            for filename in filenames:
                if ".java" in filename:
                    file_array.append(dirpath + os.sep + filename)
    return file_array

