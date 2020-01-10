# -*- coding: UTF-8 -*-
import os

fileDir = "H:" + os.sep + "Code" + os.sep + "Java\\tale"
context = ''
fileFilter = ['txt', 'md', 'html', 'css', 'js']

def readFiles(filePath):
  global context
  for root, dirs, files in os.walk(filePath):
    for file in files:
      fileName = os.path.join(root, file)
      if (getSuffix(fileName) not in fileFilter):
        continue
      controlFile = open(fileName, 'r', encoding='UTF-8') 
      lines = controlFile.readlines()
      if lines.__len__() > 0:
        context = context + '$$$' + os.path.join(root, file) + '\n'
      for line in lines: 
        context = context + line
      context = context + '\n'
      controlFile.close()
    # for dir in dirs:
    #   readFiles(os.path.join(root, dir))

def getParentDir(path):
  return str(path)[:str(path).rfind(os.sep)]

def getSuffix(file):
  print(file)
  pointIndex = str(file).rfind('.')
  if pointIndex == -1:
    return ''
  return str(file)[pointIndex + 1:]

if __name__ == '__main__':
  readFiles(fileDir)
  # os.remove(os.path.join(fileDir, 'context'))
  f = open(os.path.join(fileDir, 'context'), 'w+', encoding='UTF-8')
  f.writelines(context)
  f.close()
