# -*- coding: UTF-8 -*-
import os

newDir = "H:" + os.sep + "Test"
fileDir = "H:" + os.sep + "Code" + os.sep + "Java\\tale"
context = ''

def rebuildFiles(filePath):
  fileStart = False
  controlFile = open(filePath, encoding='UTF-8') 
  lines = controlFile.readlines()
  for line in lines: 
    if line.startswith('$$$'):
      fileStart = True
      newFilePath = line[3:-1]
      newFilePath = newFilePath.replace(fileDir, newDir)
      parentDir = getParentDir(newFilePath)
      if not os.path.exists(parentDir):
        os.makedirs(parentDir)
      newFile = open(newFilePath, 'w', encoding='UTF-8')
      continue
    if fileStart:
      newFile.write(line)

def getParentDir(path):
  return str(path)[:str(path).rindex(os.sep)]

if __name__ == '__main__':
  rebuildFiles(os.path.join(fileDir, 'context'))
