import os


def getTagName(filename):
    end = filename.split('\\')[-1]
    name = end.split('.')[0]
    return name


def get_types(imageList):
    imageList = imageList.split(',')
    print(imageList)
    for i in range(len(imageList)):
        imageList[i] = int(imageList[i])
    typeList = [{'tagName': 'no select', 'value': imageList}]
    nameIndex = {}
    filename = 'database\\tags'
    fileList = []
    for filepath, dirnames, filenames in os.walk(filename):
        for filename in filenames:
            fileList.append(os.path.join(filepath, filename))
    print(fileList)
    for filepath in fileList:
        count = 0
        with open(filepath, 'r', errors='ignore') as f:
            for line in f:  # 读取每一行
                for imageIndex in imageList:
                    if int(line) == int(imageIndex):
                        count = count + 1
                        if count == 1:
                            typeList.append({'tagName': getTagName(filepath),
                                             'value': [imageIndex]})
                            nameIndex[getTagName(filepath)] = len(typeList) - 1
                        else:
                            typeList[nameIndex[getTagName(filepath)]]['value'].append(imageIndex)
    print(typeList)
    return typeList
