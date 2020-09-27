
def readFileAsStr(fileName):
    data = ''
    with open(fileName, 'r',encoding='utf-8') as f:
        for line in f.readlines():
            line = line.strip()
            data += line
            data += '\n'
    return data

def readFileAsArray(fileName):
    data = []
    with open(fileName, 'r',encoding='utf-8') as f:
        for line in f.readlines():
            line = line.strip()
            data.append(line)
    return data

def readFileAsOriginalStr(fileName):
    data = ''
    with open(fileName, 'r',encoding='utf-8') as f:
        for line in f.readlines():
            data += line
    return data